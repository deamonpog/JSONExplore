
from .Maybe import Maybe
from .Explore import Explore
from .SimpleXML import SimpleXML


class Xplore:
    def __init__(self, data):
        self.data = data
        self.explore = Explore(data)
        self.maybe = Maybe(data)
        self.xml = SimpleXML(data) if isinstance(data, str) and data.strip().startswith("<") else None

    def __repr__(self):
        return f"Explore({type(self.data)}[size={len(self.data)}])" if hasattr(self.data, "__len__") else f"Xplore({type(self.data)})[size=N/A]"
