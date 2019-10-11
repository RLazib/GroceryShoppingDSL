from Constants import *
from ASNStatement import ASNStatement

class StoreASN(ASNStatement):
    def __init__(self, list, store_name):
        super().__init__()
        self.list = list
        self.store_name = store_name

    def parse(self):
        self.tokenizer.pop_and_check(END_OF_LINE)
        
    def evaluate(self):
        pass
        