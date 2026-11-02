import ast
import logging
from decimal import Decimal
from ipaddress import IPv6Address, ip_address
from fnmatch import fnmatch as match
from tabulate import tabulate
from .types import normalize_obj, Serializable
from flask import (Flask, request, redirect, jsonify, make_response,
                   current_app, has_request_context)
from flask_restx import Api, Resource, reqparse, abort
from flask_cors import CORS
from flask_caching import Cache
from . import get_price, version
from . import ALL as AllCoinPairs
from .cli import command, option
from .redis_conn import get_redis, use_redis
from .cli_check import show_computed_pairs_fromula, summary, coinpairs_report
from .my_envs import envs
from .my_logging import LOG_FORMAT, LOG_DATE_FORMAT



title='MoC prices source API Rest webservice'
description="""

<br>
### Description

This is the API Rest webservice that comes integrated in
the python **moc_prices_source** package.

<br>
### Purpose

Simplify integrations with other environments than **Python**.

<br>
### Refrences

* [Source code in Github](https://github.com/money-on-chain/moc_prices_source)
* [Package from Python package index (PyPI)](https://pypi.org/project/moneyonchain-prices-source)

<br>
<br>

## Endpoints
"""


all_coinpairs = list([str(x) for x in AllCoinPairs])
all_coinpairs.sort()
max_coinpair_limit = envs(
    'MAX_COINPAIR_LIMIT', 12, envs.types.positive_integer)
flask_debug = envs('FLASK_DEBUG', False, envs.types.bool)
gunicorn_workers = envs(
    'GUNICORN_WORKERS', 1, envs.types.positive_integer)
gunicorn_timeout = envs(
    'GUNICORN_TIMEOUT', 60, envs.types.positive_integer)
health_check_user_agent = envs(
    'HEALTH_CHECK_USER_AGENT', 'ELB-HealthChecker')
HEALTH_CHECK_LOG_INTERVAL = envs(
    'HEALTH_CHECK_LOG_INTERVAL', 100, envs.types.positive_integer)


cache = Cache()
cors = CORS()
api = Api(
    prefix='/api',
    doc='/api/doc',
    version=f"v{version}",
    title=title,
    description=description,
)


def client_ip(environ):
    candidate = environ.get('HTTP_CF_CONNECTING_IP', '').strip()
    try:
        return str(ip_address(candidate))
    except ValueError:
        return environ.get('REMOTE_ADDR', '-')


class RequestClientLogFilter(logging.Filter):

    def filter(self, record):
        if has_request_context():
            message = record.getMessage()
            record.msg = f'client={client_ip(request.environ)} {message}'
            record.args = ()
        return True

def create_app():
    
    app = Flask(__name__)
    if not any(isinstance(item, RequestClientLogFilter)
               for item in app.logger.filters):
        app.logger.addFilter(RequestClientLogFilter())
    
    if use_redis:
        app.config["CACHE_TYPE"] = "RedisCache"
        app.config["CACHE_REDIS_HOST"] = get_redis()
        app.config["CACHE_KEY_PREFIX"] = "moc_prices_source:response:"
    else:
        app.config["CACHE_TYPE"] = "SimpleCache"
    cache.init_app(app)
   
    api.init_app(app)

    app.config["CORS_RESOURCES"] = {r'/*': {"origins": "*"}}
    cors.init_app(app)
    
    app.logger.setLevel(1)
    app.logger.info(f"{title} (v{version})")
    app.logger.info(f"{len(all_coinpairs)} available coinpairs")
    app.logger.info(f"CONFIG: {use_redis=}")
    app.logger.info(f"CONFIG: {max_coinpair_limit=}")

    return app

app = create_app()



def get_coin_pairs(
        wildcard: str = "*",
        coinpairs_base: list = None
        ) -> list:
    """
    Get all coin pairs that match the wildcard.
    """
    if coinpairs_base is None:
        coinpairs_base =  AllCoinPairs
    wildcards_base = str(wildcard).lower().replace(" ", ",").split(",")
    wildcards = list(set([w for w in wildcards_base if w]))
    coinpairs = []
    for w in wildcards:
        f = filter(lambda i: match(str(i).lower(), w), coinpairs_base)
        f = list(set(list(f)))
        coinpairs.extend(f)
    coinpairs = list(set(coinpairs))
    coinpairs.sort()
    return coinpairs



