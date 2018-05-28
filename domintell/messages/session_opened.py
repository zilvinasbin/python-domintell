"""
Session opened  Message
:author: Zilvinas Binisevicius <zilvinas@binis.me>
"""
import json
import domintell

class SessionOpenedMessage(domintell.Message):
    """
    Session opened message
    """

    def __init__(self, moduleType=None, data=None):

        domintell.Message.__init__(self)
        self._message = ''
        if data[0:24] == 'INFO:Session opened:INFO':
            self.moduleType = 'SESSION_OPENED'
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
