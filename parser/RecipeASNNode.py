from Node import Node
from RecipePartNode import RecipePartNode
from Tokens import *
from Error import ParseError
import re

class RecipeASNNode(Node):

    def __init__(self):
        super().__init__()
        #                             RecipeParts       RecipeName
        self.expression = [YOU, NEED, LIST, TO, MAKE, IDENTIFIER]
        self.recipeName = None

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
            if re.match(LIST, token) and context.top() == TO:
                # Parse reciparts
                recipeParts = token.split(SEP)
                for r in reciparts:
                    if re.match(r, IDENTIFIER) is None:
                        raise ParseError("Invalid recipe part at line {0}."
                                 .format(current_line))
                    r = new RecipePartNode()
                    r.parse(context)
                    self.children.push(r)
            if re.match(IDENTIFIER, token):
                self.recipeName = token

    def get_recipeName():
        return self.recipeName
                
    
    def compile(self):
        # TODO
        pass