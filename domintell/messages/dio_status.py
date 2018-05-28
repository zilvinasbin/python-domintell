"""
DIO (Input / Output) status (to be inherited)
:author: Zilvinas Binisevicius <zilvinas@binis.me>
"""
import json
import domintell

DIO_COMMAND_CODE = "DIO"

class GenericDIOStatusMessage(domintell.Message):
    """
    Generic Digital input & output hybrid module status
    """

    def __init__(self, pinCount=1, address=None):
        domintell.Message.__init__(self)
        self.moduleType = DIO_COMMAND_CODE
        self.pinCount = pinCount
        self.serialNumber = None
        self.dataType = None
        self._inputs = {}
        self._outputs = {}

        for i in range(0, self.pinCount):
            self._inputs[i] = 0

        for i in range(0, self.pinCount):
            self._outputs[i] = 0
    
    def get_inputs(self):
        return self._inputs

    def get_outputs(self):
        return self._outputs

    def get_input(self, channel):
        if channel < self.pinCount:
            return self._inputs[channel]
        return 0

    def get_output(self, channel):
        if channel < self.pinCount:
            return self._outputs[channel]
        return 0
    
    def is_input(self):
        if self.dataType == 'I':
            return True
        return False

    def is_output(self):
        if self.dataType == 'O':
            return True
        return False

    def populate(self, serialNumber, dataType, dataString):
        """
        :return: None
        """
        assert isinstance(dataString, str)

        self.serialNumber = serialNumber
        self.dataType = dataType

        mask = int(dataString[0:2].strip(), 16)

        if dataType == 'I':
            for input in range(0, self.pinCount):
                self._inputs[input] = 1 if (mask & (input + 1)) else 0

        if dataType == 'O':
            for output in range(0, self.pinCount):
                self._outputs[output] = 1 if (mask & (output + 1)) else 0

    def to_json(self):
        """
        :return: str
        """
        json_dict = self.to_json_basic()
        for input in range(0, self.pinCount):
            if input < len(self._inputs):
                json_dict['input{}'.format(input + 1)] = self._inputs[input]
            if input < len(self._outputs):
                json_dict['output{}'.format(input + 1)] = self._outputs[input]
        return json.dumps(json_dict)
