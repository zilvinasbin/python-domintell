"""
TRV module status
Output card to control 8 motors

:author: Zilvinas Binisevicius <zilvinas@binis.me>
"""
import json
import domintell
from domintell.messages import GenericDOStatusMessage

TRV_COMMAND_CODE = "TRV"
V24_COMMAND_CODE = "V24"

class DTRVStatusMessage(GenericDOStatusMessage):
    """
    DBIR module status
    """

    def __init__(self, address=None):
        GenericDOStatusMessage.__init__(self, 8)
        self.moduleType = TRV_COMMAND_CODE

class DTRVBTStatusMessage(GenericDOStatusMessage):
    """
    DBIR module status
    """

    def __init__(self, address=None):
        GenericDOStatusMessage.__init__(self, 1)
        self.moduleType = V24_COMMAND_CODE


domintell.register_command(TRV_COMMAND_CODE, DTRVStatusMessage)
domintell.register_command(V24_COMMAND_CODE, DTRVBTStatusMessage)
