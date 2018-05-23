"""
Port for Domintell
:author: Zilvinas Binisevicius <zilvinas@binis.me>
"""
import json
import base64
import domintell
from domintell.module_directory import get_point_id

class Command(domintell.Message):
    # pylint: disable-msg=R0904
    """
    Base Domintell message
    """

    def __init__(self, module_type=None, serial_number=None, channel=0, command=None, data=None):
        domintell.Message.__init__(self, module_type, serial_number)
        self._command = command
        self._data = data
        self._channel = channel

    def populate(self, serial_number, data_type, data_string):
        pass

    def command(self, module_type, point_id, data_type=None, value=None):
        if data_type == None:
            data_type = ''
        if len(data_type) < 1:
            data_type = ''
        if value != None:
            return "{:3}{:>8}{}{}".format(module_type, point_id, data_type, value)
        return "{:3}{:>8}{}".format(module_type, point_id, data_type)

    def to_string(self):
        """
        Convert to domintell controll string
        This method can be overridden in subclasses to include more than just generic attributes
        :return: str
        """
        pid = get_point_id(self.moduleType, self.serialNumber, self._channel)
        return self.command(self.moduleType, pid, self._command, self.data)
