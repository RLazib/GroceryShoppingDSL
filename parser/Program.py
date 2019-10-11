from Node import Node
from StatementParser import parse_statement
from ProcDef import ProcDef
from Constants import *
from Error import ParseError

class Program(Node):
    def parse(self):
        self.tokenizer.pop_and_check(START)
        self.statements = []
        while(self.tokenizer.has_next() and self.tokenizer.top() != END):
            if self.tokenizer.top() == DEF:
                statement = ProcDef()
                statement.parse()
                self.statements.append(statement)
            else:
                self.statements.append(parse_statement())
        self.tokenizer.pop_and_check(END)
        if self.tokenizer.has_next():
            raise ParseError("Expected no more tokens after {0} at line {1}."
                            .format(END, tokenizer.get_line()))

    def evaluate(self):
        pass
