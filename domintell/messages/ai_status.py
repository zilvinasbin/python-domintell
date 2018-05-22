"""
AO status (to be inherited)
:author: Zilvinas Binisevicius <zilvinas@binis.me>
"""
import json
import domintell

AI_COMMAND_CODE = "AI"

class GenericAIStatusMessage(domintell.Message):
    """
    Generic Analog output module status
    """

    def __init__(self, inputCount=1, address=None):
        domintell.Message.__init__(self)
        self.moduleType = AI_COMMAND_CODE
        self.inputCount = inputCount
        self.serialNumber = None
        self.dataType = None
        self.inputs = []
        for i in range(0, self.inputCount):
            self.inputs[i] = 0

    def populate(self, serialNumber, dataType, dataString):
        """
        :return: None
        """
        assert isinstance(dataString, str)

        self.serialNumber = serialNumber
        self.dataType = dataType

        for input in range(0, self.inputCount):
            self.inputs[input] = int(dataString[input * 2: 2].strip(), 16)

    def to_json(self):
        """
        :return: str
        """
        json_dict = self.to_json_basic()
        for input in range(0, self.inputCount):
            if input < len(self.inputs):
                json_dict['input{}'.format(input)] = self.inputs[input]
        return json.dumps(json_dict)
