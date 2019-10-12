from Node import Node
from Utils import parse_name
from ProcBlock import ProcBlock
from Constants import *

class ProcDef(Node):
    def parse(self):
        self.tokenizer.pop_and_check(DEF)
        self.name = parse_name([WITH])
        self.proc_block = ProcBlock()
        self.proc_block.parse()

    def evaluate(self):
        self.symbol_table.insert(self.name, Type.PROC, self.proc_block)
     