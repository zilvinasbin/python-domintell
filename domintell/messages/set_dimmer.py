"""
:author: Zilvinas Binisevicius <zilvinas@binis.me>
"""
import domintell
from domintell.messages import SetAnalogOutputMessage

class SetDimmer(SetAnalogOutputMessage):

    def __init__(self, serialNumber, value):
        SetAnalogOutputMessage.__init__(self, "DIM", serialNumber, "%D", value)

class StartDimmer(domintell.Command):
    """
        Start dimmer action
    """
    def __init__(self, serialNumber):
        domintell.Command.__init__(self, "DIM", serialNumber, "%DB")

class StopDimmer(domintell.Command):
    """
        Stop dimmer action
    """
    def __init__(self, serialNumber):
        domintell.Command.__init__(self, "DIM", serialNumber, "%DE")

class IncrementDimmer(domintell.Command):
    """
        Increment dimmer
    """
    def __init__(self, serialNumber, value):
        domintell.Command.__init__(self, "DIM", serialNumber, "%I%D", value)

class DecrementDimmer(domintell.Command):
    """
        Decrement dimmer
    """
    def __init__(self, serialNumber, value):
        domintell.Command.__init__(self, "DIM", serialNumber, "%O%D", value)
