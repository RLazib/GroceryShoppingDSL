from enum import Enum

# literals
START = "start"
END = "end"
NEW = "new"
INGREDIENTS = "ingredients:"
STORES = "stores:"
MEASUREMENTS = "measurements:"
RECIPES = "recipes:"
YOU = "you"
CAN = "can"
GET = "get"
BUY = "buy"
AT = "at"
TO = "to"
NEED = "need"
MAKE = "make"
DOLLARS = "dollars"
FOR = "for"
WITH = "with"
PRINT = "print"
DEF = "def"
CALL = "call"
PROCSTART = "procstart"
PROCEND = "procend"
CHEAPEST = "cheapest"
WAY = "way"

# Types
class Type(Enum):
    INGREDIENT = "ingredient"
    STORE = "store"
    RECIPE = "recipe"
    MEASUREMENT = "measurement"
    PROC = "proc"
    PARAM = "param"

# special values
END_OF_LINE = ";"
SEPARATOR = ","
NUMBER_MATCHER = "^(\d+\.)?\d+$"
