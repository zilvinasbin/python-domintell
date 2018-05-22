"""
BIR module status
Output card to control 8 250V/8A two-pole relays.

:author: Zilvinas Binisevicius <zilvinas@binis.me>
"""
import json
import domintell
from domintell.messages import GenericAIStatusMessage

DIN10V_COMMAND_CODE = "I10"

class DIN10VStatusMessage(GenericAIStatusMessage):
    """
    I10 module status
    """
    def __init__(self, address=None):
        GenericAIStatusMessage.__init__(self, 10)
        self.moduleType = DIN10V_COMMAND_CODE

domintell.register_command(DIN10V_COMMAND_CODE, DIN10VStatusMessage)
