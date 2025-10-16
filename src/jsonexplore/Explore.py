class Explore:
    def __init__(self, json_object):
        self.json_object = json_object
        self.child_keys = []
        if type(self.json_object) is dict:
            self.child_keys = list(self.json_object.keys())
        if type(self.json_object) is list:
            self.child_keys = [idx for idx in range(len(self.json_object))]

    def __repr__(self):
        return f"Explore({type(self.json_object)}[size={len(self.child_keys)}])"

    def get_child_keys(self):
        return self.child_keys
    
    def explore_child(self, child_key):
        if child_key in self.json_object:
            return Explore(self.json_object[child_key])
        return Explore(None)
    
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