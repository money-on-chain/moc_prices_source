import datetime, requests
from os.path import dirname, abspath
from json import load, dumps, loads
from json.decoder import JSONDecodeError
from sys import stderr
from statistics import median as median_base
from statistics import mean as mean_base
from tabulate import tabulate
from decimal import Decimal
from os import environ
from typing import Tuple
from .conf import get



env_pre = 'MOC_PRICES_SOURCE'
on_remote_differences_options = ['halt', 'error', 'remote', 'local']

enabled = None
url = None
refresh_time_in_minutes = 60
on_remote_differences = on_remote_differences_options[0]
envs = {}

def call_back(options):

    enabled = None if not 'enabled' in options else options['enabled'] 
    if not(isinstance(enabled, bool) or enabled==None):
        raise ValueError('enabled must be bool or null')
    
    url = None if not 'url' in options else options['url'] 
    if not(isinstance(url, str) or url==None):
        raise ValueError('url must be str or null')

    refresh_time_in_minutes = 60 if not 'refresh_time_in_minutes' in options else options['refresh_time_in_minutes']
    if not(isinstance(refresh_time_in_minutes, int)):
        raise ValueError('refresh_time_in_minutes must be integer')
    if refresh_time_in_minutes<1:
        raise ValueError('refresh_time_in_minutes must be < 1')

    on_remote_differences = on_remote_differences_options[0] if not 'on_remote_differences' in options else options['on_remote_differences']
    if not(isinstance(on_remote_differences, str)):
        raise ValueError('on_remote_differences must be str')
    on_remote_differences = on_remote_differences.lower().strip()
    if on_remote_differences not in on_remote_differences_options:
        raise ValueError('on_remote_differences must be ' + ', '.join(map(repr, on_remote_differences_options[:-1])) + ' or ' + repr(on_remote_differences_options[-1]))

    return {
        'url': url,
        'refresh_time_in_minutes': refresh_time_in_minutes,
        'on_remote_differences': on_remote_differences
    }

kargs = dict(
    out          = locals(),
    call_back    = call_back,
    files        = ['remote_weighing.json', 'remote_weighing_default.json'],
    env_pre      = env_pre,
    dir_         = '/data/',
    copy_to_home = False,
    places       = dirname(abspath(__file__)))

get(**kargs)


filename = dirname(abspath(__file__)) + '/data/weighing.json'


class WeighingException(Exception):
    pass


def get_json_file():

    def config_error(e, source, s="Config file error\nLocation: {}\n{}"):
        print(s.format(source, e), file=stderr)
        exit(1)

    def validate_json_data(data):       
        if not isinstance(data, dict):
            return False
        for key, value in data.items():
            if isinstance(value, int):
                data[key]=float(value)
        for key, value in data.items():
            if not isinstance(key, str):
                return False
            if not isinstance(value, float):
                return False
        return True

    try:
        with open(filename) as json_file:
            data = load(json_file)
    except JSONDecodeError as e:
        config_error(e, filename)
    except FileNotFoundError as e:
        config_error('File not found!', filename)

    if not validate_json_data(data):
        str_err_map = "Bad mapping, has to be a dictionary with string keys and float values"
        config_error(str_err_map, filename)
    
    if enabled and  url and not(on_remote_differences=='local') :
        try:
            url_data = validate_json_data(requests.get(url).json())
        except:
            url_data = None
        if url_data and url_data!=data:
            if on_remote_differences=='error':
                raise WeighingException
            if on_remote_differences=='halt':
                print("Error: differences between local and remote weighing", file=stderr)
                exit(1)
            if on_remote_differences=='remote':
                data = url_data

    env = env_pre + "_WEIGHING_OVERRIDE"
    override_raw = environ.get(env, None)
    if override_raw:
        str_error = "Env var {} error: {}"
        try:
            override = loads(override_raw)
        except JSONDecodeError as e:
            config_error(e, env, str_error)
        if not validate_json_data(override):
            str_err_map = "Bad mapping, has to be a dictionary with string keys and float values"
            config_error(str_err_map, env, str_error)

        data = override

    return data



