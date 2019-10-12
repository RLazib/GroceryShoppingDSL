from Node import Node
from Constants import *
from Error import ParseError

class Use(Node):
    def __init__(self, name, type=None):
        super().__init__()
        self.name = name
        self.type = type
        
    def parse(self):
        pass
        
    def evaluate(self):
        if not self.symbol_table.contains(self.name):
            raise ParseError("Expected declaration of {0} before its usage.".format(self.name))
        
        entry = self.symbol_table.get(self.name)
        name = self.name
        if entry.type == Type.PARAM:
            name = entry.value
            entry = self.symbol_table.get(name)
        if self.type is not None and entry.type != self.type:
            raise ParseError("Expected {0} to be of type {1} but found type {2} instead."
                            .format(self.name, self.type, entry.type))
        return name
        