class CacheKeyMaker():

    def __init__(self, *args, headers=[],
                 info=lambda x: None, pre="") -> None:
        self._pre = pre
        self._info = info
        # Arg names stay case-sensitive, as reqparse reads them
        self._args = list(map(lambda x: str(x).strip(), list(args)))
        self._headers = list(map(lambda x: str(x).strip().lower(),
                                 list(headers)))

    def __call__(self) -> str:

        path = request.path

        # The key is built from what the handlers actually use, so request
        # variants that produce the same response share one cache entry
        # (otherwise each variant is a miss that queries every source).

        args = request.args.to_dict(flat=True)
        filtered_args = {k: v for k, v in args.items() if k in self._args}
        if 'coinpairs' in filtered_args:
            # Only when present: reqparse returns an omitted arg's default
            # unexpanded, which handlers treat differently from '*'.
            filtered_args['coinpairs'] = ','.join(
                str(c).lower() for c in get_coin_pairs(
                    filtered_args['coinpairs']))
        sorted_args = sorted(filtered_args.items())

        headers = {k.lower(): v for k, v in request.headers.items()}
        filtered_headers = {k: v for k, v in headers.items(
            ) if k in self._headers}
        if 'accept' in self._headers:
            # Handlers only check whether text/plain is accepted
            filtered_headers['accept'] = 'text/plain' in headers.get(
                'accept', 'text/plain')
        sorted_headers = sorted(filtered_headers.items())

        key = f"{self._pre}|{path}|{sorted_args}|{sorted_headers}"
        
        self._info(f"cache key = {repr(key)}")

        return key



class HashMethod():

    def __init__(self, *options, info=lambda x: None, pre="") -> None:
        self._pre = pre
        self.info = info
        self.options = list(map(lambda x: str(x).strip().lower(),
                                list(options)))
        self.out = []

    def __call__(self, x) -> "HashMethod":
        # flask-caching shares this instance across requests and calls
        # hexdigest() on the returned object, so return a new one: mutating
        # self lets concurrent requests read each other's cache key.
        digest = HashMethod(*self.options, info=self.info, pre=self._pre)
        # flask-caching passes the query args as bytes, which literal_eval
        # rejects; left undecoded, every coinpair shared one cache key.
        if isinstance(x, bytes):
            x = x.decode()
        try:
            values = ast.literal_eval(x)
        except (ValueError, SyntaxError):
            values = []
        for key, value in values:
            # reqparse treats argument names and coinpair choices as
            # case-sensitive, so the cache key must preserve both.
            key = str(key)
            if key in self.options:
                value = str(value)
                if key=='coinpairs' and value:
                    value = ','.join([str(c).lower() for c in get_coin_pairs(
                        value)])
                digest.out.append((key, value))
        return digest

    def hexdigest(self):
        hash_ = repr(self.out) if self.out else ""
        if self._pre:
            hash_ = f"{self._pre}{hash_}"
        self.info(f"hash = {repr(hash_)}")
        return hash_



@app.after_request
def add_header(response):
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    response.headers["Cache-Control"] = 'public, max-age=0'
    return response



@app.before_request
def before_request_func():
    if request.path.startswith('/api/doc'):
        if request.args.get('url'):
            return redirect('/api/doc')



@app.errorhandler(404)
def page_not_found(e):
    if request.path.startswith('/api/'):
        return jsonify(
            code=e.code,
            name=e.name,
            description=e.description
        ), 404
    return redirect('/api/doc')



@app.route('/')
def index():
    return redirect('/api/doc')


@app.route('/health_check')
def health_check():
    return jsonify(status='ok'), 200



coinpairs_ns = api.namespace('coinpairs',
                             description='Coinpairs related operations')



