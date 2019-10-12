from DecStatement import DecStatement
from Constants import *

class RecipesDec(DecStatement):
    def get_dec_token(self):
        return RECIPES
            
    def get_dec_type(self):
        return Type.RECIPE
        