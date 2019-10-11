from Statement import Statement
from Utils import parse_list
from Constants import *

class DecStatement(Statement):
    def __init__(self):
        super().__init__()
        self.declarations = []
        
    def parse(self):
        pass

    def evaluate(self):
        pass
        
    def parse_dec_list(self):
        self.declarations = parse_list(END_OF_LINE)
        self.tokenizer.pop_and_check(END_OF_LINE)
     