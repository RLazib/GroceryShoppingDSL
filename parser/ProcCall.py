from Statement import Statement
from Utils import parse_name
from Constants import *

class ProcCall(Statement):
    def parse(self):
        self.tokenizer.pop_and_check(CALL)
        self.proc_name = parse_name([WITH])
        self.tokenizer.pop_and_check(WITH)
        self.proc_param = parse_name([END_OF_LINE])
        self.tokenizer.pop_and_check(END_OF_LINE)
            
    def evaluate(self):
        pass
     