@coinpairs_ns.route('/')
class CoinPairsList(Resource):

    @api.doc(produces=['application/json', 'text/plain'])
    def get(self):
        """Shows a list of all supported coinpairs"""

        accept = request.headers.get('Accept', 'text/plain')
        pairs = AllCoinPairs[:]
        pairs.sort()
        
        if 'text/plain' in accept:
            text = tabulate(
                list([ (str(x),
                        x.name_base,
                        str(x.from_) if x.from_ else '',
                        str(x.to_) if x.to_ else '',
                        x.variant if x.variant else '',
                        x.description or x.short_description
                        ) for x in pairs]),
                headers=['Name', 'Base', 'From', 'To', 'Variant',
                         'Description'],
                tablefmt="simple",
                stralign="left",
                numalign="right"
            )
            response = make_response(text, 200)
            response.mimetype = "text/plain"
            return response
        else:
            return list([{'name': str(x),
                          'base': x.name_base,
                          'from': str(x.from_) if x.from_ else None,
                          'to': str(x.to_) if x.to_ else None,
                          'variant': x.variant,
                          'description': x.description or x.short_description}
                          for x in pairs])



@coinpairs_ns.route('/computed_coinpair_formulas')
class ComputedCoinpairFormulas(Resource):

    @api.doc(produces=['text/plain'])
    def get(self):
        """
        Displays the formulas used for the computed coinpair
        
        In plain text
        """
        
        text = show_computed_pairs_fromula()
        response = make_response(text, 200)
        response.mimetype = "text/plain"
        return response



coinpair_value_get = reqparse.RequestParser()
coinpair_value_get.add_argument(
    'coinpair',
    choices = all_coinpairs,
    type = str,
    help = 'Coinpair symbols')

bad_coinpair_choice = (400, 'Bad coinpair choice')
coinpair_value_not_found = (404, 'Coinpair value not found')

@coinpairs_ns.route('/get_value')
@coinpairs_ns.response(200, 'Success!')
@coinpairs_ns.response(*bad_coinpair_choice)
@coinpairs_ns.response(*coinpair_value_not_found)
class CoinPairValue(Resource):

    @coinpairs_ns.expect(coinpair_value_get)
    @cache.cached(
        timeout=5,
        query_string=True,
        hash_method=HashMethod(
            'coinpair',
            pre="get_coinpair_value",
        )
    )
    def get(self):
        """Get the price of a specific coinpair"""

        args = coinpair_value_get.parse_args()
        coinpair = args['coinpair']

        if coinpair not in all_coinpairs:
            abort(*bad_coinpair_choice)

        current_app.logger.info(
            f"Asking for the value of {coinpair}")

        detail = {}
        value = get_price(
            coinpairs=coinpair,
            detail=detail,
            serializable=True,
            ignore_zero_weighing=True)

        value = normalize_obj(value)

        sources_count = {}
        sources_count_ok = {}
        for p in detail.get('prices', []):
            sub_coinpair = p.get('coinpair', 'unknown')
            sources_count[sub_coinpair] = sources_count.get(
                sub_coinpair, 0) + 1
            sources_count_ok[sub_coinpair] = sources_count_ok.get(
                sub_coinpair, 0)
            if p.get('ok'):
                sources_count_ok[sub_coinpair] += 1
            else:
                source = p.get('description', 'unknown')
                error = p.get('error', 'unknown')
                if coinpair==sub_coinpair:
                    current_app.logger.warning(f"{coinpair} --> {source} {error}")
                else:
                    current_app.logger.warning(
                        f"{sub_coinpair} for {coinpair} --> {source} {error}")

        for sub_coinpair, p in detail.get('values', {}).items():
            error = p.get('error')
            if error:
                if coinpair==sub_coinpair:
                    current_app.logger.warning(f"{coinpair} --> {error}")
                else:
                    current_app.logger.warning(
                        f"{sub_coinpair} for {coinpair} --> {error}")

        source_parts = [
            f"{sources_count_ok[k]} of {v}" if k == coinpair and len(sources_count) == 1
            else f"{k}: {sources_count_ok[k]} of {v}"
            for k, v in sources_count.items()]
        source_suffix = f" (sources: {', '.join(source_parts)})" if source_parts else ''

        if value is None:
            current_app.logger.error(f"Not value for {coinpair}{source_suffix}")
            abort(*coinpair_value_not_found)
        else:
            current_app.logger.info(f"Value for {coinpair}: {value}{source_suffix}")

        out = {}
        out['required_coinpair'] = coinpair 
        out['value'] = value
        out['detail'] = detail

        return out



