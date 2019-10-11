from Constants import *
from ASNStatement import ASNStatement

class PartCostASN(ASNStatement):
    def __init__(self, list, store_name):
        super().__init__()
        self.recipe_part = list[0]
        self.store_name = store_name

    def parse(self):
        self.tokenizer.pop_and_check(FOR)
        self.part_cost = self.tokenizer.pop_and_check_regex(NUMBER_MATCHER, "a valid number")
        self.tokenizer.pop_and_check(DOLLARS)
        self.tokenizer.pop_and_check(END_OF_LINE)
        
    def evaluate(self):
        pass
        