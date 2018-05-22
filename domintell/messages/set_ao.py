"""
:author: Zilvinas Binisevicius <zilvinas@binis.me>
"""
import domintell


class SetAnalogOutputMessage(domintell.Command):

    def __init__(self, module_type, serial_number, channel=0, value=0):
        domintell.Command.__init__(self, module_type, serial_number, channel, "%D", value)

