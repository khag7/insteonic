Insteonic
=========

A Python command line interface for Insteon devices

Installation
------------

Install with PIP::

    pip install -e git+git@github.com:ryanbagwell/insteonic.git#egg=insteonic

In your home directory, create a directory called .insteonic, and create a config.ini file inside it.

Use the default config.ini file that ships with the package to finish your setup.

Usage
-----

From the command line, type the following::

  insteonic

Additional examples::

  insteonic hvac cool

  irrigation on


Extend
------

Create custom device classes by creating a file called ``local_devices.py`` that lives in ``~/.insteonic/``. Then specify your custom device class in your config.ini file.