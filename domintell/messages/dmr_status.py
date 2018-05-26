"""
DMR module status
Output card to control 8 250V/8A two-pole relays.

:author: Zilvinas Binisevicius <zilvinas@binis.me>
"""
import json
import domintell
from domintell.messages import GenericDOStatusMessage

DMR_COMMAND_CODE = "DMR"

class DDMRStatusMessage(GenericDOStatusMessage):
    """
    DBIR module status
    """

    def __init__(self, address=None):
        GenericDOStatusMessage.__init__(self, 5)
        self.moduleType = DMR_COMMAND_CODE

domintell.register_command(DMR_COMMAND_CODE, DDMRStatusMessage)
