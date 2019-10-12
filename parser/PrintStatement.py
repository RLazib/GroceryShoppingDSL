from Statement import Statement
from Utils import parse_name
from Use import Use
from MinCost import MinCost
from Constants import *
import json

class PrintStatement(Statement):
    def __init__(self):
        super().__init__()
        self.name = ""

    def parse(self):
        self.tokenizer.pop_and_check(PRINT)
        if self.tokenizer.top() == CHEAPEST:
            self.min_cost = MinCost()
            self.min_cost.parse()
        else:
            self.name = Use(parse_name([END_OF_LINE]))
        self.tokenizer.pop_and_check(END_OF_LINE)
            
    def evaluate(self):
        if self.name:
            name = self.name.evaluate()
            entry = self.symbol_table.get(name)
            self.output.write("{0}: ".format(name))
            if entry.value is None:
                self.output.write(name)
            else:
                self.output.write(json.dumps(entry.value))
        else:
            min_cost = self.min_cost.evaluate()
            ingredient_stores = min_cost[2]
            stores_string = ", ".join(["{0} at {1}".format(i, ingredient_stores[i]) for i in ingredient_stores])
            self.output.write("The cheapest way to make {0} is by buying {1}. ".format(min_cost[0], stores_string))
            
            self.output.write("The total cost is {0}. ".format(min_cost[1]))
            if len(min_cost[3]) > 0:
                self.output.write("No prices were found for the following ingredients: {0}."
                                    .format(", ".join(min_cost[3])))
            
        self.output.write("\n")
     