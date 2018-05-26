"""
:author: Zilvinas Binisevicius <zilvinas@binis.me>
"""
import domintell


class AppInfoRequest(domintell.Command):
    """
        send: &APPINFO
    """
    def __init__(self):
        domintell.Command.__init__(self, "_APPINFO_", "_APPINFO_")

    def command(self):
        return "APPINFO"
