"""
:author: Zilvinas Binisevicius <zilvinas@binis.me>
"""
import domintell


class Ping(domintell.Command):
    """
        send: &PING message
    """
    def __init__(self):
        domintell.Command.__init__(self)

    def command(self):
        return "&PING"
