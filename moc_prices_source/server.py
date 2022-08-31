import sys
from os.path  import dirname, abspath
from flask import Flask, request, redirect, jsonify
from flask_restx import Api, Resource, reqparse
from decimal import Decimal
from flask_cors import CORS

bkpath   = sys.path[:]
base_dir = dirname(abspath(__file__))
sys.path.append(dirname(base_dir))

from moc_prices_source import get_price, ALL, version

sys.path = bkpath


title='MoC prices source API Rest webservice',
description="""

<br>
### Description

This is the API Rest webservice that comes integrated in the python **moc_prices_source** package.

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

all_coinpairs = list([str(x) for x in ALL])

app = Flask(__name__)

api = Api(
    app,
    prefix='/api',
    doc='/api/doc',
    version=f"v{version}",
    title=title,
    description=description,
)

CORS(app, resources={r'/*': {'origins': '*'}})



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



price_ns = api.namespace('price', description='Price related operations')



@price_ns.route('/')
class Price(Resource):

    def get(self):
        '''Get coinpairs price'''
        coinpairs = all_coinpairs
        out = {}
        detail = {}
        value = get_price(coinpairs=coinpairs, detail=detail, serializable=True)
        if isinstance(value, dict):
            value = dict([(str(k), float(v)) for (k, v) in value.items()])
        if isinstance(value, Decimal):
            value = float(value)
        out['required_coinpairs'] = coinpairs 
        out['value'] = value
        out['detail'] = detail
        return out



if __name__ == '__main__':
    app.run(debug=True)
