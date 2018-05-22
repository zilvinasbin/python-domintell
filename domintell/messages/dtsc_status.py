"""
DTSC0xodule status
Touch screen.

:author: Zilvinas Binisevicius <zilvinas@binis.me>
"""
import json
import domintell
from domintell.messages import GenericDIStatusMessage
from decimal import Decimal
from domintell.utils import DecimalEncoder

DTSC_COMMAND_CODE = "TSB"

class DTSCStatusMessage(GenericDIStatusMessage):
    """
    DISM4 module status
    """

    def __init__(self, address=None):
        GenericDIStatusMessage.__init__(self, 4)
        self.moduleType = DTSC_COMMAND_CODE
        self.current = None
        self.mode = None
        self.setPoint = None
        self.range = None

    def populate(self, serialNumber, dataType, dataString):
        """
        :return: None
        """
        # assert isinstance(dataString, str)
        self.serialNumber = serialNumber

        if dataType == "I":
            mask = int(dataString[0:2].strip(), 16)
            for input in range(0, self.inputCount):
                self.inputs[input] = 1 if (mask & (input + 1)) else 0
        elif dataType == "T":
            data = dataString.split()
            self.current = Decimal(data[0])
            self.setPoint = Decimal(data[1])
            self.mode = data[2]
            self.range = Decimal(data[3])

    def to_json(self):
        """
        :return: str
        """
        json_dict = self.to_json_basic()
        for input in range(0, self.inputCount):
            if input < len(self.inputs):
                json_dict['input{}'.format(input)] = self.inputs[input]
        
        json_dict['current'] = DecimalEncoder().encode(self.current)
        json_dict['mode'] = self.mode
        json_dict['setPoint'] = DecimalEncoder().encode(self.setPoint)
        json_dict['range'] = DecimalEncoder().encode(self.range)
        return json.dumps(json_dict)


domintell.register_command(DTSC_COMMAND_CODE, DTSCStatusMessage)
