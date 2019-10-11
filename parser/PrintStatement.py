from Statement import Statement
from Utils import parse_name
from Constants import *

class PrintStatement(Statement):
    def parse(self):
        self.tokenizer.pop_and_check(PRINT)
        self.name = parse_name(END_OF_LINE)
        self.tokenizer.pop_and_check(END_OF_LINE)
            
    def evaluate(self):
        pass
     