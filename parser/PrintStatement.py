from Statement import Statement
from Utils import parse_name
from Use import Use
from Constants import *

class PrintStatement(Statement):
    def parse(self):
        self.tokenizer.pop_and_check(PRINT)
        self.name = Use(parse_name([END_OF_LINE]))
        self.tokenizer.pop_and_check(END_OF_LINE)
            
    def evaluate(self):
        name = self.name.evaluate()
        self.output.write(name)
     