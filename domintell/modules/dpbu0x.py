"""
Dimmer control module DDIM01
Controlls up to 8 dimmers DD500, DD750, DD1000 and DD10V

:author: Zilvinas Binisevicius <zilvinas@binis.me>
"""
import domintell
import domintell.messages

class GenericDPBU0xModule(domintell.Module):
    """
    Abstract DPBU control module     
    """
    COMMAND_CODE = 'UNK'

    def __init__(self, serial_number, controller):
        domintell.Module.__init__(self, serial_number, controller)
        self._leds = {}
        for i in range(0, self.number_of_channels()):
            self._leds[i] = 0


    def is_on(self, channel):
        if channel < self.number_of_channels():
            if self._values[channel] > 0:
                return True
        return False

    def is_led_on(self, channel):
        if channel < self.number_of_channels():
            if self._leds[channel] > 0:
                return True
        return False
        
    def sim_long_push(self, channel):
        """
        Simulate long push
        """
        # TODO
        pass

    def sim_long_push_end(self, channel):
        """ 
        Simulate end of long push
        """
        # TODO
        pass

    def sim_short_push(self, channel):
        """
        Simulate short push
        """
        # TODO
        pass

    def sim_short_push_end(self, channel):
        """ 
        Simulate end of short push
        """
        # TODO
        pass

    def number_of_channels(self):
        raise NotImplementedError

    def _on_message(self, message):
        if isinstance(message, domintell.DDIMStatusMessage):
            
            if message.is_input():
                self._values = message.get_inputs()

            if message.is_output():
                self._leds = message.get_outputs()

            for ch in range(0, self.number_of_channels()):
                if ch in self._callbacks:
                    for callback in self._callbacks[ch]:
                        callback(self._values[ch], self._leds[ch])

class DPBU01Module(GenericDPBU0xModule):

    COMMAND_CODE = 'BU1'

    def number_of_channels(self):
        return 1

    def _on_message(self, message):
        if isinstance(message, domintell.DPBU01StatusMessage):
            
            if message.is_input():
                self._values = message.get_inputs()

            if message.is_output():
                self._leds = message.get_outputs()

            for ch in range(0, self.number_of_channels()):
                if ch in self._callbacks:
                    for callback in self._callbacks[ch]:
                        callback(self._values[ch], self._leds[ch])

class DPBU02Module(GenericDPBU0xModule):

    COMMAND_CODE = 'BU2'

    def number_of_channels(self):
        return 2

    def _on_message(self, message):
        if isinstance(message, domintell.DPBU02StatusMessage):
            
            if message.is_input():
                self._values = message.get_inputs()

            if message.is_output():
                self._leds = message.get_outputs()

            for ch in range(0, self.number_of_channels()):
                if ch in self._callbacks:
                    for callback in self._callbacks[ch]:
                        callback(self._values[ch], self._leds[ch])

class DPBU04Module(GenericDPBU0xModule):

    COMMAND_CODE = 'BU4'

    def number_of_channels(self):
        return 4

    def _on_message(self, message):
        if isinstance(message, domintell.DPBU04StatusMessage):
            
            if message.is_input():
                self._values = message.get_inputs()

            if message.is_output():
                self._leds = message.get_outputs()

            for ch in range(0, self.number_of_channels()):
                if ch in self._callbacks:
                    for callback in self._callbacks[ch]:
                        callback(self._values[ch], self._leds[ch])

class DPBU06Module(GenericDPBU0xModule):

    COMMAND_CODE = 'BU6'

    def number_of_channels(self):
        return 6

    def _on_message(self, message):
        if isinstance(message, domintell.DPBU06StatusMessage):
            
            if message.is_input():
                self._values = message.get_inputs()

            if message.is_output():
                self._leds = message.get_outputs()

            for ch in range(0, self.number_of_channels()):
                if ch in self._callbacks:
                    for callback in self._callbacks[ch]:
                        callback(self._values[ch], self._leds[ch])


domintell.register_module_class(DPBU01Module)
domintell.register_module_class(DPBU02Module)
domintell.register_module_class(DPBU04Module)
domintell.register_module_class(DPBU06Module)
