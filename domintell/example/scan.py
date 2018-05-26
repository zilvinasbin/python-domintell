#!/usr/bin/python3
"""
Example code to scan Domintell and return list of installed modules.
"""

import time
import logging
import sys
import domintell
import os, sys
from config import host

def _on_message(message):
    print('received message', message)
    print(message)

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
"""
please create a simple credentials.py:

host = {
    'ADDRESS': '192.168.0.1:17481',
    'SECRET': '<your password hash>'
}

"""

#pylint: disable-msg=C0103
logging.info('Configuring controller for {}'.format(host['ADDRESS']))

controller = domintell.Controller(host['ADDRESS']) 
controller.subscribe(_on_message)

logging.info('LOGIN')
controller.login(host['SECRET'])

time.sleep(10)
logging.info('Starting scan')

controller.scan(None)

logging.info('Starting sleep')
time.sleep(1000)
logging.info('Exiting ...')
controller.stop()
