"""
VAR & SYS

:author: Zilvinas Binisevicius <zilvinas@binis.me>
"""
import json
import domintell
from domintell.messages import GenericDIStatusMessage

VAR_COMMAND_CODE = "VAR"
SYS_COMMAND_CODE = "SYS"


class GenericVARStatusMessage(GenericDIStatusMessage):
    """
    DISM4 module status
    """
    def __init__(self, command_code=VAR_COMMAND_CODE, address=None):
        GenericDIStatusMessage.__init__(self, command_code, 1)
        self.serialNumber = None
        self.dataType = None
        self.var = 0

    def populate(self, serialNumber, dataType, dataString):
        if dataType == "O":
            self.populateA(serialNumber, dataType, dataString)
        elif dataType == "D":
            self.populateD(serialNumber, dataType, dataString)

    def populateD(self, serialNumber, dataType, dataString):
        assert isinstance(dataString, str)
        self.serialNumber = serialNumber
        self.dataType = dataType
        if dataString[0:2].strip() == "00":
            self.var = 0
        else:
            self.var = 1

    def populateA(self, serialNumber, dataType, dataString):
        self.serialNumber = serialNumber
        self.dataType = dataType
        self.var = int(dataString[0:2].strip(), 16)

    def to_json(self):
        """
        :return: str
        """
        json_dict = self.to_json_basic()
        json_dict['var'] = self.var
        return json.dumps(json_dict)



class VARStatusMessage(GenericVARStatusMessage):
    """
    VAR  status
    """
    def __init__(self, address=None):
        GenericVARStatusMessage.__init__(self, VAR_COMMAND_CODE)


class SYSStatusMessage(GenericVARStatusMessage):
    """
    SYS  status
    """
    def __init__(self, address=None):
        GenericVARStatusMessage.__init__(self, SYS_COMMAND_CODE)



domintell.register_command(VAR_COMMAND_CODE, VARStatusMessage)
domintell.register_command(SYS_COMMAND_CODE, SYSStatusMessage)
