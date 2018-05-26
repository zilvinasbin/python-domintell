"""
Temperature status
:author: Zilvinas Binisevicius <zilvinas@binis.me>
"""
import json
import domintell
from domintell.utils import DecimalEncoder

TEM_COMMAND_CODE = "TEM"
TE1_COMMAND_CODE = "TE1"
TE2_COMMAND_CODE = "TE2"

class GenericTemperaturetatusMessage(domintell.Message):
    """
    Generic Temperature input module status
    """

    def __init__(self, address=None):
        domintell.Message.__init__(self)
        self.moduleType = TEM_COMMAND_CODE
        self.serialNumber = None
        self.dataType = None
        self._current = None
        self._mode = None
        self._set_point = None
        self._range = None

    def get_temperature(self):
        return self._current
    
    def get_mode(self):
        return self._mode

    def get_set_point(self):
        return self._set_point
    
    def get_range(self):
        return self._range

    def populate(self, serialNumber, dataType, dataString):
        """
        :return: None
        """
        # assert isinstance(dataString, str)

        self.serialNumber = serialNumber
        self.dataType = dataType

        data = dataString.split()

        self._current = float(data[0])
        self._set_point = float(data[1])
        self._mode = data[2]
        self._range = float(data[3])

    def to_json(self):
        """
        :return: str
        """
        # FIXME
        json_dict = self.to_json_basic()
        json_dict['current'] = self._current
        json_dict['mode'] = self._mode
        json_dict['set_point'] = self._set_point
        json_dict['range'] = self._range
        return json.dumps(json_dict)


class TE1TemperaturetatusMessage(GenericTemperaturetatusMessage):
    def __init__(self, address=None):
        GenericTemperaturetatusMessage.__init__(self)
        self.moduleType = TE1_COMMAND_CODE

class TE2TemperaturetatusMessage(GenericTemperaturetatusMessage):
    def __init__(self, address=None):
        GenericTemperaturetatusMessage.__init__(self)
        self.moduleType = TE2_COMMAND_CODE


domintell.register_command(TE1_COMMAND_CODE, TE1TemperaturetatusMessage)
domintell.register_command(TE2_COMMAND_CODE, TE2TemperaturetatusMessage)
