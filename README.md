
umuus-addict-decorator
======================

Installation
------------

    $ pip install umuus_addict_decorator

Example
-------

    $ umuus_addict_decorator

    >>> import umuus_addict_decorator

    >>> @umuus_addict_decorator.decorator(x=1)
    ... def get_data(): return {"a": {"b": {"c": 1}}}

    >>> get_data()
    {'x': 1, 'a': {'b': {'c': 1}}}

    >>> get_data().a.b.c
    1

Authors
-------

- Jun Makii <junmakii@gmail.com>

License
-------

GPLv3 <https://www.gnu.org/licenses/>