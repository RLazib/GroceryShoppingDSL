from DecStatement import DecStatement
from Constants import *

class MeasuresDec(DecStatement):
    def parse(self):
        self.tokenizer.pop_and_check(MEASUREMENTS)
        self.parse_dec_list()

    def evaluate(self):
        pass
        