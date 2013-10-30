Insteonic
=========

A Python command line interface for Insteon devices

Installation
------------

Install with PIP::

    pip install -e git+git@github.com:ryanbagwell/insteonic.git#egg=insteonic



Configuration
-------------

In your home directory, create a directory called .insteonic, and create a config.ini file inside it. Then set up your devices. Example::

	[controller]
	host: 192.168.1.12
	devices: hvac,irrigation,porchlight

	[hvac]
	id: 1F.16.D4
	type: ClimateControlDevice

	[porchlight]
	id: 20.9A.33
	type: SwitchedLightingControlDevice


Usage
-----

After configurating your devices, you're ready to send come commands. From the command line, type the following::

	insteonic

List available commands for a particular device::

 	insteonic porchlight (or other device name)


Send a command::

  insteonic hvac cool

  irrigation on


Extend
------

Create custom device classes by creating a file called ``local_devices.py`` that lives in ``~/.insteonic/``. Then specify your custom device class in your config.ini file.