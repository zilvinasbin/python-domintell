## python-domintell: A python library to control the Domintell home automation system

This library was created to support Domintell protocol in [home assisstant](http://home-assistant.io). It is based on [python-velbus](https://github.com/thomasdelaet/python-velbus) library by [Thomas Delaet](https://github.com/thomasdelaet).

It is currently being used by the Domintell component in [home assisstant](http://home-assistant.io) but can also be used indepenently.

The latest version of the library is *0.0.16* and it is published as a python package on [pypi](https://pypi.python.org/pypi/python-domintell)

API documentation is not yet available.

# Example usage

The library currently only supports a UDP communicatin via DETH02 Domintell module, it can be easily modified to support RS-232 intiarface (domintell light protocol). In order to use the library, you need to first initialize the controller and can then send and receive messages on the Domintell.

```python
import time
import logging
import sys
import domintell
import credentials
import os, sys

def _on_message(message):
    print('received message')
    print(message)

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

# UDP, Serial (or USB over serial) connection to Domintell controller
host = '192.168.0.1:17481'

controller = domintell.Controller(host) 
controller.subscribe(_on_message)

logging.info('LOGIN')
controller.login(credentials.host['SECRET'])

time.sleep(10)
logging.info('Starting scan')
controller.scan(None)

logging.info('Going to sleep')
time.sleep(100)
logging.info('Exiting ...')
controller.stop()

```

# Installation

You can install the library with pip (*pip install python-domintell*) or by checking out the [github](https://github.com/shamanenas/python-domintell) repository and running *python setup.py install* at the root of the repository.

# Supported modules

The following Domitell modules are currently supported by this library:

| Module name | Description | Status | Comments | Using everyday? |
| ----------- | ----------- | ------ | -------- | --------------- |
| DISM4 | Control of 4 inputs (buttons) | SUPPORTED | All messages are supported | Yes |
| DISM8 | Control of 8 inputs (buttons) | SUPPORTED | All messages are supported | Yes |
| DPBU01 | 1 button module | SUPPORTED | All messages are supported | No |
| DPBU02 | 2 button module | SUPPORTED | All messages are supported | No |
| DPBU04 | 4 button module | SUPPORTED | All messages are supported | Rarely |
| DPBU06 | 6 button module | SUPPORTED | All messages are supported | No |
| DBIR01 | 8 relay output module | SUPPORTED | All messages are supported | Yes |
| DTRP01 | Output card for the control of up to 4 trip switches | SUPPORTED | All messages are supported | Yes |
| DTRP02 | Output card for the control of 2 x 2 inverted trip switches |SUPPORTED | All messages are supported | No |
| DDIM01 | Control module for up to 8 dimmers | SUPPORTED | All messages are supported | Yes |
| DTEM01 | Temperature sensor module. Allows the connection of the temperature sensor | SUPPORTED | Only basic messages | Yes |
| DTEM02 | Temperature sensor module. Allows the connection of the temperature sensor | SUPPORTED | Only basic messages | Yes |
| DDIR01 | Infrared Sensor | NOT SUPPORTED | No plans to support | No |
| DTSC0x | TFT back-lit color touchscreen | SUPPORTED | Only temperature messages are supported | Yes |
| DMOV01 | Movement sensor | SUPPORTED | All messages are supported | Yes |
| DLCD01 | LCD | NOT SUPPORTED |  | No |
| DTRV01 | 4 outputs control module. For the control of shutters, valves, motors, etc | SUPPORTED | All messages are supported | No |
| DLED01 | 4 outputs led control module | SUPPORTED | All messages are supported | Yes |
| DTRVBT01 | Single output card controlling motors, valves, shutters or Velux with low tension between 12 to 24Vdc | SUPPORTED | All messages are supported | No |
| DAMPLI01 |  4 zones stereo audio amplifi er  | NOT SUPPORTED | No plans to implement | No |
| VAR | Variable | SUPPORTED | All messages are supported | No|
| SYS | System variable | SUPPORTED | All messages are supported | No |
| DOUT10V01 | 0 - 10Vdc output module | SUPPORTED | All messages are supported | No |
| DLCD01 | LCD panel | NOT SUPPORTED | | No |
| DFAN01 | Fan coil controller | NOT SUPPORTED | | No |
| DMR01 | Output card with 5 x 250 V/3 A monopolar relays. | SUPPORTED | All messages are supported | Yes |
| DIN10V01 | 0 - 10Vdc input module | NOT SUPPORTED || No |

# Adding support for other modules

The [Domintell website](http://www.domintell.com) contains an overview of the different available modules and their protocol documentation. In order to add support for an additional module, read through the protocol documemntation and add support for missing messages (many messages are shared between modules so make sure to check if a message already exists or not)

Steps to add support for an additional module:

- [ ] Look up the protocol documentation of the module you want to include at the [Domintell website](https://www.domintell.eu/).
- [ ] Go through the messages directory and look for messages in the protocol information sheet that are not yet supported. Create a new file in the *messages* folder for each unsupported message. Every new message should inherit from the *Message* object and reuse common functionality.
- [ ] Implement constructor method for each new message
- [ ] Implement the *populate* and *data_to_binary* methods for each new message
- [ ] Add new messages to the *__init__.py* file in the *messages* folder
- [ ] Test and iterate
- [ ] Update the Supported modules section of the *README.md* file
- [ ] Submit a pull request on Github

# Further development

The library currently offers only the lowest level of functionality: sending and receiving messages to modules:

- [ ] Modeling modules and their supported functions as entities
- [ ] Only allowing to send supported messages to modules
- [*] Auto-discovery of modules
- [ ] Exposing the velbus controller as an external API so it can be shared between different consumers