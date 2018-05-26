"""
DO status (to be inherited)
:author: Zilvinas Binisevicius <zilvinas@binis.me>
"""
import json
import domintell

DO_COMMAND_CODE = "DO"

class GenericDOStatusMessage(domintell.Message):
    """
    Generic Digital output module status
    """

    def __init__(self, outputCount=1, address=None):
        domintell.Message.__init__(self)
        self.moduleType = DO_COMMAND_CODE
        self.outputCount = outputCount
        self.serialNumber = None
        self.dataType = None
        self.outputs = {}
        for i in range(0, self.outputCount):
            self.outputs[i] = 0

    def populate(self, serialNumber, dataType, dataString):
        """
        :return: None
        """
        # assert isinstance(dataString, str)

        self.serialNumber = serialNumber
        self.dataType = dataType

        mask = int(dataString[0:2].strip(), 16)

        for output in range(0, self.outputCount):
            c = pow(2, output)
            self.outputs[output] = 1 if (mask & c) == c else 0

    def to_json(self):
        """
        :return: str
        """
        json_dict = self.to_json_basic()
        for output in range(0, self.outputCount):
            if output < len(self.outputs):
                json_dict['output{}'.format(output)] = self.outputs[output]
        return json.dumps(json_dict)
    
    def get_values(self):
        return self.outputs
    
    def is_on(self, channel):
        return self.outputs[channel - 1] == 1
