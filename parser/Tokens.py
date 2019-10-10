NEW = "new"

INGREDIENT = "ingredients"

STORE = "stores"

YOU = "you"

CAN = "can"

BUY = "buy"

AT = "at"

MEASUREMENT = "measurements"

TO = "to"

NEED = "need"

MAKE = "make"

DOLLARS = "dollars"

RECIPE = "recipes"

SEP = ","

# number with up to two decimal places
PRICE = "^\s*(?=.*[1-9])\d*(?:\.\d{1,2})?\s*$"

DECTYPE = "/^({0}|{1}|{2})$/".format(RECIPE, MEASUREMENT, INGREDIENT)

IDENTIFIER = "[_A-Za-z]+([A-Za-z0-9]*)"

LIST = "^[a-zA-Z0-9, ]*$"

NUMBER = "^[0-9]*$"

