from Node import Node
from Tokens import *
from Error import ParseError
import re


class DecNode(Node):

    def __init__(self):
        super().__init__()
        self.expression = [NEW, DECTYPE, LIST, ";"]
        self.type = None
        self.objects = []

    def parse(self, context):
        current_line = context.get_line()
        for exp in self.expression:
            token = context.pop()
            if token is None:
                raise ParseError("Invalid token at line {0}. Expected: {1} but received {2}."
                                 .format(current_line, exp, token))
            if re.match(exp, token) is None:
                raise ParseError("Invalid token at line {0}. Expected: {1} but received {2}."
                                 .format(current_line, exp, token))
            if re.match(DECTYPE, token):
                self.type = token         
            if re.match(LIST, token):
                objects = token.split(SEP)
                for o in objects:
                    if re.match(o, IDENTIFIER) is None:
                        raise ParseError("Invalid object at line {0}. '{1}' has incorrect format ".format(current_line, o))
                    else:
                        self.stores.push(o)
            

    def get_objects(self):
        if len(self.objects) == 0:
            return None
        else:
            return self.objects

    def get_decType(self):
        return self.type

    def compile(self):
        # TODO
        pass
