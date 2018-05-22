"""
BIR module status
Output card to control 8 250V/8A two-pole relays.

:author: Zilvinas Binisevicius <zilvinas@binis.me>
"""
import json
import domintell
from domintell.messages import GenericAOStatusMessage

class DDIMStatusMessage(GenericAOStatusMessage):
    COMMAND_CODE = 'DIM'
    """
    DDIM module status
    """
    def __init__(self, address=None):
        GenericAOStatusMessage.__init__(self, 8)
        self.moduleType = DDIMStatusMessage.COMMAND_CODE

domintell.register_command(DDIMStatusMessage.COMMAND_CODE, DDIMStatusMessage)
