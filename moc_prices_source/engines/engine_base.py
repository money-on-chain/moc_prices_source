import requests
import datetime
from os.path import basename
from decimal import Decimal
from   coins import *

#RIF_BTC = "RIF/BTC"
#BTC_USD = "BTC/USD"



class Base(object):

    _name        = "base"
    _description = "Base Engine"
    _uri         = "http://api.pricefetcher.com/BTCUSD"
    _coinpair    = BTC_USD
    _timeout     = 10


    @property
    def name(self):
        return self._name


    @property
    def description(self):
        return self._description


    @property
    def uri(self):
        return self._uri


    @property
    def coinpair(self):
        return self._coinpair


    @property
    def timeout(self):
        return self._timeout


    def _clean_output_values(self):
        self._price     = None
        self._volume    = None
        self._timestamp = None
        self._error     = None
        self._time      = None


    def __init__(self, session=None):
        if not session:
            session = requests.Session()
        self._session = session
        self._clean_output_values()


    @property
    def price(self):
        return self._price


    @property
    def volume(self):
        return self._volume


    @property
    def timestamp(self):
        return self._timestamp


    @property
    def error(self):
        return self._error


    @property
    def time(self):
        return self._time


    @staticmethod
    def _name_from_file(_file):
        name = basename(_file)
        if name.endswith('.py'):
            name = name[:-3]
        return name


    @staticmethod
    def _now():
        return datetime.datetime.now().replace(microsecond=0)


    @staticmethod
    def _utcfromtimestamp(timestamp):
        return datetime.datetime.utcfromtimestamp(int(timestamp))


    def _map(self, data):
        return {
            'price':  data['last'],
            'volume': data['volume'],
            'timestamp': self._utcfromtimestamp(data['timestamp']) }


    def __bool__(self):
        return not(bool(self._error))


    def __str__(self):
        name  = '{} {}'.format(self.description, self.coinpair
            ) if self.description else self.name
        if self.price == None:
            return name
        value = self.price if self else self.error
        return '{} = {}'.format(name, value)


    @property
    def as_dict(self):
        out = {}
        for attr in [
            'coinpair',
            'description',
            'error',
            'name',
            'price',
            'timeout',
            'timestamp',
            'uri',
            'volume',
            'time']:
            out[attr] = getattr(self, attr, None)
        out['ok'] = bool(self)
        return out


    def __call__(self):

        start_time = datetime.datetime.now()

        session = self._session
        self._clean_output_values()

        try:
            response = session.get(self.uri, timeout=self.timeout)
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            self._error = e
            return False
        except Exception as e:
            self._error = e
            return False

        if not response:
            self._error = "No response from server"
            return False

        if response.status_code != 200:
            self._error = "Response error (code {})".format(
                response.status_code)
            return False

        try:
            response = response.json()
        except Exception:
            self._error = "Response format error (not JSON)"
            return False

        try:
            info = self._map(response)
            self._price = Decimal(str(info['price']))
        except Exception:
            self._error = "Engine error (bad mapping)"
            return False

        if 'timestamp' in info:
            if isinstance(info['timestamp'], datetime.datetime):
                self._timestamp = info['timestamp']
            else:
                self._error = "Engine error (bad mapping)"
                return False
        else:
            self._timestamp = self._now()

        if 'volume' in info:
            try:
                self._volume = Decimal(str(info['volume']))
            except Exception:
                self._error = "Engine error (bad mapping)"
                return False
        else:
            self._volume = 0.0

        self._time = datetime.datetime.now() - start_time

        return True

if __name__ == '__main__':
    print("File: {}, Ok!".format(repr(__file__)))
