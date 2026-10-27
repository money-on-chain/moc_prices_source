import unittest
from datetime import timedelta
from types import SimpleNamespace
from unittest.mock import patch, sentinel

from moc_prices_source import server


class ResponseCacheConfigurationTests(unittest.TestCase):

    def test_redis_cache_uses_existing_connection_when_enabled(self):
        with patch.object(server, 'use_redis', True), \
                patch.object(server, 'get_redis', return_value=sentinel.redis) as get_redis:
            app = server.create_app()

        get_redis.assert_called_once_with()
        self.assertEqual(app.config['CACHE_TYPE'], 'RedisCache')
        self.assertEqual(app.config['CACHE_KEY_PREFIX'],
                         'moc_prices_source:response:')
        with app.app_context():
            self.assertIs(server.cache.cache._read_client, sentinel.redis)

    def test_simple_cache_does_not_connect_to_redis_when_disabled(self):
        with patch.object(server, 'use_redis', False), \
                patch.object(server, 'get_redis') as get_redis:
            app = server.create_app()

        get_redis.assert_not_called()
        self.assertEqual(app.config['CACHE_TYPE'], 'SimpleCache')


class GunicornBindTests(unittest.TestCase):

    def test_bind_formats_ipv4_and_ipv6_addresses(self):
        from gunicorn.app.base import BaseApplication
        from gunicorn.util import parse_address

        for host, expected in [('127.0.0.1', '127.0.0.1:7989'),
                               ('::1', '[::1]:7989'),
                               ('::', '[::]:7989')]:
            with self.subTest(host=host), \
                    patch.object(BaseApplication, 'run', autospec=True) as run:
                server.run_gunicorn(host, 7989)

            bind = run.call_args.args[0].cfg.bind[0]
            self.assertEqual(bind, expected)
            self.assertEqual(parse_address(bind), (host, 7989))


class CoinPairValueTests(unittest.TestCase):

    def setUp(self):
        self.client = server.app.test_client()
        with server.app.app_context():
            server.cache.clear()

    def test_failed_only_sub_coinpair_reports_zero_sources_without_500(self):
        def get_price_with_failed_source(*args, detail, **kwargs):
            detail['prices'] = [{
                'coinpair': 'RIF/USDT(MA)',
                'ok': False,
                'description': 'test source',
                'error': 'unavailable',
            }]
            return 1

        with patch.object(server, 'get_price', get_price_with_failed_source):
            response = self.client.get(
                '/api/coinpairs/get_value_simple?coinpair=ISLIQ_ROC')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), 1)

    def test_cached_value_is_not_shared_between_coinpairs(self):
        prices = {'BTC/USD': 100, 'RIF/USD': 2}

        def get_price_by_coinpair(coinpairs, detail, **kwargs):
            return prices[coinpairs]

        with patch.object(server, 'get_price', get_price_by_coinpair):
            for coinpair, price in prices.items():
                response = self.client.get(
                    '/api/coinpairs/get_value_simple',
                    query_string={'coinpair': coinpair})
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.get_json(), price)

    def test_cached_valid_coinpair_does_not_accept_invalid_case(self):
        for path in ('/api/coinpairs/get_value',
                     '/api/coinpairs/get_value_simple'):
            with self.subTest(path=path):
                with server.app.app_context():
                    server.cache.clear()
                with patch.object(server, 'get_price', return_value=123):
                    valid = self.client.get(
                        path, query_string={'coinpair': 'BTC/USD'})
                    lowercase = self.client.get(
                        path, query_string={'coinpair': 'btc/usd'})
                    uppercase_arg = self.client.get(
                        path, query_string={'COINPAIR': 'BTC/USD'})

                self.assertEqual(valid.status_code, 200)
                self.assertEqual(lowercase.status_code, 400)
                self.assertEqual(uppercase_arg.status_code, 400)


class CoinPairsValueCacheTests(unittest.TestCase):

    url = '/api/coinpairs/get_values'
    json = {'Accept': 'application/json'}

    def setUp(self):
        self.client = server.app.test_client()
        with server.app.app_context():
            server.cache.clear()
        self.calls = []

    def get_price(self, coinpairs, detail, **kwargs):
        self.calls.append(list(coinpairs))
        return {c: 1 for c in coinpairs}

    def get(self, query_string, headers):
        with patch.object(server, 'get_price', self.get_price):
            return self.client.get(
                self.url, query_string=query_string, headers=headers)

    def test_equivalent_requests_share_one_cache_entry(self):
        for coinpairs, accept in [
                ('BTC/USD,RIF/USD', 'application/json'),
                ('rif/usd,btc/usd', 'application/json'),
                (' BTC/USD, RIF/USD,', 'application/json, */*;q=0.1'),
                ('BTC/USD RIF/USD,BTC/USD', 'application/json; x=1')]:
            response = self.get({'coinpairs': coinpairs}, {'Accept': accept})
            self.assertEqual(response.status_code, 200)

        self.assertEqual(len(self.calls), 1)

    def test_plain_text_and_json_are_cached_separately(self):
        response = self.get({'coinpairs': 'BTC/USD'}, self.json)
        self.assertEqual(response.mimetype, 'application/json')

        with patch.object(server, 'coinpairs_report',
                          return_value='report') as report:
            response = self.get({'coinpairs': 'BTC/USD'},
                                {'Accept': 'text/plain'})
        self.assertEqual(response.mimetype, 'text/plain')
        report.assert_called_once()

    def test_wildcard_over_limit_is_not_served_from_omitted_arg_cache(self):
        self.assertEqual(self.get({}, self.json).status_code, 200)

        response = self.get({'coinpairs': '*'}, self.json)

        self.assertEqual(response.status_code, 403)

    def test_arg_name_is_case_sensitive_like_reqparse(self):
        # reqparse ignores COINPAIRS and answers with every coinpair, so that
        # response must not be cached as the BTC/USD one.
        self.assertEqual(
            self.get({'COINPAIRS': 'BTC/USD'}, self.json).status_code, 200)

        response = self.get({'coinpairs': 'BTC/USD'}, self.json)

        self.assertEqual(list(response.get_json()['values']), ['BTC/USD'])
        self.assertEqual(self.calls[-1], ['BTC/USD'])


