"""
DI status (to be inherited)
:author: Zilvinas Binisevicius <zilvinas@binis.me>
"""
import json
import domintell

DI_COMMAND_CODE = "DI"

class GenericDIStatusMessage(domintell.Message):
    """
    Generic Digital input module status
    """

    def __init__(self, moduleType=None, inputCount=1, address=None):
        # assert isinstance(moduleType, str)
        # assert isinstance(inputCount, int) 
        domintell.Message.__init__(self, moduleType)
        self.moduleType = DI_COMMAND_CODE
        self.inputCount = inputCount
        self.serialNumber = None
        self.dataType = None
        self.inputs = {}
        for i in range(0, self.inputCount):
            self.inputs[i] = 0

    def populate(self, serialNumber, dataType, dataString):
        """
        :return: None
        """
        self.serialNumber = serialNumber
        self.dataType = dataType
        mask = int(dataString[0:2].strip(), 16)

        for input in range(0, self.inputCount):
            c = pow(2, input)
            self.inputs[input] = 1 if (mask & c) == c  else 0

    def to_json(self):
        """
        :return: str
        """
        json_dict = self.to_json_basic()
        for input in range(0, self.inputCount):
            if input < len(self.inputs):
                json_dict['input{}'.format(input)] = self.inputs[input]
        return json.dumps(json_dict)

    def get_values(self):
        return self.inputs
