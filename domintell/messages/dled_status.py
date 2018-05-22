"""
BIR module status
Output card to control 8 250V/8A two-pole relays.

:author: Zilvinas Binisevicius <zilvinas@binis.me>
"""
import json
import domintell
from domintell.messages import GenericDOStatusMessage

LED_COMMAND_CODE = "LED"

class DLEDStatusMessage(GenericDOStatusMessage):
    """
    DBIR module status
    """

    def __init__(self, address=None):
        GenericDOStatusMessage.__init__(self, 4)
        self.moduleType = LED_COMMAND_CODE

domintell.register_command(LED_COMMAND_CODE, DLEDStatusMessage)