class Weighing(object):

    def __init__(self, refresh_time=datetime.timedelta(minutes=refresh_time_in_minutes)):
        self._data = {}
        self._last_load = None
        self._refresh_time = refresh_time
        self._load()

    def _load(self):

        if ((self._last_load is None) or (
            (datetime.datetime.now() - self._last_load) > self._refresh_time)):

            data = get_json_file()

            if isinstance(data, dict):
                ok = True
                try:
                    for key, value in data.items():
                        data[key] = Decimal(str(value))
                except:
                    ok = False

                if ok:
                    for key, value in data.items():
                        self._data[key] = value
                    self._last_load = datetime.datetime.now()

    @property
    def as_dict(self):
        self._load()
        return dict(self._data)

    @property
    def as_json(self):
        self._load()
        return dumps(dict([(k, float(v)) for k, v in self._data.items()]), indent=4)

    @property
    def names(self):
        return list(self.as_dict.keys())

    def __call__(self, name):
        return  self.as_dict.get(name, Decimal('0.0'))

    @property
    def last_load(self):
        return self._last_load

    @property
    def refresh_time(self):
        return self._refresh_time

    def __str__(self):
        return tabulate(list(self.as_dict.items()),
            headers=['Engine', 'Weigh'])



weighing = Weighing()


def validate_values_and_weights(values: list,
                                weights: list) -> Tuple[list, list]:

    if not isinstance(values, list):
        raise TypeError('values must be a list')

    if not isinstance(weights, list):
        raise TypeError('weights must be a list')

    if len(values) != len(weights):
        raise ValueError('values and weights must have the same length')

    if values:

        expected_values_type = type(values[0])
        if not all(type(item) is expected_values_type for item in values):
            raise TypeError('all items in values must have the same type')

        expected_weights_type = type(weights[0])
        if not all(type(item) is expected_weights_type for item in weights):
            raise TypeError('all items in weights must have the same type')

        if not isinstance(values[0], (bool, int, float, Decimal)):
            raise TypeError(
                'values must contain only bool, int, float, Decimal types')

        if not isinstance(weights[0], (int, float, Decimal)):
            raise TypeError(
                'weights must contain only int, float, Decimal types')

        if not all((item>=0) for item in weights):
            raise ValueError('all items in weights must be non-negative')

        # Make a table of values and weights
        table = zip(values, weights)

        # Remove items with zero weights
        table = filter(lambda item: item[1], table)
        
        # Sort values and weights based on values
        table = sorted(table, key=lambda item: item[0])

        # Unzip the table back into values and weights
        values, weights = map(list, zip(*table))

    return values, weights


def weighted_median(values: list, weights: list):

    # Normalize and validate values and weights
    values, weights = validate_values_and_weights(values, weights)

    # If not values, return None
    if not values:
        return None
    
    count = len(values)

    # If only one value, return it
    if 1==count:
        return values[0]

    # Get values type
    value_is_bool = isinstance(values[0], bool)
    value_type = type(values[0])
    if value_is_bool:
        values = [int(v) for v in values]

    # Convert values and weights to Decimal for precision
    values = [Decimal(str(v)) for v in values]
    weights = [Decimal(str(w)) for w in weights]

    # Convert the weights into probabilities
    sum_weights = sum(weights)
    weights = [w / sum_weights for w in weights]
    
    # Select the median point
    cumulative_probability = Decimal('0')
    for idx in range(count):
        cumulative_probability += weights[idx]
        if cumulative_probability >= Decimal('0.5'):
            break

    if (count % 2) != 0:
        # If odd number of values, return the value
        # at the median index
        value = values[idx]
    else:
        # If even number of values, return the
        # weighted average of the two middle values
        base = weights[idx-1] + weights[idx]
        p, q = weights[idx-1]/base, weights[idx]/base
        value = (values[idx-1] * p) + (values[idx] * q)

    # Set the value type back to original type
    if value_is_bool:
        value = bool(value>Decimal('0.5'))
    else:
        value = value_type(value)

    return value


def median(*args):
    data = args[0] if len(args)==1 and isinstance(args[0], list) else args
    value = median_base(data)
    if all([(v is True or v is False) for v in data]):
        value = bool(value>0.5)
    return value


def mean(*args):
    data = args[0] if len(args)==1 and isinstance(args[0], list) else args
    value = mean_base(data)
    if all([(v is True or v is False) for v in data]):
        value = bool(value>0.5)
    return value
