
class Maybe:
    """
    A wrapper for a JSON object that may or may not exist.
    Provides safe access to fields and indices without raising exceptions.
    Example usage:
        maybe = Maybe(json_data)
        name = maybe.field('name').value()  # Safely get 'name' field
        first_item = maybe.index(0).value()  # Safely get first item in a list
        items = maybe.array().value()  # Safely get all items in a list
    """
    def __init__(self, json_object):
        self.json_object = json_object

    def __repr__(self):
        return f"Maybe({type(self.json_object)})"
        
    def field(self, field):
        """
        Safely access a field in a JSON object (dict).
        Returns a Maybe wrapping the field value or None if not present.
        Example:
            maybe = Maybe({'name': 'Alice'})
            name = maybe.field('name').value()  # 'Alice'
            age = maybe.field('age').value()    # None
        """
        if self.json_object is not None and type(self.json_object) is dict and field in self.json_object:
            return Maybe(self.json_object[field])
        return Maybe(None)
    
    def index(self, index):
        """
        Safely access an index in a JSON array (list).
        Returns a Maybe wrapping the item value or None if not present.
        Example:
            maybe = Maybe([1, 2, 3])
            first = maybe.index(0).value()  # 1
            fourth = maybe.index(3).value()  # None
        """
        if self.json_object is not None and type(self.json_object) is list and index < len(self.json_object):
            return Maybe(self.json_object[index])
        return Maybe(None)

    def array(self, func=lambda k,o: o, filter=lambda k,o: True, as_type=list):
        """
        Safely convert a JSON array (list) or object (dict) to a list of transformed items.
        Applies the provided function to each item in the array or each key-value pair in the object.
        Filters items based on the provided filter function. Filter is applied before transformation.
        Returns an empty list if the JSON object is neither a list nor a dict.
        Example:
            maybe_list = Maybe([1, 2, 3])
            items = maybe_list.array(lambda k,v: v*2)  # [2, 4, 6]
            filtered_items = maybe_list.array(lambda k,v: v*2, lambda k,v: v > 2)  # [6]

            maybe_dict = Maybe({'a': 1, 'b': 2, 'c': 3})
            items = maybe_dict.array(lambda k,v: (k, v*2), as_type=Maybe).value()  # [('a', 2), ('b', 4), ('c', 6)]
            filtered_items = maybe_dict.array(lambda k,v: (k, v*2), lambda k,v: v > 2, Maybe).value()  # [('c', 6)]

            not_a_list_or_dict = Maybe(42).array()  # []
        """
        if self.json_object is not None:
            if type(self.json_object) is dict:
                return as_type([func(key, obj) for key,obj in self.json_object.items() if filter(key, obj)])
            elif type(self.json_object) is list:
                return as_type([func(idx, obj) for idx,obj in enumerate(self.json_object) if filter(idx, obj)])
        return []
    
    def filter(self, func=lambda k,o: True):
        """
        Safely filter items in a JSON array (list) or object (dict) based on the provided function.
        Returns a Maybe wrapping a list of items that satisfy the filter condition.
        """
        if self.json_object is not None:
            if type(self.json_object) is dict:
                return Maybe({k: v for k,v in self.json_object.items() if func(k,v)})
            elif type(self.json_object) is list:
                return Maybe([obj for idx,obj in enumerate(self.json_object) if func(idx, obj)])
        return Maybe(None)

    def value(self):
        return self.json_object
    
    