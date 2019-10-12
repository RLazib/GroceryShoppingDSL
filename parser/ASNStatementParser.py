from Constants import *
from RecipeASN import RecipeASN
from BuyStatementParser import parse_buy_statement
from Tokenizer import get_tokenizer
from Error import ParseError

def parse_asn_statement():
    tokenizer = get_tokenizer()
    tokenizer.pop_and_check(YOU)
    token = tokenizer.top()
    if token == MAKE:
        statement = RecipeASN()
        statement.parse()
        return statement
    elif token == CAN:
        return parse_buy_statement()

    raise ParseError("Invalid token at line {0}.".format(tokenizer.get_line()))