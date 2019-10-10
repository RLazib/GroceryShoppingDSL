from Node import Node
from Tokens import *
from Error import ParseError
import re

class RecipePartNode(Node):

    def __init__(self):
        super().__init__()
        #                          MeasureName     IngredientName
        self.expression = [NUMBER, IDENTIFIER, OF, IDENTIFIER]
        self.parts = {}

    def parse(self, context):
        current_line = context.getLine()
        # TODO        
    
    def compile(self):
        # TODO
        pass