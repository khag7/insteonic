#!/usr/bin/env python
from setuptools import setup

setup(
    name = "insteonic",
    version = "0.1",
    author = "Ryan Bagwell",
    author_email = "ryan@ryanbagwell.com",
    description = ("A Python command-line interface for Insteon's smartlinc controller"),
    license = "BSD",
    keywords = "Insteon automation",
    url = "http://packages.python.org/an_example_pypi_project",
    packages=['insteon',],
    install_requires = [
        'beautifulsoup4==4.2.1',
        'requests==1.2.3',
    ],
    scripts=['bin/insteon', ],
)