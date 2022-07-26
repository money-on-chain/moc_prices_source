import datetime, json, sys
from sys             import stderr
from influxdb        import InfluxDBClient
from os.path         import dirname, abspath

bkpath   = sys.path[:]
base_dir = dirname(abspath(__file__))
sys.path.append(dirname(base_dir))

from moc_prices_source.conf import get

sys.path = bkpath


db_conf = None
envs    = {}


def call_back(options):

    selected_profile = options['selected_profile']

    return {
        'db_conf': options['profiles'][selected_profile]
    }

kargs = dict(
    out          = locals(),
    call_back    = call_back,
    files        = ['database.json', 'database_default.json'],
    env_pre      = 'MOC_PRICES_SOURCE',
    dir_         = '/data/',
    copy_to_home = False,
    places       = dirname(abspath(__file__)))

get(**kargs)




class Database(object):

    def __init__(self, **kargs):

        self.name = kargs['name']
        del kargs['name']

        self.client = InfluxDBClient(**kargs)

        if not self.name in [ d['name'] for d in self.client.get_list_database() ]:
              self.client.create_database(self.name)

        self.client.switch_database(self.name)


    @staticmethod
    def _validate_time(time_):
        if time_ is None:
            time_ = datetime.datetime.utcnow()
        return time_


    def write(self, measurement, fields, tags={}, time_ = None):

        time_ = self._validate_time(time_)

        item = {}

        item["measurement"] = measurement
        item["tag"]         = tags
        item["fields"]      = fields
        item["time"]        = time_.isoformat()

        body = []
        body.append(item)

        out = self.client.write_points(body, time_precision='s')

        return out


    @staticmethod
    def normalize_point_time(point):
        point['time'] = datetime.datetime.strptime(point['time'],
            '%Y-%m-%dT%H:%M:%SZ')


    @property
    def measurement_list(self):

        query = 'show measurements'

        results = self.client.query(query)
        points  = [ x['name'] for x in list(results.get_points()) ]

        return points


    def get_all(self, measurement, fields, tags={},
                group_by=None, aggregate_function="mean", fill= "linear"):

        if group_by:

            query = 'SELECT {fields} FROM "{measurement}" GROUP BY time({group_by}) fill({fill})'

            query = query.format(
                fill        = fill,
                group_by    = group_by,
                measurement = measurement,
                fields      = ', '.join([ '{}("{}") AS "{}"'.format(
                    aggregate_function, f, f) for f in fields ]))

        else:

            query = 'SELECT {fields} FROM "{measurement}"'

            query = query.format(measurement = measurement,
                fields  = ', '.join([ '"{}"'.format(f) for f in fields ]))

        results = self.client.query(query)
        points  = list(results.get_points(tags=tags))

        for point in points:
            self.normalize_point_time(point)

        return points


    def get_count(self, measurement):

        query = 'SELECT count(*) FROM "{measurement}"'

        query = query.format(measurement = measurement)

        results = self.client.query(query)
        points  = list(results.get_points())

        if not points:
            return 0

        return max([ x for x in points[0].values() if type(x)==int ])


    def get_last(self, measurement, field='*', tags={}):
        return self._get_last_or_first(True, measurement, field, tags=tags)


    def get_first(self, measurement, field='*', tags={}):
        return self._get_last_or_first(False, measurement, field, tags=tags)


    def _get_last_or_first(self, last, measurement, field='*', tags={}):

        if field in ['*', '', None, []]:
           field = None 

        if field:
            query = 'SELECT {field} FROM "{measurement}" ORDER BY {desc} LIMIT 1'
        else:
            query = 'SELECT * FROM "{measurement}" ORDER BY {desc} LIMIT 1'

        if type(field)==list:
            str_filed = ', '.join([ '"{}"'.format(f) for f in field ])
        else:
            str_filed = '"{}"'.format(field)

        query = query.format(measurement = measurement,
                             field       = str_filed,
                             desc        = 'DESC' if last else 'ASC')

        results = self.client.query(query)
        points  = list(results.get_points(tags=tags))

        if not points:
            if field and type(field)!=list:
                return None, None
            return None

        point = points[0]

        self.normalize_point_time(point)

        if not(field) or type(field)==list:
            return point

        value = point[field]
        time_ = point['time']

        return value, time_


    def exists(self, measurement, field, value, tags={}):

        query = 'SELECT "{field}" FROM "{measurement}" WHERE "{field}" = {value} ORDER BY DESC LIMIT 1'
        query = query.format(measurement = measurement,
                             field       = field,
                             value       = str(repr(value)).replace("'", '"'))

        results = self.client.query(query)
        points  = list(results.get_points(tags=tags))

        return bool(points)



database_error_message = None
try:
    database = Database(**db_conf)
except Exception as e:
    database_error_message = str(f"""
{str(e)}

Maybe you need to check environment variables or config file {repr(config_file)}
""")
    database = None


if __name__ == '__main__':

    print("File: {}, Ok!".format(repr(__file__)))
    print("Config file: {}, Ok!".format(repr(config_file)))
    if not database:
        print(database_error_message)
