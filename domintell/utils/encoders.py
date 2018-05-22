import json
from json import JSONEncoder
from domintell.module import Module
from decimal import Decimal

class ModuleJSONEncoder(JSONEncoder):
    """
    Convert module to json
    """
    #pylint: disable=E0202
    def default(self, obj):
        if issubclass(obj.__class__, Module):
            return obj.to_json_basic()
        return JSONEncoder.default(self, obj)


class DecimalEncoder(json.JSONEncoder):
    #pylint: disable=E0202
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return json.JSONEncoder.default(self, obj)