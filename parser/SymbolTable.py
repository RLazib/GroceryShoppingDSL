class SymbolTable:
    def __init__(self):
        self.table = dict()

    def size(self):
        return len(self.table)

    def contains(self, name):
        return name in self.table

    def get(self, name):
        return self.table.get(name)

    def insert(self, name, type, value):
        self.table[name] = self.Entry(type, value)
        
    def delete(self, name):
        return self.table.pop(name, None)
        
    class Entry:
        def __init__(self, type, value):
            self.type = type
            self.value = value

symbol_table = None

def get_symbol_table():
    global symbol_table
    if symbol_table is None:
        symbol_table = SymbolTable()
    return symbol_table