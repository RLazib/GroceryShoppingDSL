from DecStatement import DecStatement
from Constants import *

class IngredientsDec(DecStatement):
    def parse(self):
        self.tokenizer.pop_and_check(INGREDIENTS)
        self.parse_dec_list()

    def evaluate(self):
        pass
        