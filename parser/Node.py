from Tokenizer import get_tokenizer
from OutputWriter import get_output_file

class Node:

    def __init__(self):
        self.tokenizer = get_tokenizer()
        self.output_file = get_output_file()

    def parse(self):
        pass

    def evaluate(self):
        pass

