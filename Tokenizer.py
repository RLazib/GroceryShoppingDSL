import os


class Tokenizer:

    def __init__(self, filename):
        self.current_token = 0
        self.line = 1
        self.column = 0

        file = open(filename, "r")
        if file.mode == 'r':
            self.program = file.read()
        self.tokens = self.pre_proccess_input()

    def pre_proccess_input(self):
        result = self.program.split()
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
            return token
        return None

    def has_next(self):
        return self.top() is not None

    def get_line(self):
        return self.line

    def get_column(self):
        return self.column
