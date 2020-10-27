import threading, sys
from os       import listdir, path
from os.path  import isfile, dirname, abspath

bkpath   = sys.path[:]
base_dir = dirname(abspath(__file__))


all_engines   = {}
exclude       = ['base.py']
mypath        = dirname(__file__)
files         = [f for f in listdir(mypath) if isfile(path.join(mypath, f))]
files         = [f for f in files if f not in exclude]
modules_names = [ n[:-3] for n in files if n[-3:] =='.py' and n[:1]!='_']

del listdir, path, isfile, dirname, mypath, files, exclude

for name in modules_names:
    sys.path.append(base_dir)
    locals()[name] = __import__(name, globals(), locals()).Engine()
    sys.path = bkpath
    all_engines[name] = locals()[name]

del name, modules_names



def get_coinpair_list():
    engines_list = all_engines.values()
    coinpair_list = [ engine.coinpair for engine in engines_list ]
    coinpair_list = list(set(coinpair_list))
    coinpair_list.sort()
    return coinpair_list



def get_engines_names():
    engines_list = all_engines.values()
    engines_names = [ engine.name for engine in engines_list ]
    engines_names.sort()
    return engines_names



def get_prices(coinpairs=None, engines_names=None, engines_list=[]):

    assert isinstance(engines_list, (list, str))
    if not engines_list:
        engines_list = all_engines.values()

    if engines_names:
        assert isinstance(engines_names, (list, str))
        engines_list = [ e for e in engines_list if (
            e.name in engines_names or e.description in engines_names) ]

    if coinpairs:
        assert isinstance(coinpairs, (list, str))
        engines_list = [ e for e in engines_list if (
            e.coinpair in coinpairs) ]

    if not engines_list:
        return []

    threads = []
    for engine in engines_list:
        thread = threading.Thread(target=engine)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return [ engine.as_dict for engine in engines_list ]



if __name__ == '__main__':
    print("File: {}, Ok!".format(repr(__file__)))
    for data in get_prices():
        print()
        print('{}:'.format(data['name']))
        print()
        for key, value in data.items():
            if key!='name':
                print('    {} = {}'.format(key, value))
    print()