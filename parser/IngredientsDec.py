from DecStatement import DecStatement
from Constants import *

class IngredientsDec(DecStatement):
    def get_dec_token(self):
        return INGREDIENTS
            
    def get_dec_type(self):
        return Type.INGREDIENT
          