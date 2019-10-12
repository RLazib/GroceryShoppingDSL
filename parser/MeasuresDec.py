from DecStatement import DecStatement
from Constants import *

class MeasuresDec(DecStatement):
    def get_dec_token(self):
        return MEASUREMENTS
            
    def get_dec_type(self):
        return Type.MEASUREMENT
        