"""
:author: Thomas Delaet <thomas@delaet.org>

Port to Domintell
:author: Zilvinas Binisevicius <zilvinas@binis.me>
"""
import os

MINIMUM_MESSAGE_SIZE = 10
MAXIMUM_MESSAGE_SIZE = MINIMUM_MESSAGE_SIZE + 100

# pylint: disable-msg=C0103
CommandRegistry = {}

ModuleRegistry = {}

def on_app_engine():
    """
    :return: bool
    """
    if 'SERVER_SOFTWARE' in os.environ:
        server_software = os.environ['SERVER_SOFTWARE']
        if server_software.startswith('Google App Engine') or \
                server_software.startswith('Development'):
            return True
        return False
    return False


def register_command(command_name, command_class):
    """
    :return: None
    """
    assert isinstance(command_name, str)
    assert isinstance(command_class, type)
    if command_name not in CommandRegistry:
        CommandRegistry[command_name] = command_class
    else:
        raise Exception('double registration in command registry {}:{}'.format(command_name, command_class))

def register_module(module_name, module_class):
    """
    :return: None
    """
    assert isinstance(module_name, str)
    assert isinstance(module_class, type)
    if module_name not in ModuleRegistry:
        ModuleRegistry[module_name] = module_class
    else:
        raise Exception("Double registration in module registry {}:{}".format(module_name, module_class))

def register_module_class(module_class):
    register_module(module_class._module_code(), module_class)

# pylint: disable-msg=W0401,C0413
from domintell.message import Message
from domintell.command import Command
from domintell.messages import *

from domintell.module import Module
from domintell.modules import *

from domintell.parser import DomintellParser, ParserError
from domintell.controller import Controller, DomintellConnection

if not on_app_engine():
    try:
        from domintell.connections import UDPConnection, RS232Connection
    except ImportError:
        pass
