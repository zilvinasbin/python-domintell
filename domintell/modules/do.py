"""
DBIR01 - 8th bipolar relays controll module 
DTRP01 - 4th trip switched controll module

:author: Zilvinas Binisevicius <zilvinas@binis.me>
"""
import domintell
import domintell.messages

class DBIR01Module(domintell.Module):
    """
    DBIR - relays controll module (8 channels)    
    """
    COMMAND_CODE = 'BIR'

    def __init__(self, serial_number, controller):
        domintell.Module.__init__(self, serial_number, controller)

    def is_on(self, channel):
        if channel < self.number_of_channels():
            if self._values[channel] > 0:
                return True
        return False
    
    def get_value(self, channel):
        if channel < self.number_of_channels():
            return self._values[channel] > 0

    def set_value(self, channel, value):
        if channel < self.number_of_channels():
            message = domintell.SetDigitalOutputMessage(self.get_module_code(), self.get_serial_number(), channel, value)
            self._controller.send(message)

    def togle(self, channel):
        if channel < self.number_of_channels():
            message = domintell.TogleDigitalOutputMessage(self.get_module_code(), self.get_serial_number, channel)
            self._controller.send(message)

    def turn_on(self, channel):
        if channel < self.number_of_channels():
            message = domintell.SetDigitalOutputOnMessage(self.get_module_code(), self.get_serial_number(), channel)
            self._controller.send(message)
 
    def turn_off(self, channel):
        if channel < self.number_of_channels():
            message = domintell.SetDigitalOutputOffMessage(self.get_module_code(), self.get_serial_number(), channel)
            self._controller.send(message)

    def number_of_channels(self):
        return 8

    def _on_message(self, message):
        if isinstance(message, domintell.DBIRStatusMessage):
            self._values = message.get_values()

            for ch in range(0, self.number_of_channels()):
                if ch in self._callbacks:
                    for callback in self._callbacks[ch]:
                        callback(self.get_value(ch))

class DTRP01Module(DBIR01Module):
    """
    Controll up to 4 trip switches
    """
    COMMAND_CODE = 'TRP'
    
    def number_of_channels(self):
        return 4

    def _on_message(self, message):
        if isinstance(message, domintell.DTRPStatusMessage):
            self._values = message.get_values()

            for ch in range(0, self.number_of_channels()):
                if ch in self._callbacks:
                    for callback in self._callbacks[ch]:
                        callback(self.get_value(ch))

class DTRP02Module(DBIR01Module):
    """
    Controll up to 4 trip switches
    2 x 2shutter command with teleruptors
    Bit 0 Relay 1 = UP
    Bit 1 Relay 1 = DOWN ...
    """
    COMMAND_CODE = 'TPV'
    
    def number_of_channels(self):
        return 4

class DTRV01Module(DBIR01Module):
    """
    DTRV01 Module
    4 shutter inverters
    Bit 0 Relay 1 = UP
    Bit 1 Relay 1 = DOWN ...
    """
    COMMAND_CODE = 'TRV'
    
    def number_of_channels(self):
        return 4
    
    def _on_message(self, message):
        if isinstance(message, domintell.DTRVStatusMessage):
            self._values = message.get_values()

            for ch in range(0, self.number_of_channels()):
                if ch in self._callbacks:
                    for callback in self._callbacks[ch]:
                        callback(self.get_value(ch))        

class DTRVBT01Module(DBIR01Module):
    """
    1 DC shutter command
        0 = UP
        1 = DOWN    
    """
    COMMAND_CODE = 'V24'

    def number_of_channels(self):
        return 1

    def _on_message(self, message):
        if isinstance(message, domintell.DTRVBTStatusMessage):
            self._values = message.get_values()

            for ch in range(0, self.number_of_channels()):
                if ch in self._callbacks:
                    for callback in self._callbacks[ch]:
                        callback(self.get_value(ch))

class DFAN01Module(DBIR01Module):
    """
    Fan controller
    """
    # TODO I have no DFAN01 module, need to implement it normally
    COMMAND_CODE = 'FAN'

    def number_of_channels(self):
        return 5

class DMR01Module(DBIR01Module):
    """
    5 monopolar relays control module
    """
    COMMAND_CODE = 'DMR'

    def number_of_channels(self):
        return 5

    def _on_message(self, message):
        if isinstance(message, domintell.DDMRStatusMessage):
            self._values = message.get_values()

            for ch in range(0, self.number_of_channels()):
                if ch in self._callbacks:
                    for callback in self._callbacks[ch]:
                        callback(self.get_value(ch))


class DLED01Module(DBIR01Module):
    """
    4 LED's driver
    """
    COMMAND_CODE = 'LED'

    def number_of_channels(self):
        return 4

    def _on_message(self, message):
        if isinstance(message, domintell.DLEDStatusMessage):
            self._values = message.get_values()
            for ch in range(0, self.number_of_channels()):
                if ch in self._callbacks:
                    for callback in self._callbacks[ch]:
                        callback(self.get_value(ch))


domintell.register_module_class(DBIR01Module)
domintell.register_module_class(DTRP01Module)
domintell.register_module_class(DTRP02Module)
domintell.register_module_class(DTRV01Module)
domintell.register_module_class(DTRVBT01Module)
domintell.register_module_class(DMR01Module)
domintell.register_module_class(DLED01Module)
