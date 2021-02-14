"""
:author: Zilvinas Binisevicius <zilvinas@binis.me>
"""
import domintell


class SetDigitalOutputMessage(domintell.Command):
    def __init__(self, moduleType, serialNumber, channel, value):
        val = 1 if value > 0 else 0
        print("val={}", val)
        domintell.Command.__init__(self, moduleType, serialNumber, channel, "%I", val)

class SetDigitalOutputOnMessage(domintell.Command):
    def __init__(self, moduleType, serialNumber, channel):
        domintell.Command.__init__(self, moduleType, serialNumber, channel, "%I")

class SetDigitalOutputOffMessage(domintell.Command):
    def __init__(self, moduleType, serialNumber, channel):
        domintell.Command.__init__(self, moduleType, serialNumber, channel, "%O")

class TogleDigitalOutputMessage(domintell.Command):
    def __init__(self, moduleType, serialNumber, channel):
        domintell.Command.__init__(self, moduleType, serialNumber, channel, "")

""" Cover support added """
class SetDigitalOutputOpenMessage(domintell.Command):
    def __init__(self, moduleType, serialNumber, channel):
        domintell.Command.__init__(self, moduleType, serialNumber, channel*2-1, "%I")

class SetDigitalOutputCloseMessage(domintell.Command):
    def __init__(self, moduleType, serialNumber, channel):
        domintell.Command.__init__(self, moduleType, serialNumber, channel*2, "%I")

class SetDigitalOutputStopMessage(domintell.Command):
    def __init__(self, moduleType, serialNumber, channel):
        domintell.Command.__init__(self, moduleType, serialNumber, channel*2, "%O")