class HashMethodTests(unittest.TestCase):

    @staticmethod
    def _args(coinpair):
        return str((('coinpair', coinpair),)).encode()

    def test_interleaved_calls_keep_their_own_key(self):
        hash_method = server.HashMethod('coinpair', pre='test')

        # flask-caching calls hash_method(x) and then .hexdigest(); another
        # request may hash in between on the same shared instance.
        btc = hash_method(self._args('BTC/USD'))
        rif = hash_method(self._args('RIF/USD'))

        self.assertIn('BTC/USD', btc.hexdigest())
        self.assertIn('RIF/USD', rif.hexdigest())
        self.assertNotEqual(btc.hexdigest(), rif.hexdigest())


class HealthCheckTests(unittest.TestCase):

    def test_health_check_returns_ok(self):
        response = server.app.test_client().get('/health_check')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'status': 'ok'})


class AccessLoggerTests(unittest.TestCase):

    def setUp(self):
        from gunicorn.config import Config
        cfg = Config()
        cfg.set('accesslog', '-')
        self.logger = server.access_logger_class()(cfg)

    def log(self, status='200 OK', user_agent='curl/8.0', **environ):
        resp = SimpleNamespace(status=status, headers=[], sent=2)
        req = SimpleNamespace(headers=[])
        environ = {'REQUEST_METHOD': 'GET', 'RAW_URI': '/api/info',
                   'PATH_INFO': '/api/info',
                   'SERVER_PROTOCOL': 'HTTP/1.1', 'REMOTE_ADDR': '10.0.1.169',
                   'HTTP_USER_AGENT': user_agent, **environ}
        with patch.object(self.logger.access_log, 'info') as info:
            self.logger.access(resp, req, environ, timedelta(seconds=1))
        return [fmt % atoms for (fmt, atoms), _ in info.call_args_list]

    def test_successful_health_check_is_not_logged(self):
        self.assertEqual(self.log(user_agent='ELB-HealthChecker/2.0',
                                  PATH_INFO='/health_check'), [])

    def test_other_successful_requests_with_health_check_user_agent_are_logged(self):
        self.assertEqual(len(self.log(user_agent='ELB-HealthChecker/2.0')), 1)

    def test_other_methods_on_health_check_are_logged(self):
        self.assertEqual(len(self.log(user_agent='ELB-HealthChecker/2.0',
                                      PATH_INFO='/health_check',
                                      REQUEST_METHOD='HEAD')), 1)

    def test_failed_health_check_is_logged(self):
        lines = self.log(status='503 SERVICE UNAVAILABLE',
                         user_agent='ELB-HealthChecker/2.0',
                         PATH_INFO='/health_check')
        self.assertEqual(len(lines), 1)
        self.assertIn(' 503 ', lines[0])

    def test_client_ip_comes_from_cloudflare_header(self):
        lines = self.log(HTTP_CF_CONNECTING_IP='203.0.113.7')
        self.assertTrue(lines[0].startswith('203.0.113.7 '))

    def test_invalid_cloudflare_header_falls_back_to_remote_addr(self):
        lines = self.log(HTTP_CF_CONNECTING_IP='not-an-ip')
        self.assertTrue(lines[0].startswith('10.0.1.169 '))


class MainTests(unittest.TestCase):

    def test_debug_refuses_non_loopback_host(self):
        with patch.object(server.app, 'run') as app_run:
            with self.assertRaises(SystemExit):
                server.main(host='0.0.0.0', debug=True)
        app_run.assert_not_called()

    def test_debug_allows_loopback_host(self):
        with patch.object(server.app, 'run') as app_run:
            server.main(host='127.0.0.1', port=7989, debug=True)
        app_run.assert_called_once_with(
            debug=True, host='127.0.0.1', port=7989)

    def test_production_uses_gunicorn(self):
        with patch.object(server, 'run_gunicorn') as run_gunicorn, \
             patch.object(server.app, 'run') as app_run:
            server.main(host='0.0.0.0', port=7989, debug=False)
        run_gunicorn.assert_called_once_with('0.0.0.0', 7989)
        app_run.assert_not_called()


if __name__ == '__main__':
    unittest.main()
