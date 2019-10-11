import os
import re
from Error import ParseError

class Tokenizer:

    def __init__(self, filename):
        self.current_token = 0
        self.line = 1
        self.column = 0

        self.file = open(filename, "r")
        if self.file.mode == 'r':
            self.program = self.file.read()
        self.tokens = self.pre_process_input()

    def pre_process_input(self):
        result = re.sub("[:]", lambda match: match.group(0) + " ", self.program)
        result = re.sub("[,;]", lambda match: " " + match.group(0) + " ", self.program)
        result = result.split()
        result = list(filter(None, result))
        return result

    def top(self):
        if self.current_token < len(self.tokens):
            while self.tokens[self.current_token] == os.linesep:
                self.current_token += 1
                self.line += 1
                self.column = 0
            return self.tokens[self.current_token]
        return None

    def pop(self):
        if self.top() is not None:
            token = self.tokens[self.current_token]
            self.current_token += 1
            self.column += 1
            print(token)
            return token
        return None
        
    def pop_and_check(self, expected):
        token = self.pop()
        if expected == token is None:
            raise ParseError("Invalid token at line {0}. Expected: {1} but received {2}."
                                 .format(self.get_line(), expected, token))
        return token
        
    def pop_and_check_regex(self, format, expectedMsg):
        token = self.pop()
        if re.match(format, token) is None:
            raise ParseError("Invalid token at line {0}. Received {1} but expected "
                                 .format(self.get_line(), token) + expectedMsg)
        return token

    def has_next(self):
        return self.top() is not None

    def get_line(self):
        return self.line

    def get_column(self):
        return self.column
        
    def destroy_tokenizer(self):
        self.file.close()

tokenizer = None
        
def create_tokenizer(filename):
    global tokenizer
    if tokenizer is None:
        tokenizer = Tokenizer(filename)
    return tokenizer

def get_tokenizer():
    return tokenizer