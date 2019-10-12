from Statement import Statement
from Utils import parse_list
from Constants import *

class DecStatement(Statement):
    def __init__(self):
        super().__init__()
        self.declarations = []
        
    def parse(self):
        self.tokenizer.pop_and_check(self.get_dec_token())
        self.declarations = parse_list(END_OF_LINE)

    def evaluate(self):
        for dec in self.declarations:
            self.symbol_table.insert(dec, self.get_dec_type(), None)
            
    def get_dec_token(self):
        pass
            
    def get_dec_type(self):
        pass
     