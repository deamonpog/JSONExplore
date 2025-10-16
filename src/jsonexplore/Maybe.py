class Maybe:
    def __init__(self, json_object):
        self.json_object = json_object

    def __repr__(self):
        return f"Maybe({type(self.json_object)})"
        
    def field(self, field):
        if self.json_object is not None and type(self.json_object) is dict and field in self.json_object:
            return Maybe(self.json_object[field])
        return Maybe(None)
    
    def index(self, index):
        if self.json_object is not None and type(self.json_object) is list and index < len(self.json_object):
            return Maybe(self.json_object[index])
        return Maybe(None)
    
    def array(self, func=lambda m: m, as_type=list):
        if self.json_object is not None and type(self.json_object) is list:
            return as_type([func(obj) for obj in self.json_object])
        return []
    
    def array_from_dict(self, func=lambda k,o: o, as_type=list):
        if self.json_object is not None:
            return as_type([func(key, obj) for key,obj in self.json_object.items()])
        return []
    
    def value(self):
        return self.json_object
    
    