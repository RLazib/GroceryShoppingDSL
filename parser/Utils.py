from Tokenizer import get_tokenizer
from Constants import *
from Error import ParseError

def parse_list(end_token):
    results = []
    tokenizer = get_tokenizer()
    
    while tokenizer.top() != end_token:
        full_identifier = parse_name([SEPARATOR, end_token])
        if tokenizer.top() == SEPARATOR:
            tokenizer.pop()
        if full_identifier:
            results.append(full_identifier)
    return results
    
def parse_name(end_tokens):
    full_identifier = ""
    tokenizer = get_tokenizer()
    while tokenizer.has_next() and tokenizer.top() not in end_tokens:
        full_identifier += tokenizer.pop()
    if not tokenizer.has_next():
        raise ParseError("Expected one of the following tokens {0} at line {1}."
                        .format(end_tokens, tokenizer.get_line()))
    return full_identifier
    