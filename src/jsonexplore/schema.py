import os
import json

#from pprint import pprint
# from .file_reader import get_json_file_paths, read_json_file

# TEST_JSON_BASE = r"D:\PROJECTS\itemlol\DD\dragontail-15.20.1\15.20.1\data\en_US"

# file_paths = get_json_file_paths(TEST_JSON_BASE, pattern="item.json")
# pprint(file_paths)

# this_file_path = file_paths[0]
# json_data = read_json_file(this_file_path)

class ExploreUnknown:
    def __init__(self, json_object):
        self.json_object = json_object
        self.child_keys = []
        if type(self.json_object) is dict:
            self.child_keys = list(self.json_object.keys())
        if type(self.json_object) is list:
            self.child_keys = [idx for idx in range(len(self.json_object))]

    def __repr__(self):
        return f"ExploreUnkown({type(self.json_object)}[size={len(self.child_keys)}])"

    def get_child_keys(self):
        return self.child_keys
    
    def explore_child(self, child_key):
        if child_key in self.json_object:
            return ExploreUnknown(self.json_object[child_key])
        return ExploreUnknown(None)
    
    def invest_grandchildren(self, verbose=False):
        if verbose:
            print(f"Exploring grandchildren of type: {type(self.child_keys)} (size={len(self.json_object)}) with keys: {self.get_child_keys()}")
        counts = {}
        for child_key in self.child_keys:
            if verbose:
                print(f"Exploring child key: {child_key}")
            expChild = self.explore_child(child_key)
            if verbose:
                print(f"  Child type: {type(expChild.json_object)} with keys: {expChild.get_child_keys()}")
            for grandChildKey in expChild.get_child_keys():
                if verbose:
                    print(f"    Found grandchild key: {grandChildKey}")
                if grandChildKey in counts:
                    counts[grandChildKey] += 1
                else:
                    counts[grandChildKey] = 1
            
        return counts
        
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




    

