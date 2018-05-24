"""
AO status (to be inherited)
:author: Zilvinas Binisevicius <zilvinas@binis.me>
"""
import json
import domintell

AO_COMMAND_CODE = "AO"

class GenericAOStatusMessage(domintell.Message):
    """
    Generic Analog output module status
    """

    def __init__(self, outputCount=1, address=None):
        domintell.Message.__init__(self)
        self.moduleType = AO_COMMAND_CODE
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
        self.serialNumber = serialNumber
        self.dataType = dataType

        for output in range(0, self.outputCount):
            self.outputs[output] = int(dataString[output * 2: (output * 2) + 2].strip(), 16)

    def to_json(self):
        """
        :return: str
        """
        json_dict = self.to_json_basic()
        for output in range(0, self.outputCount):
            if output < len(self.outputs):
                json_dict['output{}'.format(output + 1)] = self.outputs[output]
        return json.dumps(json_dict)

    def is_on(self, output):
        if output < self.outputCount:
            if self.outputs[output] > 0:
                return True
        return False
    
    def get_value(self, output):
        if output < self.outputCount:
            return self.outputs[output]
        return 0

    def get_values(self):
        return self.outputs
        