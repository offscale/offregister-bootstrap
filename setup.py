# -*- coding: utf-8 -*-

"""
setup.py implementation, interesting because it parsed the first __init__.py and
    extracts the `__author__` and `__version__`
"""

from ast import Assign, Str, parse
from operator import attrgetter
from os import path
from os.path import extsep
from sys import version_info

from setuptools import find_packages, setup

if version_info[0] == 2:
    from itertools import ifilter as filter
    from itertools import imap as map

if version_info[:2] > (3, 7):
    from ast import Constant
else:
    from ast import expr

    # Constant. Will never be used in Python =< 3.8
    Constant = type("Constant", (expr,), {})


package_name = "offregister_bootstrap"

with open(
    path.join(path.dirname(__file__), "README{extsep}md".format(extsep=extsep)),
    "rt",
) as fh:
    long_description = fh.read()


def main():
    """Main function for setup.py; this actually does the installation"""
    with open(
        path.join(
            path.abspath(path.dirname(__file__)),
            package_name,
            "__init__{extsep}py".format(extsep=extsep),
        )
    ) as f:
        parsed_init = parse(f.read())

    __author__, __version__, __description__ = map(
        lambda node: node.value if isinstance(node, Constant) else node.s,
        filter(
            lambda node: isinstance(node, (Constant, Str)),
            map(
                attrgetter("value"),
                filter(lambda node: isinstance(node, Assign), parsed_init.body),
            ),
        ),
    )

    setup(
        name=package_name,
        author=__author__,
        author_email="807580+SamuelMarks@users.noreply.github.com",
        version=__version__,
        description=__description__,
        long_description=long_description,
        long_description_content_type="text/markdown",
        install_requires=["six", "jsonref"],
        test_suite="{}.tests".format(package_name),
        packages=find_packages(),
        package_dir={package_name: package_name},
        classifiers=[
            "Development Status :: 7 - Inactive",
            "Intended Audience :: Developers",
            "Topic :: Software Development",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication"
            "License :: OSI Approved :: MIT License",
            "License :: OSI Approved :: Apache Software License",
            "Programming Language :: Python",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.4",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
        ],
        url="https://github.com/offscale/{}".format(package_name),
    )


def setup_py_main():
    """Calls main if `__name__ == '__main__'`"""
    if __name__ == "__main__":
        main()


setup_py_main()
