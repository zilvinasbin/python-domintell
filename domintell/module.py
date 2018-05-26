"""
:author: Thomas Delaet <thomas@delaet.org>

Port to domintell
:authot: Zilvinas Biniseviciud <zilvinas@binis.me>
"""
import string
import json
import domintell
from domintell.module_directory import MODULE_DIRECTORY

class Module(object):
    """
    Abstract class for Domintell hardware modules.
    """
    COMMAND_CODE = 'UNK'
    
    #pylint: disable-msg=R0902
    def __init__(self, serial_number, controller):
        """ C'tor
        Args:
            serial_number (str): module serial number
            controller (Controller): Controller
        """

        # module properties
        self._serial_number = serial_number

        # channel (point) properties
        self._chanel_ids = {}
        self._channel_names = {}
        self._channel_paths = {}
        self._values = {}
        for i in range(0, self.number_of_channels()):
            self._values[i] = 0

        self._callbacks = {}

        self._controller = controller
        self._controller.subscribe(self.on_message)
    
    def get_module_type(self):
        """
        Returns the module model type (full code)

        :return: str
        """
        if self._module_code() in MODULE_DIRECTORY.keys(): 
            return MODULE_DIRECTORY[self._module_code()]['type']
        return "UNK"
    
    def get_module_code(self):
        """
        Returns module model short code (3 letters)
        Is used in domintell protocol
        """
        return self._module_code()
    
    def get_serial_number(self):
        return self._serial_number

    def get_module_name(self):
        """
        Returns the module model type

        :return: str
        """
        if self._module_code() in MODULE_DIRECTORY.keys(): 
            return MODULE_DIRECTORY[self._module_code()]['name']
        return "Unknown"
    
    def get_point_id(self, channel):
        if channel < self.number_of_channels():
            return self._chanel_ids[channel]

    def get_name(self, channel):
        """
        Get name for one of the channels

        :return: str
        """
        if channel < self.number_of_channels():
            return self._channel_names[channel]

    def on_message(self, message):
        """
        Process received message
        """
        if isinstance(message, domintell.ModuleInfoMessage):
            # this is a info messages
            # process & store info
            self._on_info_message(message)
        else:
            # this is regular message
            self._on_message(message)

    def _on_message(self, message):
        pass

    def _on_info_message(self, message):
        if message.serialNumber == self.get_serial_number():
            ch = int(message.channel)
            if ch > 0 and ch <= self.number_of_channels():
                self._channel_names[ch] = message.name
                self._channel_paths[ch] = message.path
                self._chanel_ids[ch] = message.point_id

    def number_of_channels(self):
        """
        Retrieve the number of avaiable channels in this module

        :return: int
        """
        return 1
    
    def turn_on(self):
        raise NotImplementedError
    
    def turn_off(self):
        raise NotImplementedError
    
    def is_on(self, channel):
        raise NotImplementedError

    
    def get_status(self):
        message = domintell.ModuleStatusRequest(self.get_module_code(), self.get_serial_number())
        self._controller.send(message)
        
    def get_io_type(self):
        """
        Get Input Output type
        
        Returns:
         ai - analog input
         ao - analog output
         di - digital input
         do - digital output
         t  - temperature controller
         unk - unknown
        """
        if self._module_code() in MODULE_DIRECTORY.keys(): 
            return MODULE_DIRECTORY[self._module_code()]['io']
        return "unk"

    def is_dimmer(self):
        """
        Check if module is a dimmer
            :param self: 
        """   
        if self.get_io_type() == 'ao':
            return True
        return False
    
    def _load(self):
        message = domintell.ModuleStatusRequest(self.get_module_code(), self._serial_number)
        self._controller.send(message)


    @classmethod
    def _module_code(cls):
        return cls.COMMAND_CODE

    def on_status_update(self, channel, callback):
        """
        Callback to execute on status of update of channel
        """
        if not channel in self._callbacks:
            self._callbacks[channel] = [] 
        self._callbacks[channel].append(callback)

    def to_json_basic(self):
        """
        Create JSON structure with generic attributes
        :return: dict
        """
        return {'name': self.__class__.__name__, 
                'module_type': self.get_module_type(), 
                'module_name':self.get_module_name(),
                'module_code': self.get_module_code(), 
                'serial_number': self._serial_number,
                'channel_ids': (self._chanel_ids), 
                'channel_names': (self._channel_names), 
                'channel_paths': (self._channel_paths) }

    def to_json(self):
        # print(self.to_json_basic)
        return json.dumps(self.to_json_basic()) 



# json_dict = self.to_json_basic()
#         for input in range(0, self.inputCount):
#             if input < len(self.inputs):
#                 json_dict['input{}'.format(input)] = self.inputs[input]
#         return json.dumps(json_dict)
