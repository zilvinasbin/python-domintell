"""
Simulate digital inputs
:author: Zilvinas Binisevicius <zilvinas@binis.me>
"""
import domintell


class DigitalShortPush(domintell.Command):
    """Simulate SHORT signal on digital input"""
    def __init__(self, moduleType, serialNumber):
        domintell.Command.__init__(self, moduleType, serialNumber, "%P1")

class DigitalLongPush(domintell.Command):
    """Simulate LONG signal on digital input"""
    def __init__(self, moduleType, serialNumber):
        domintell.Command.__init__(self, moduleType, serialNumber, "%P3")

class DigitalShortPushEnd(domintell.Command):
    """Simulate End of Short signal on digital input"""
    def __init__(self, moduleType, serialNumber):
        domintell.Command.__init__(self, moduleType, serialNumber, "%P2")

class DigitalLongPushEnd(domintell.Command):
    """Simulate End of Long signal on digital input"""
    def __init__(self, moduleType, serialNumber):
        domintell.Command.__init__(self, moduleType, serialNumber, "%P4")