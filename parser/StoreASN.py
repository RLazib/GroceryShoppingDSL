from Constants import *
from ASNStatement import ASNStatement
from Error import ParseError
from Use import Use

class StoreASN(ASNStatement):
    def __init__(self, list, store_name):
        super().__init__()
        self.ingredients = list
        self.store_name = store_name

    def parse(self):
        self.store_name = Use(self.store_name, Type.STORE)
        self.ingredients = [Use(i, Type.INGREDIENT) for i in self.ingredients]
        self.tokenizer.pop_and_check(END_OF_LINE)
        
    def evaluate(self):
        store_name = self.store_name.evaluate()
        store_entry = self.symbol_table.get(store_name)
        if store_entry.value is None:
            store_entry.value = dict()
            
        for ingredient in self.ingredients:
            i = ingredient.evaluate()
            if i not in store_entry.value:
                store_entry.value[i] = None