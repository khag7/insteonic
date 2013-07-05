import requests
from commands import *
import ConfigParser
import sys
import os
import socket
import binascii

class Device(object):
    device_id = None
    host = '0.0.0.0'
    config = None
    commands = {}
    description = 'No descrption available.'
                
    def __init__(self, host=None, device_id=''):
        self.host = host
        self.device_id = device_id.replace('.', '')
            
    def send_command(self, cmd=None, **kwargs):
        cmd_obj = self.commands[cmd](**kwargs)

        cmd_str = cmd_obj.get_raw_command_string(self.device_id)
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.host, 9761))
        s.send(cmd_str)        
        response_str = s.recv(24)
        
        cmd_obj.handle_response(response_str)
        cmd_obj.handle_response(response_str)


    def _set_host(self):
        
        if host is not None:
            self.host = host
    
    def _get_config(self):
        
        config = ConfigParser.ConfigParser()
        
        try:
            config.read(os.path.expanduser('~/.insteon/config.ini'))
        except:
            config.read('config/config.default.ini')
            
        return config
        
class DimmableLightingControlDevice(Device):
    """ A geneic class that contains commands
        for dimmable lighting control devices. """
    pass


class SwitchedLightingControlDevice(Device):
    """ A geneic class that contains commands
        for switched lighting control devices.
        
        Includes relay devices, such as switchlinc """
        
    commands = {
        'on': On,
        'off': Off,
    }
    
    def on(self):
        self.send_command('on')
        
    def off(self):
        self.send_command('off')


class IrrigationControlDevice(Device):
        pass


class ClimateControlDevice(Device):
    """ A generic class that contains commands 
        for climate control devices """
   
    commands = {
        'off': ThermostatSetOff,
        'cool': ThermostatSetCool,
        'heat': ThermostatSetHeat,
        'auto': ThermostatSetAuto, 
        'fan_on': ThermostatFanOn,
        'fan_auto': ThermostatFanAuto,
        'set_cool_point': ThermostatSetCoolPoint,
        'set_heat_point': ThermostatSetHeatPoint,
        'set_program_cool': ThermostatSetProgramCool
    }
    
    def off(self):
        self.send_command('off')
        
    def cool(self):
        self.send_command('cool')

    def heat(self):
        self.send_command('heat')
        
    def auto(self):
        self.send_command('auto')
        
    def fan_on(self):
        self.send_command('fan_on')
        
    def fan_auto(self):
        self.send_command('fan_auto')
        
    def set_cool_point(self, temperature):
        self.send_command('set_cool_point', temperature=temperature)
        
    def set_program_cool(self):
        self.send_command('set_program_cool')

try:
    sys.path.append(os.path.expanduser('~/.insteonic/'))
    from local_devices import *
except:
    pass