from Constants import *
from DecStatementParser import parse_dec_statement
from ASNStatementParser import parse_asn_statement
from ProcCall import ProcCall
from PrintStatement import PrintStatement
from Tokenizer import get_tokenizer
from Error import ParseError

def parse_statement():
    tokenizer = get_tokenizer()
    token = tokenizer.top()
    if token == NEW:
        return parse_dec_statement()
    if token == YOU:
        return parse_asn_statement()
    if token == CALL:
        statement = ProcCall()
        statement.parse()
        return statement
    if token == PRINT:
        statement = PrintStatement()
        statement.parse()
        return statement
        
    raise ParseError("Invalid token {0} at line {1}.".format(token, tokenizer.get_line()))
    