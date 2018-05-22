"""
:author: Zilvinas Binisevicius <zilvinas@binis.me>
"""
import domintell


class Ping(domintell.Command):
    """
        send: &APPINFO
    """
    def __init__(self):
        domintell.Command.__init__(self)

    def command(self, moduleType, serialNumber, dataType=None, value=None):
        return "&PING"
