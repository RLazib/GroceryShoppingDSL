from Tokenizer import get_tokenizer
from OutputWriter import get_output
from SymbolTable import get_symbol_table

class Node:

    def __init__(self):
        self.tokenizer = get_tokenizer()
        self.output = get_output()
        self.symbol_table = get_symbol_table()

    def parse(self):
        pass

    def evaluate(self):
        pass

