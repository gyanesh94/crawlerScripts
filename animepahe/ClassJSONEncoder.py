# Encode class object to JSON Serializable
from json import JSONEncoder

class ClassJSONEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