@coinpairs_ns.route('/get_value_simple')
@coinpairs_ns.response(200, 'Success!')
@coinpairs_ns.response(*bad_coinpair_choice)
@coinpairs_ns.response(*coinpair_value_not_found)
class CoinPairValueSimple(Resource):

    @coinpairs_ns.expect(coinpair_value_get)
    @cache.cached(
        timeout=5,
        query_string=True,
        hash_method=HashMethod(
            'coinpair',
            pre="get_coinpair_value_simple",
        )
    )
    def get(self):
        """Get the price of a specific coinpair (simple, no details)"""
        return CoinPairValue.get(self)['value']



def get_set_of_prices(*args,
                      detail: dict = {},
                      plain_text: bool = False,
                      plain_text_summary: bool = False,
                      md: bool = False) -> dict:
        
        if not args:
            raise ValueError("No arguments provided")
        
        if len(args)==1:
            if isinstance(args[0], (list, tuple)):
                args = list(args[0])
            else:
                args = [args[0]]
        args = [str(x).strip() for x in args if str(x).strip()]

        if not args:
            raise ValueError("No arguments provided")
        
        wildcard = ','.join(args)
        
        coinpairs = get_coin_pairs(wildcard)

        if not coinpairs:
            raise ValueError("No coinpairs provided")

        if plain_text:
            if plain_text_summary:
                out = summary(
                    coinpairs = coinpairs,
                    md = md)
            else:
                out = coinpairs_report(
                    coinpairs = coinpairs,
                    data = detail)
        else:
            values = get_price(
                coinpairs = coinpairs,
                detail = detail,
                serializable = True,
                ignore_zero_weighing = True)

            if values is None:
                values = {}

            if isinstance(values, (Serializable, Decimal, float, int, bool)):
                values = {coinpairs[0]: values}

            for cp in coinpairs:
                if cp not in values:
                    values[cp] = None

            out = {
                'values': normalize_obj(values),
                'detail': detail
            }
        return out

coinpairs_values_get = reqparse.RequestParser()
coinpairs_values_get.add_argument(
    'coinpairs',
    default="*",
    required=False,    
    type = lambda s: get_coin_pairs(wildcard=s),
    help = 'Set of coinpairs symbols')
bad_coinpairs_set = (400, 'Bad set of coinpairs symbols')
max_coinpairs_reached = (403, 
    f'Forbidden, max number of pairs reached ({max_coinpair_limit})')
coinpairs_value_not_found = (404, 'Non coinpairs value found')

