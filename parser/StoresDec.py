from DecStatement import DecStatement
from Constants import *

class StoresDec(DecStatement):
    def get_dec_token(self):
        return STORES
            
    def get_dec_type(self):
        return Type.STORE
        