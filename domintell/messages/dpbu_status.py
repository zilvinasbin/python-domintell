"""
DPBUx  module status
:author: Zilvinas Binisevicius <zilvinas@binis.me>
"""
import json
import domintell
import domintell.messages
from domintell.messages import GenericDIOStatusMessage

BU1_COMMAND_CODE = "BU1"
BU2_COMMAND_CODE = "BU2"
BU4_COMMAND_CODE = "BU4"
BU6_COMMAND_CODE = "BU6"

class DPBU01StatusMessage(GenericDIOStatusMessage):
    """
    DPBU01 module status
    """
    def __init__(self, address=None):
        GenericDIOStatusMessage.__init__(self, 1)
        self.moduleType = BU1_COMMAND_CODE

class DPBU02StatusMessage(DPBU01StatusMessage):
    """
    DPBU02 module status
    """
    def __init__(self, address=None):
        GenericDIOStatusMessage.__init__(self, 2)
        self.moduleType = BU2_COMMAND_CODE

class DPBU04StatusMessage(DPBU02StatusMessage):
    """
    DPBU04 module status
    """
    def __init__(self, address=None):
        GenericDIOStatusMessage.__init__(self, 4)
        self.moduleType = BU4_COMMAND_CODE

class DPBU06StatusMessage(DPBU04StatusMessage):
    """
    DPBU06 module status
    """
    def __init__(self, address=None):
        GenericDIOStatusMessage.__init__(self, 6)
        self.moduleType = BU6_COMMAND_CODE

domintell.register_command(BU1_COMMAND_CODE, DPBU01StatusMessage)
domintell.register_command(BU2_COMMAND_CODE, DPBU02StatusMessage)
domintell.register_command(BU4_COMMAND_CODE, DPBU04StatusMessage)
domintell.register_command(BU6_COMMAND_CODE, DPBU06StatusMessage)