@coinpairs_ns.route('/get_values')
@coinpairs_ns.response(200, 'Success!')
@coinpairs_ns.response(*bad_coinpairs_set)
@coinpairs_ns.response(*max_coinpairs_reached)
@coinpairs_ns.response(*coinpairs_value_not_found)
class CoinPairsValue(Resource):

    @api.doc(produces=['application/json', 'text/plain'])
    @coinpairs_ns.expect(coinpairs_values_get)
    @cache.cached(
        timeout=10,
        key_prefix=CacheKeyMaker(
            'coinpairs',
            headers=['Accept'],
            pre="get_coinpairs_value"))
    def get(self):
        """
        Get the price of a specific set of coinpairs
        
        The __coinpairs__ parameter is required.
        It represents the pairs you want to get the price for.
        
        It supports:

        * A single parameter like __BTC/USD__
        * Multiple parameters in a list, e.g.: __BTC/USD,USD/ARS__
        * Accepts wildcards, e.g., __*/ARS__
        * Or combinations, e.g.: __BTC/USD,*/ARS__

        """

        accept = request.headers.get('Accept', 'text/plain')
        plain_text = 'text/plain' in accept

        args = coinpairs_values_get.parse_args()
        coinpairs = args['coinpairs']

        if not coinpairs:
            abort(*bad_coinpairs_set)

        if len(coinpairs)>max_coinpair_limit:
            abort(*max_coinpairs_reached)

        if len(coinpairs)==1:
            current_app.logger.info(f"Asking for the value of {coinpairs[0]}")
        else:
            current_app.logger.info(f"Asking for the value of {len(coinpairs)} coinpairs")

        detail = {}
       
        out = get_set_of_prices(coinpairs,
                                detail = detail,
                                plain_text = plain_text)

        source_summaries = self._extra_log(coinpairs, detail,
                                           log_counts=plain_text)

        if not out:
            abort(*coinpairs_value_not_found)       
        
        # The plain text report is a str, without per-coinpair values
        if not plain_text:
            for coinpair, value in out['values'].items():
                source_suffix = (f" (sources: {source_summaries[coinpair]})"
                                 if coinpair in source_summaries else '')
                if value is None:
                    current_app.logger.error(
                        f"No value for {coinpair}{source_suffix}")
                else:
                    current_app.logger.info(
                        f"Value for {coinpair}: {value}{source_suffix}")

        if plain_text:
            response = make_response(out, 200)
            response.mimetype = "text/plain"
            return response
        else:
            return out

    @staticmethod
    def _extra_log(coinpairs, detail, log_counts=False):
        warn, info  = current_app.logger.warning, current_app.logger.info
        source_summaries = {}
        values = detail.get('values', {})
        prices = detail.get('prices', {})
        for coinpair in map(str, coinpairs):
            sub_coinpairs = values.get(coinpair, {}).get(
                "requirements", [coinpair])
            sources_count = {}
            sources_count_ok = {}
            for p in prices:
                sub_coinpair = p.get('coinpair', 'unknown')
                if sub_coinpair in sub_coinpairs:
                    sources_count[sub_coinpair] = sources_count.get(
                        sub_coinpair, 0) + 1
                    if p.get('ok'):
                        sources_count_ok[sub_coinpair] = sources_count_ok.get(
                            sub_coinpair, 0) + 1
                    else:
                        source = p.get('description', 'unknown')
                        error = p.get('error', 'unknown')
                        str_value = f"{source} {error}"
                        if coinpair==sub_coinpair:
                            str_title = coinpair
                        else:
                            str_title = f"{sub_coinpair} for {coinpair}"
                        warn(f"{str_title} --> {str_value}")
            if sources_count:
                source_parts = [
                    f"{sources_count_ok.get(k, 0)} of {v}"
                    if k == coinpair and len(sources_count) == 1
                    else f"{k}: {sources_count_ok.get(k, 0)} of {v}"
                    for (k, v) in sources_count.items()]
                source_summaries[coinpair] = ', '.join(source_parts)
                if log_counts:
                    info(f"Sources count for {coinpair}: "
                         f"{source_summaries[coinpair]}")
        return source_summaries



@coinpairs_ns.route('/summary')
@coinpairs_ns.response(200, 'Success!')
@coinpairs_ns.response(*bad_coinpairs_set)
class Summary(Resource):

    @api.doc(produces=['text/markdown', 'text/plain'])
    @coinpairs_ns.expect(coinpairs_values_get)
    @cache.cached(
        timeout=10,
        key_prefix=CacheKeyMaker(
            'coinpairs',
            headers=['Accept'],
            pre="get_summary"))
    def get(self):
        """
        Show how the data is obtained

        Gets a summary of subset of coinpairs or all coinpairs ("*").
        Showing information on how the data is obtained.
        
        It will be displayed in plain text or Markdown.

        The __coinpairs__ parameter is required.
        It represents the pairs you want to get the price for.
        
        It supports:

        * A single parameter like __BTC/USD__
        * Multiple parameters in a list, e.g.: __BTC/USD,USD/ARS__
        * Accepts wildcards, e.g., __*/ARS__
        * Or combinations, e.g.: __BTC/USD,*/ARS__

        """

        accept = request.headers.get('Accept', 'text/plain')
        md = not('text/plain' in accept)

        args = coinpairs_values_get.parse_args()
        coinpairs = args['coinpairs']

        if not coinpairs:
            abort(*bad_coinpairs_set)
      
        out = get_set_of_prices(coinpairs,
                                detail = {},
                                plain_text = True,
                                plain_text_summary = True,
                                md = md)
        
        response = make_response(out, 200)
        response.mimetype = "text/plain"
        return response



@api.route('/info')
class Info(Resource):

    def get(self):
        """Shows API info related"""
        return {
            'name:': title,
            'version' : version,
            'use_redis': use_redis,
            'max_coinpair_limit': max_coinpair_limit
        }



