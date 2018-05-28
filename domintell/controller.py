"""
:author: Thomas Delaet <thomas@delaet.org>

Port for Domintell
:author: Zilvinas Binisevicius <zilvinas@binis.me>
"""
import logging
import time
import json
import domintell
from domintell.utils import ModuleJSONEncoder
 
MODULE_CATEGORIES = {
    # todo: fix modules
    'switch': ['VMB4RYLD', 'VMB4RYNO'],
    'sensor': ['VMB6IN', 'VMB7IN']
}

class DomintellConnection(object):
    """
    Generic Domintell connection
    """

    controller = None

    def set_controller(self, controller):
        """
        :return: None
        """
        assert isinstance(controller, Controller)
        self.controller = controller

    def send(self, message, callback=None):
        """
        :return: None
        """
        raise NotImplementedError


class Controller(object):
    """
    Domintell Bus connection controller
    """

    def __init__(self, port):
        self.logger = logging.getLogger('domintell')
        self.parser = domintell.DomintellParser(self)
        self.__subscribers = []
        self.__scan_callback = None
        self._modules = {}
        if ":" in port:
            self.connection = domintell.UDPConnection(port, self)
        else:
            self.connection = domintell.RS232Connection(port, self)

    def feed_parser(self, data):
        """
        Feed parser with new data

        :return: None
        """
        assert isinstance(data, bytes)
        self.parser.feed(data)

    def subscribe(self, subscriber):
        """
        :return: None
        """
        self.__subscribers.append(subscriber)

    def parse(self, message):
        """
        :return: domintell.Message or None
        """
        return self.parser.parse(message)

    def unsubscribe(self, subscriber):
        """
        :return: None
        """
        self.__subscribers.remove(subscriber)

    def send(self, message, callback=None):
        """
        :return: None
        """
        self.connection.send(message, callback)

    def get_modules(self, category):
        """
        Returns a list of modules from a specific category

        :return: list
        """
        result = []
        for module in self._modules.values():
            if module.get_module_name() in MODULE_CATEGORIES[category]:
                result.append(module)
        return result

    def scan(self, callback=None):
        """
        Scan the bus discovered modules will com to reader thread
        :return: None
        """
        # def scan_finished():
        #     """
        #     Callback when scan is finished
        #     """
        #     time.sleep(3)
        #     logging.info('Scan finished')
        #     callback()
        
        message = domintell.AppInfoRequest()
        self.send(message)

    def login(self, password):
        message = domintell.LoginRequest(password)
        self.send(message)
         
    def new_message(self, message):
        """
        :return: None
        """
        self.logger.debug("New message: [" + str(message) + "]")
        if isinstance(message, domintell.ModuleInfoMessage):
            # do something with module data here
            self.logger.info("Domintell module info message received")
            module_type = message.moduleType
            serial_number = message.serialNumber
            # print(domintell.ModuleRegistry)
            self.add_module(module_type, serial_number)
        elif isinstance(message, domintell.ControllMessage):
            if message.moduleType == 'END APPINFO':
                # all APPINFO received
                logging.info("All APPINFO received")
                # TODO move to config
                with open('modules.js', 'w') as f:
                    m = self._modules
                    # move encoding into config , encoding='iso8859_13'
                    json.dump(m, f, cls=ModuleJSONEncoder)
        
        # forward message to listeners
        for subscriber in self.__subscribers:
            subscriber(message)

    def add_module(self, module_type, serial_number):
        """
        Create and add device
            :param self: 
            :param module_type: 
            :param serial_number: 
        """  
        if module_type in domintell.ModuleRegistry:
            # we support this module
            if serial_number in self._modules:
                # serial numbeer already registered
                pass
            else:
                module = domintell.ModuleRegistry[module_type](serial_number, self)
                self._modules[serial_number] = module
            return self._modules[serial_number]
        else:
            self.logger.warning("!! Module " + module_type + " is not yet supported. !!")
            return None
    
    def get_module(self, serial_number):
        """
        Get device by serial number
        """
        if serial_number in self._modules:
            return self._modules[serial_number]
        else:
            return None

    def stop(self):
        """
        Stop domintell
        """
        self.connection.stop()

    def start_ping(self, ping_interval):
        """
        Start ping service
            :param self: 
            :param ping_interval: 
        """
        self.connection.start_ping(ping_interval)
