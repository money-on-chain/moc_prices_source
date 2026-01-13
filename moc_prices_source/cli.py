import click, shutil, sys
from tabulate import tabulate
from os import environ



cli = click
option = click.option
argument = click.argument
BadParameter = click.BadParameter
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


def command_group(command_group_=None, name=None, **kargs):
    f = command_group_.group if command_group_ else cli.group
    kargs['context_settings'] = CONTEXT_SETTINGS
    kargs['name'] = name
    return f(**kargs)


def command(command_=None, name=None, **kargs):
    f = command_.command if command_ else cli.command
    kargs['context_settings'] = CONTEXT_SETTINGS
    kargs['name'] = name
    return f(**kargs)


def trim(s, len_=30, end=' [...]'):
    assert len(end)<=len_
    out = str(s)
    if len(out)>len_:
        out = out[:(len_-len(end))] + end
    return out 


def print_list(items):
    if not items:
        return
    
    items = list(map(str, items))
    items.sort()
    
    width = shutil.get_terminal_size().columns
    col_width = max(len(s) for s in items) + 2
    cols = max(1, width // col_width)

    for i, s in enumerate(items):
        print(s.ljust(col_width), end="")
        if (i + 1) % cols == 0:
            print()
    print()


def get_env(name, default, cast=str, alias={}):
    alias = dict(
        [(str(k).strip().lower(),
          str(v).strip()) for (k, v) in alias.items()])
    try:
        value = environ[name]
    except KeyError:
        value = default
    while str(value).strip().lower() in alias:
        value = alias[str(value).strip().lower()]
    try:
        return cast(str(value))
    except Exception as e:
        options = list(alias.keys())
        options.sort()
        if options:
            options_str = ' or this options: ' + ', '.join(map(repr, options))
        else:
            options_str = ''

        print(
            f"ERROR: invalid value for env var {name}: {value!r} "
            f"(expected valid {cast.__name__}{options_str})",
            file=sys.stderr
        )
        sys.exit(1)