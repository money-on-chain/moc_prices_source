import datetime, numpy
from os.path      import dirname, abspath
from json         import load, dumps
from json.decoder import JSONDecodeError
from sys          import stderr
from statistics   import median, mean
from tabulate     import tabulate



filename = dirname(abspath(__file__)) + '/data/weighing.json'

def get_json_file(filename):

    def error(e):
        s = "Config file error\n{}\n{}"
        print(s.format(filename, e), file=stderr)
        exit(1)

    try:
        with open(filename) as json_file:
            data = load(json_file)
    except JSONDecodeError as e:
        error(e)
    except FileNotFoundError as e:
        error('File not found!')

    return data



class Weighing(object):

    def __init__(self, refresh_time=datetime.timedelta(minutes=60)):
        self._data = {}
        self._last_load = None
        self._refresh_time = refresh_time
        self._load()

    def _load(self):

        if ((self._last_load == None) or (
            (datetime.datetime.now() - self._last_load) > self._refresh_time)):

            data = get_json_file(filename)

            if isinstance(data, dict):
                ok = True
                try:
                    for key, value in data.items():
                        data[key] = float(value)
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
    def names(self):
        return list(self.as_dict.keys())

    def __call__(self, name):
        return  self.as_dict.get(name, 0.0)

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



def weighted_median(values, weights):
    ''' compute the weighted median of values list. The
weighted median is computed as follows:
    1- sort both lists (values and weights) based on values.
    2- select the 0.5 point from the weights and return the corresponding values as results
    e.g. values = [1, 3, 0] and weights=[0.1, 0.3, 0.6] assuming weights are probabilities.
    sorted values = [0, 1, 3] and corresponding sorted weights = [0.6,     0.1, 0.3] the 0.5 point on
    weight corresponds to the first item which is 0. so the weighted     median is 0.'''

    # convert the weights into probabilities
    sum_weights = sum(weights)
    weights = numpy.array([(w*1.0)/sum_weights for w in weights])
    # sort values and weights based on values
    values = numpy.array(values)
    sorted_indices = numpy.argsort(values)
    values_sorted  = values[sorted_indices]
    weights_sorted = weights[sorted_indices]
    # select the median point
    it = numpy.nditer(weights_sorted, flags=['f_index'])
    accumulative_probability = 0
    median_index = -1
    while not it.finished:
        accumulative_probability += it[0]
        if accumulative_probability > 0.5:
            median_index = it.index
            return values_sorted[median_index]
        elif accumulative_probability == 0.5:
            median_index = it.index
            it.iternext()
            next_median_index = it.index
            return numpy.mean(values_sorted[[median_index, next_median_index]])
        it.iternext()

    return values_sorted[median_index]



if __name__ == '__main__':
    print("File: {}, Ok!".format(repr(__file__)))
    print("Config file: {}".format(repr(filename)))
    print()
    print(weighing)
    print()