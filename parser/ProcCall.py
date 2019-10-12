from Statement import Statement
from Utils import parse_name
from Constants import *

class ProcCall(Statement):
    def parse(self):
        self.tokenizer.pop_and_check(CALL)
        self.proc_name = parse_name([WITH])
        self.tokenizer.pop_and_check(WITH)
        self.proc_arg = parse_name([END_OF_LINE])
        self.tokenizer.pop_and_check(END_OF_LINE)
            
    def evaluate(self):
        if not self.symbol_table.contains(self.proc_name) or self.symbol_table.get(self.proc_name).type != Type.PROC:
            raise ParseError("Expected declaration of procedure {0} before its usage."
                            .format(self.proc_name))
        proc_block = self.symbol_table.get(self.proc_name).value
        proc_block.set_arg(self.proc_arg)
        proc_block.evaluate()
     