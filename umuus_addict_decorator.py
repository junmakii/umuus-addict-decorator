#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A package.

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

"""
import sys
import re
import logging
import functools
import addict
__version__ = '0.1'
__url__ = 'https://github.com/junmakii/umuus-addict-decorator'
__author__ = 'Jun Makii'
__author_email__ = 'junmakii@gmail.com'
__keywords__ = []
__license__ = 'GPLv3'
__scripts__ = []
__install_requires__ = [
    'addict',
]
__dependency_links__ = [
]
__classifiers__ = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Natural Language :: English',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
]
__entry_points__ = {'console_scripts': ['umuus_addict_decorator = umuus_addict_decorator:main']}

logger = logging.getLogger(__name__)


def decorator(fn=None, *args, **kwargs):
    @functools.wraps(fn)
    def wrapper(*_args, **_kwargs):
        return addict.Dict(
            dict(list(kwargs.items())
                 + list(fn(*_args, **_kwargs).items())))
    return (
        fn
        and wrapper
        or functools.partial(decorator, *args, **kwargs))
