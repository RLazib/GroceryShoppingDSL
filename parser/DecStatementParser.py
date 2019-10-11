from Constants import *
from IngredientsDec import IngredientsDec
from StoresDec import StoresDec
from MeasuresDec import MeasuresDec
from RecipesDec import RecipesDec
from Tokenizer import get_tokenizer
from Error import ParseError

def parse_dec_statement():
    tokenizer = get_tokenizer()
    tokenizer.pop_and_check(NEW)
    token = tokenizer.top()
    statement = None
    if token == INGREDIENTS:
        statement = IngredientsDec()
    elif token == STORES:
        statement = StoresDec()
    elif token == MEASUREMENTS:
        statement = MeasuresDec()
    elif token == RECIPES:
        statement = RecipesDec()

    if statement is None:
        raise ParseError("Invalid token at line {0}.".format(tokenizer.get_line()))

    statement.parse()
    return statement