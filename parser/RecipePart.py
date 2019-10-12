from Node import Node
from Constants import *
from Error import ParseError
from Use import Use
import re

class RecipePart(Node):
    def __init__(self, recipe_part):
        super().__init__()
        self.recipe_part = recipe_part
        
    def parse(self):
        index = self.recipe_part.find(" ")
        self.quantity = self.recipe_part[:index]
        if re.match(NUMBER_MATCHER, self.quantity) is None:
            raise ParseError("Invalid token at line {0}. Received {1} but expected a valid number"
                                 .format(self.tokenizer.get_line(), self.quantity))
        self.quantity = float(self.quantity)
        self.recipe_part = self.recipe_part[index+1:]
        
    def evaluate(self):
        optionalStr = " of "
        index = self.recipe_part.find(optionalStr)
        if index == -1:
            measure = ""
            ingredient = ""
            split = self.recipe_part.split(" ")
            i = 0
            while i < len(split) and (not self.symbol_table.contains(measure) or self.symbol_table.get(measure).type != Type.MEASUREMENT):
                if len(measure) > 0:
                    measure += " "
                measure += split[i]
                i = i + 1
            ingredient = " ".join(split[i:])
        else:
            measure = self.recipe_part[:index]
            ingredient = self.recipe_part[index+len(optionalStr):]
        
        measure = Use(measure, Type.MEASUREMENT).evaluate()
        ingredient = Use(ingredient, Type.INGREDIENT).evaluate()
                            
        return RecipePartObj(self.quantity, measure, ingredient)
        
    

class RecipePartObj():
    def __init__(self, quantity, measure, ingredient):
        self.quantity = quantity
        self.measure = measure
        self.ingredient = ingredient
        