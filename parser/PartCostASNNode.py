from Node import Node
from RecipePartNode import RecipePartNode
from Tokens import *
from Error import ParseError
import re

class PartCostASNNode(Node):

    def __init__(self):
        super().__init__()
        #                           RECIPEPARTS      PARTCOST 
        self.expression = [TO, BUY, LIST, YOU, NEED, NUMBER, DOLLARS]
        self.partcost = None

    def parse(self, context):
        current_line = context.getLine()
        for exp in self.expression:
            token = context.pop()
            if token is None:
                raise ParseError("Invalid token at line {0}. Expected: {1} but received {2}."
                                 .format(current_line, exp, token))
            if re.match(exp, token) is None:
                raise ParseError("Invalid token at line {0}. Expected: {1} but received {2}."
                                 .format(current_line, exp, token))
            if re.match(LIST, token):
                r = new RecipePartNode()
                r.parse(context)
                self.children.push(r)
            if re.match(NUMBER, token):
                self.partcost = token
                
    def compile(self):
        # TODO
        pass