"""
DISM4 & DISM8 module status
Communication module.
This module permits the direct connection of 1 to 4 push buttons (DISM04) 
or from 1 to 8 push buttons (DISM08) or any other inputs, detectors, etc. 
Each DISM0x has a unique number which enables it to be 

:author: Zilvinas Binisevicius <zilvinas@binis.me>
"""
import json
import domintell
from domintell.messages.di_status import GenericDIStatusMessage

IS4_COMMAND_CODE = "IS4"
IS8_COMMAND_CODE = "IS8"

class DISM4StatusMessage(GenericDIStatusMessage):
    """
    DISM4 module status
    """

    def __init__(self, address=None):
        GenericDIStatusMessage.__init__(self, IS4_COMMAND_CODE, 4)

class DISM8StatusMessage(GenericDIStatusMessage):
    """
    DISM8 module status
    """
    def __init__(self, address=None):
        GenericDIStatusMessage.__init__(self, IS8_COMMAND_CODE, 8)

domintell.register_command(IS4_COMMAND_CODE, DISM4StatusMessage)
domintell.register_command(IS8_COMMAND_CODE, DISM8StatusMessage)
