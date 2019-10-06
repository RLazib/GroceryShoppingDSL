from Node import Node
from Tokens import *
from Error import ParseError
import re


class MeasurementNode(Node):

    def __init__(self):
        super().__init__()
        self.expression = [NEW, MEASUREMENT, IDENTIFIER]
        self.measurement = None

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
            if re.match(IDENTIFIER, token):
                self.measurement = token

    def get_measurement(self):
        return self.measurement

    def compile(self):
        # Part of AST parsing?
        pass
