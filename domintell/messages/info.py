"""
Module Info Message
:author: Zilvinas Binisevicius <zilvinas@binis.me>
"""
import json
import domintell

class InfoMessage(domintell.Message):
    """
    Generic info message
    """

    def __init__(self, moduleType=None, data=None):

        domintell.Message.__init__(self)

        self._message = ''

        if (moduleType == 'INF' and data[0:5] == 'INFO:') or moduleType == '!! ' or (moduleType == 'APP' and data[0:7] == 'APPINFO'):
            self.moduleType = 'INFO'
            self._message = data
    
    def populate(self, serialNumber, dataType, dataString):
        pass

    def to_json(self):
        """
        :return: str
        """
        json_dict = self.to_json_basic()
        json_dict['info_message'] = self._message
        return json.dumps(json_dict)

domintell.register_command("INF", InfoMessage)
domintell.register_command("!! ", InfoMessage)
domintell.register_command("APP", InfoMessage)