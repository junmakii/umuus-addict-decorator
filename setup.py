
from setuptools import setup, find_packages

setup(
    name='umuus_addict_decorator',
    description='A package.',
    long_description=('A package.\n'
 '\n'
 'umuus-addict-decorator\n'
 '======================\n'
 '\n'
 'Installation\n'
 '------------\n'
 '\n'
 '    $ pip install umuus_addict_decorator\n'
 '\n'
 'Example\n'
 '-------\n'
 '\n'
 '    $ umuus_addict_decorator\n'
 '\n'
 '    >>> import umuus_addict_decorator\n'
 '\n'
 '    >>> @umuus_addict_decorator.decorator(x=1)\n'
 '    ... def get_data(): return {"a": {"b": {"c": 1}}}\n'
 '\n'
 '    >>> get_data()\n'
 "    {'x': 1, 'a': {'b': {'c': 1}}}\n"
 '\n'
 '    >>> get_data().a.b.c\n'
 '    1\n'
 '\n'
 'Authors\n'
 '-------\n'
 '\n'
 '- Jun Makii <junmakii@gmail.com>\n'
 '\n'
 'License\n'
 '-------\n'
 '\n'
 'GPLv3 <https://www.gnu.org/licenses/>'),
    py_modules=['umuus_addict_decorator'],
    version='0.1',
    url='https://github.com/junmakii/umuus-addict-decorator',
    author='Jun Makii',
    author_email='junmakii@gmail.com',
    keywords=[],
    license='GPLv3',
    scripts=[],
    install_requires=['addict'],
    dependency_links=[],
    classifiers=['Development Status :: 3 - Alpha', 'Intended Audience :: Developers', 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)', 'Natural Language :: English', 'Programming Language :: Python', 'Programming Language :: Python :: 2.7', 'Programming Language :: Python :: 3'],
    entry_points={'console_scripts': ['umuus_addict_decorator = umuus_addict_decorator:main']}
)

