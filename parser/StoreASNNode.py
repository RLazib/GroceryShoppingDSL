from Node import Node
from Tokens import *
from Error import ParseError
import re

class StoreASNNode(Node):

    def __init__(self):
        super().__init__()
        #                                 Ingredients     StoreName
        self.expression = [YOU, CAN, BUY, LIST, AT, IDENTIFIER]
        self.ingredients = []
        self.store = None

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
                if context.top() == AT:
                    # We are at Ingredients
                    ingredients = token.split(SEP)
                    for i in ingredients:
                        if re.match(IDENTIFIER, i) is None:
                           raise ParseError("Invalid ingredients at line {0}".)
                        else:
                            self.ingredients.push(i)
                else:
                    # We are at StoreName
                    self.store = token
                   
    
    def getIngredients(self):
        return self.ingredients

    def getStore(self):
        return self.store
    
    def compile(self):
        # TODO
        pass