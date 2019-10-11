from DecStatement import DecStatement
from Constants import *

class StoresDec(DecStatement):
    def parse(self):
        self.tokenizer.pop_and_check(STORES)
        self.parse_dec_list()

    def evaluate(self):
        pass
        