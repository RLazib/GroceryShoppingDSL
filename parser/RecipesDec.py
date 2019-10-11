from DecStatement import DecStatement
from Constants import *

class RecipesDec(DecStatement):
    def parse(self):
        self.tokenizer.pop_and_check(RECIPES)
        self.parse_dec_list()

    def evaluate(self):
        pass
        