LOOPBACK_HOSTS = ('127.0.0.1', 'localhost', '::1')
ACCESS_LOG_FORMAT = (
    'client=%(h)s request="%(r)s" status=%(s)s '
    'bytes=%(b)s referer="%(f)s" agent="%(a)s"')


def access_logger_class():
    # Imported here so the library can be imported where gunicorn
    # is not supported (e.g. Windows).
    from gunicorn.glogging import Logger

    class AccessLogger(Logger):

        error_fmt = LOG_FORMAT.replace('%(name)s', 'gunicorn')
        access_fmt = LOG_FORMAT
        datefmt = LOG_DATE_FORMAT

        def setup(self, cfg):
            super().setup(cfg)
            for handler in self.access_log.handlers:
                if getattr(handler, '_gunicorn', False):
                    handler.setFormatter(logging.Formatter(
                        self.access_fmt, self.datefmt))

        def __init__(self, cfg):
            super().__init__(cfg)
            self.suppressed_health_checks = 0

        def atoms(self, resp, req, environ, request_time):
            atoms = super().atoms(resp, req, environ, request_time)
            # Behind Cloudflare and the ALB, REMOTE_ADDR is the ALB node.
            # The ALB only accepts requests coming through Cloudflare, which
            # sets this header; non-IP values are ignored.
            atoms['h'] = client_ip(environ)
            return atoms

        def access(self, resp, req, environ, request_time):
            # Summarize successful probes periodically; keep failures visible.
            status = str(resp.status).split(None, 1)[0]
            if (environ.get('PATH_INFO') == '/health_check'
                    and environ.get('REQUEST_METHOD') == 'GET'
                    and status == '200'
                    and (not health_check_user_agent or
                         environ.get('HTTP_USER_AGENT', '').startswith(
                             health_check_user_agent))):
                self.suppressed_health_checks += 1
                if self.suppressed_health_checks == HEALTH_CHECK_LOG_INTERVAL:
                    self.access_log.info(
                        'Received %d successful health checks',
                        HEALTH_CHECK_LOG_INTERVAL)
                    self.suppressed_health_checks = 0
                return
            super().access(resp, req, environ, request_time)

    return AccessLogger


def run_gunicorn(host, port, workers=gunicorn_workers,
                 timeout=gunicorn_timeout):
    # Imported here so the library can be imported where gunicorn
    # is not supported (e.g. Windows).
    from gunicorn.app.base import BaseApplication

    class Server(BaseApplication):

        def load_config(self):
            try:
                IPv6Address(host)
            except ValueError:
                bind_host = host
            else:
                bind_host = f'[{host}]'
            self.cfg.set('bind', f'{bind_host}:{port}')
            self.cfg.set('workers', workers)
            self.cfg.set('worker_class', 'sync')
            # Price requests can wait on slow upstream sources plus a retry
            self.cfg.set('timeout', timeout)
            self.cfg.set('accesslog', '-')
            self.cfg.set('access_log_format', ACCESS_LOG_FORMAT)
            self.cfg.set('logger_class', access_logger_class())
            # Runtime admin socket (gunicorn >= 25.1) is not used
            self.cfg.set('control_socket_disable', True)

        def load(self):
            return app

    Server().run()


def main(host='0.0.0.0', port=7989, debug=False):
    if debug:
        # The Werkzeug debugger allows remote code execution, so the
        # development server is never exposed beyond loopback.
        if host not in LOOPBACK_HOSTS:
            raise SystemExit(
                f"FLASK_DEBUG is only allowed on loopback hosts, not {host}")
        app.run(debug=True, host=host, port=port)
    else:
        run_gunicorn(host, port)


@command()
@option('-a', '--addr', 'host', type=str,
        default='0.0.0.0', help='Server host addr.')
@option('-p', '--port', 'port', type=int,
        default=7989, help='Server port.')
@option('-e', '--show-envs', 'show_envs', is_flag=True,
        help='Show used ENV variables used and exit.')
def server_cli(host, port, show_envs=False):
    """MoC prices source API Rest webservice"""
    if show_envs:
        print(envs)
        return
    main(debug=flask_debug, host=host, port=port)



if __name__ == '__main__':
    main(debug=flask_debug)
