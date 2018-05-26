"""
:author: Thomas Delaet <thomas@delaet.org>
"""
import domintell

COMMAND_CODE = "__MODULE_STATUS__"


class ModuleStatusRequest(domintell.Command):
    """
        Request module status
    """
    def __init__(self, moduleType, serialNumber):
        domintell.Command.__init__(self, moduleType, serialNumber)
        self.moduleType = moduleType

    def command(self):
        return "{:3}{:>6}%S".format(self.moduleType, self.serialNumber)

domintell.register_command(COMMAND_CODE, ModuleStatusRequest)
