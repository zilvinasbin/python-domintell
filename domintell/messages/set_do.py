"""
:author: Zilvinas Binisevicius <zilvinas@binis.me>
"""
import domintell


class SetDigitalOutputMessage(domintell.Command):

    def __init__(self, moduleType, serialNumber, channel, value):
        val = 1 if value > 0 else 0
        domintell.Command.__init__(self, moduleType, serialNumber, channel, "%I", val)

class TogleDigitalOutputMessage(domintell.Command):
    def __init__(self, moduleType, serialNumber, channel):
        domintell.Command.__init__(self, moduleType, serialNumber, channel, "")

