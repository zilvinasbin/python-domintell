"""
DMOV01 & DMOV01 module status
PIR movement detector.

:author: Zilvinas Binisevicius <zilvinas@binis.me>
"""
import json
import domintell
from domintell.messages import GenericDIStatusMessage

DMOV_COMMAND_CODE = "DET"

class DMOVStatusMessage(GenericDIStatusMessage):
    """
    DMOV module status
    """
    def __init__(self, address=None):
        GenericDIStatusMessage.__init__(self, 1)
        self.moduleType = DMOV_COMMAND_CODE

domintell.register_command(DMOV_COMMAND_CODE, DMOVStatusMessage)
