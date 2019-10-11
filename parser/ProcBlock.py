from Statement import Statement
from Utils import parse_name
from Constants import *
from StatementParser import parse_statement

class ProcBlock(Statement):
    def parse(self):
        self.tokenizer.pop_and_check(WITH)
        parse_name([PROCSTART])
        self.tokenizer.pop_and_check(PROCSTART)
        self.statements = []
        while(self.tokenizer.has_next() and self.tokenizer.top() != PROCEND):
            self.statements.append(parse_statement())
        self.tokenizer.pop_and_check(PROCEND)
            
    def evaluate(self):
        pass
     