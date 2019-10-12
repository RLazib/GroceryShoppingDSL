from ASNStatement import ASNStatement
from Constants import *
from Utils import *
from RecipePart import RecipePart
from Use import Use

class RecipeASN(ASNStatement):
    def parse(self):
        self.tokenizer.pop_and_check(MAKE)
        self.recipe_name = Use(parse_name([WITH]), Type.RECIPE)
        self.tokenizer.pop_and_check(WITH)
        self.recipe_parts = []
        for recipe_part in parse_list(END_OF_LINE):
            part = RecipePart(recipe_part)
            part.parse()
            self.recipe_parts.append(part)
        
    def evaluate(self):
        recipe_name = self.recipe_name.evaluate()
        recipe_entry = self.symbol_table.get(recipe_name)
        if recipe_entry.value is None:
            recipe_entry.value = dict()
            
        for recipe_part in self.recipe_parts:
            part = recipe_part.evaluate()
            recipe_entry.value[part.ingredient] = { "quantity": part.quantity, "measurement": part.measure }
        