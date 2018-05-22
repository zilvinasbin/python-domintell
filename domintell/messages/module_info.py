"""
Module Info Message
:author: Zilvinas Binisevicius <zilvinas@binis.me>
"""
import json
import domintell

class ModuleInfoMessage(domintell.Message):
    """
    Module information
    """

    def __init__(self, moduleType, data=None):

        domintell.Message.__init__(self)

        self.moduleType = moduleType
        self.serialNumber = data[3:9].strip()
        self.channel = 1

        _pos = ''
        _name_section_start = 9
        if data[9:10] == '-':
            self.channel = data[10:11]
            _pos = '-' + self.channel
            _name_section_start = 11
        
        # point_id is used for compatibility with CornFlower and
        # for sending commands back to domintell bus.
        # point id is a concept widely used in industrial control :)
        self.point_id = self.serialNumber.strip() + _pos

        # user point id as a default name
        self.name = self.point_id

           # start of name section
        _name_section_end = data.find("[")  # end of name section
        _path_section_end = data.find("]")  # path section end

        if _name_section_start > 0:
            if _name_section_end > _name_section_start:
                self.name = data[_name_section_start: _name_section_end].strip()
        else:
            if self.moduleType == 'TRP':
                self.name = data[9:]
        
        if _path_section_end > _name_section_end:
            self.path = data[_name_section_end + 1 : _path_section_end].rstrip('|')


    def to_json(self):
        """
        :return: str
        """
        json_dict = self.to_json_basic()
        json_dict['module_type'] = self.moduleType
        json_dict['point_id'] = self.point_id
        json_dict['serial_number'] = self.serialNumber
        json_dict['channel'] = self.channel
        json_dict['name'] = self.name
        json_dict['path'] = self.path
        return json.dumps(json_dict)

