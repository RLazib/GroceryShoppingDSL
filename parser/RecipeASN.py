from ASNStatement import ASNStatement
from Constants import *
from Utils import *

class RecipeASN(ASNStatement):
    def parse(self):
        self.tokenizer.pop_and_check(MAKE)
        self.recipe_name = parse_name([WITH])
        self.tokenizer.pop_and_check(WITH)
        self.recipe_parts = parse_list(END_OF_LINE)
        self.tokenizer.pop_and_check(END_OF_LINE)
        
    def evaluate(self):
        pass
        