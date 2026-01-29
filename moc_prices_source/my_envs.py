from tabulate import tabulate
from os import environ
from typing import Dict, List, Any
from .types import Bool
from dotenv import load_dotenv
from shutil import get_terminal_size
from os.path import basename
from sys import argv, stderr, exit



class Envs():

    def __init__(self,
                 envfile_var_name: str = None,
                 envfile_var_description: str = 'Environment file overwrite',
                 envfile_default: str = '.env',
                 envfile_hide = False,
                 load_envfile_on_init = False,
                 load_envfile_on_first_get = True,
                 load_env_file_on_any_get = False):
        self._envfile_var_name = envfile_var_name
        self._envfile_var_description = envfile_var_description
        self._envfile_default = envfile_default
        self._envfile_hide = envfile_hide
        self._list: List[Dict] = []
        if load_envfile_on_init:
            self._load_dotenv()
        self._load_envfile_on_first_get = load_envfile_on_first_get
        self._load_env_file_on_any_get = load_env_file_on_any_get
    
    def load_dotenv(self,
                     var_name: str = None,
                     var_description: str = 'Environment file overwrite',
                     default_file: str = '.env',
                     hide = False
                     ) -> None:
        
        if var_name is None:
            var_name = basename(argv[0])
            if var_name.endswith('.py'):
                var_name = var_name[:-3]
            var_name = f"{var_name}_env_file"
        
        envfile = self(var_name, default_file, str,
                       descripion = var_description,
                       hide = hide,
                       use_load_dotenv = False)
        
        load_dotenv(envfile)

    def _load_dotenv(self) -> None:
        self.load_dotenv(
            var_name = self._envfile_var_name,
            var_description = self._envfile_var_description,
            default_file = self._envfile_default,
            hide = self._envfile_hide
        )

    @staticmethod
    def _normalize_name(name:str) -> str:
        name = '_'.join(str(name).strip().upper().split()) if name else None
        if name is None:
            raise ValueError("Environment variable name cannot be empty")
        return name

    @staticmethod
    def _bool_from_string(value: str) -> bool:
        return bool(Bool.from_string(value))
    
    def __call__(self,
            name: str,
            default: Any = None,
            cast: callable = None,
            alias: dict = {},
            on_error_exit: bool = True,
            descripion = None,
            use_load_dotenv = None,
            hide = False
        ) -> Any:

        # Load envfile
        if use_load_dotenv is not False: # avoid max recursion depth exceeded
            if use_load_dotenv or self._load_env_file_on_any_get or (
                               not(self) and self._load_envfile_on_first_get):
                self._load_dotenv()

        # Normalize name
        name = self._normalize_name(name)

        # Normalize alias
        if alias:
            alias = dict(
                [(str(k).strip().lower(),
                str(v).strip()) for (k, v) in alias.items()])
            new_alias = {}
            for (key, alias_value) in alias.items():
                available_keys = [k for k in alias.keys() if k!=key ]
                while alias_value in available_keys:
                    available_keys.remove(alias_value)
                    alias_value = alias[alias_value]
                new_alias[key] = alias_value
            alias = new_alias

        # Try to obtain previously recorded data
        if self:
            prev_data = envs[name]
            if len(prev_data)==1:
                prev_data = prev_data[0]
                prev_cast = prev_data['cast']
                prev_default = prev_data['default']
                prev_alias = prev_data['alias']
                prev_descripion = prev_data['descripion']
                if cast is None:
                    cast = prev_cast
                if default is None:
                    default = prev_default
                if alias=={}:
                    alias = prev_alias
                if descripion is None:
                    descripion = prev_descripion                    

        # Normalize cast
        if cast is None:
            cast = str
        elif cast is bool:
            cast = self._bool_from_string

        # Get value from environment
        try:
            value = environ[name]
        except KeyError:
            value = default

        # Apply aliasing
        if alias:
            alias_key = str(value).strip().lower()
            if alias_key in alias:
                value = alias[alias_key]

        # Options
        options = set([str(default)]) if default is not None else set()
        for key, option_value in alias.items():
            options.add(key)
            options.add(option_value)
        options = list(options)
        options.sort()

        # Cast value
        if value!=default:
            try:
                value = cast(str(value))
            except Exception as e:
                if on_error_exit: # Show errors
                    msg = ["ERROR: invalid value for env var "
                           f"{name}: {value!r}\n"]
                    if len(options)==1:
                        msg.append(f"       expected valid {cast.__name__}\n"
                                   f" or {repr(options[0])}")
                    msg.append(f"       expected valid {cast.__name__}\n")
                    if len(options)>1:
                        msg.append(f"       some valid options:\n")
                        width = get_terminal_size().columns - 7
                        col_width = max(len(s) for s in options) + 2
                        cols = max(1, width // col_width)
                        for i, s in enumerate(options):
                            msg.append(s.ljust(col_width))
                            if (i + 1) % cols == 0:
                                msg.append("\n       ")
                    print(''.join().strip(), file=stderr)
                    exit(1)
                else:
                    value = default

        # (De)normalize cast
        if cast==self._bool_from_string:
            cast = bool
        
        # Registry
        if not hide:
            registry = {
                'name': name,
                'cast': cast,
                'value': value,
                'default': default,
                'options': options,
                'descripion': descripion,
                'alias': alias}
            if not registry in self._list:
                self._list.append(registry)
                self._list.sort(key=lambda d: d["name"])
        
        # Return value
        return value
    
    def __iter__(self):
        return iter(self._list)

    def __len__(self):
        return len(self._list)

    def __bool__(self):
        return len(self._list)>0

    def __getitem__(self, i):
        if isinstance(i, str):
            name = self._normalize_name(i)
            return list(filter(lambda x: x['name']==name, self._list))
        return self._list[i]
    
    def __str__(self):
        if not self:
            return ''
        fields = ['name','value', 'default', 'cast', 'descripion']
        titles = {'cast': 'Type'}
        headers = [titles.get(f, str(f).capitalize()) for f in fields]
        def format(obj):
            if obj is None:
                return ''
            if obj is int:
                return 'Integer'
            if obj is float:
                return 'Float'
            if obj is str:
                return 'String'
            if obj is bool:
                return 'Bool'
            if obj==self._bool_from_string:
                return 'Bool'
            if callable(obj):
                return ' '.join(map(lambda w: w.capitalize(), str(obj.__name__
                    ).replace('_', ' ').split()))
            if isinstance(obj, list):
                return ', '.join([str(x) for x in obj])
            return str(obj)
        table = [[format(r[f]) for f in fields] for r in self]
        return f"\n{tabulate(table, headers=headers, tablefmt='simple')}\n"

    def _data_of(self, name, key) -> Any:
        data = envs[name]
        if len(data)>1:
            raise KeyError('more than one env with that name')
        if len(data)<1:
            raise KeyError('no env with that name')
        data = data[0]
        return data[key]

    def cast_of(self, name) -> Any:
        return self._data_of(name, 'cast')
    
    def value_of(self, name) -> Any:
        return self._data_of(name, 'value')
    
    def default_of(self, name) -> Any:
        return self._data_of(name, 'default')
    
    def options_of(self, name) -> List:
        return self._data_of(name, 'options')
    
    def descripion_of(self, name) -> str:
        return self._data_of(name, 'descripion')
    
    def alias_of(self, name) -> Dict:
        return self._data_of(name, 'alias')

    @property
    def names(self) -> List:
        names = list(set([x['name'] for x in list(self)]))
        names.sort()
        return names


envs = Envs()
