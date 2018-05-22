"""
Dimmer control module DDIM01
Controlls up to 8 dimmers DD500, DD750, DD1000 and DD10V

:author: Zilvinas Binisevicius <zilvinas@binis.me>
"""
import domintell
import domintell.messages


class DDIM01Module(domintell.Module):
    """
    Dimmer control module DDIM01    
    """
    COMMAND_CODE = 'DIM'

    def __init__(self, serial_number, controller):
        domintell.Module.__init__(self, serial_number, controller)

    def is_on(self, channel):
        if channel < self.number_of_channels():
            if self._values[channel] > 0:
                return True
        return False
    
    def get_value(self, channel):
        if channel < self.number_of_channels():
            return self._values[channel]

    def set_value(self, channel, value):
        if channel < self.number_of_channels():
            message = domintell.SetAnalogOutputMessage(self.get_module_code(), self.get_serial_number(), channel, value)
            self._controller.send(message)

    def turn_on(self, channel):
        self.set_value(channel, 100)

    def turn_off(self, channel):
        self.set_value(channel, 0)
    
    def number_of_channels(self):
        return 8

    def _on_message(self, message):
        if isinstance(message, domintell.DDIMStatusMessage):
            # got DDIM status message (contains all channels)
            self._values = message.get_values()

            for ch in range(0, self.number_of_channels()):
                if ch in self._callbacks:
                    for callback in self._callbacks[ch]:
                        callback(self.get_value(ch))

domintell.register_module_class(DDIM01Module)
