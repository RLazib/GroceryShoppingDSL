class SymbolTable:
    def __init__(self):
        self.table = dict()

    def size(self):
        return len(self.table)

    def contains(self, name):
        return name in self.table

    def get(self, name):
        return self.table.get(name)

    def insert(self, name, node):
        self.table[name] = node
