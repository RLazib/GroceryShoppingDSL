from Constants import *
from StoreASN import StoreASN
from PartCostASN import PartCostASN
from Tokenizer import get_tokenizer
from Utils import *

def parse_buy_statement():
    tokenizer = get_tokenizer()
    tokenizer.pop_and_check(CAN)
    tokenizer.pop_and_check(BUY)
    
    list = parse_list(AT)
    store_name = parse_name([END_OF_LINE, FOR])
    token = tokenizer.top()
    statement = None
    if token == END_OF_LINE:
        statement = StoreASN(list, store_name)
    elif token == FOR:
        statement = PartCostASN(list, store_name)
    
    if statement is None:
        raise ParseError("Invalid token at line {0}.".format(tokenizer.get_line()))

    statement.parse()
    return statement