"""
:author: Zilvinas Binisevicius <zilvinas@binis.me>
"""
import json
import domintell

class ControllMessage(domintell.Message):
    """
    Control message
    Start or End of APPINFO sections
    """

    def __init__(self, message_type=None, data=None):

        domintell.Message.__init__(self, message_type)
        if self.moduleType == "APPINFO":
            self._is_appinfo_mode = True
        elif self.moduleType == "END APPINFO":
            self._is_appinfo_mode = False
        self._message = data
    
    def populate(self, serialNumber, dataType, dataString):
        pass

    def to_json(self):
        """
        :return: str
        """
        json_dict = self.to_json_basic()
        json_dict['is_app_info'] = self._is_appinfo_mode
        json_dict['info_message'] = self._message
        return json.dumps(json_dict)
