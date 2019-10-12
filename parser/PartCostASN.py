from Constants import *
from ASNStatement import ASNStatement
from RecipePart import RecipePart
from Use import Use

class PartCostASN(ASNStatement):
    def __init__(self, list, store_name):
        super().__init__()
        self.recipe_part = RecipePart(list[0])
        self.store_name = store_name

    def parse(self):
        self.recipe_part.parse()
        self.store_name = Use(self.store_name, Type.STORE)
        self.tokenizer.pop_and_check(FOR)
        self.part_cost = float(self.tokenizer.pop_and_check_regex(NUMBER_MATCHER, "a valid number."))
        self.tokenizer.pop_and_check(DOLLARS)
        self.tokenizer.pop_and_check(END_OF_LINE)
        
    def evaluate(self):
        store_name = self.store_name.evaluate()
        part = self.recipe_part.evaluate()                    
        store_entry = self.symbol_table.get(store_name)
        if part.ingredient not in store_entry.value:
            raise ParseError("Expected store {0} to be selling {1}.".format(store_name, part.ingredient))
        
        store_entry.value[part.ingredient] = { "measure": part.measure, "price": self.part_cost / part.quantity }
        