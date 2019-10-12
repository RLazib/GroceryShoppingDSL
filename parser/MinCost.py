from Node import Node
from Use import Use
from Utils import parse_name
from Constants import *

class MinCost(Node):
    def parse(self):
        self.tokenizer.pop_and_check(CHEAPEST)
        self.tokenizer.pop_and_check(WAY)
        self.tokenizer.pop_and_check(TO)
        self.tokenizer.pop_and_check(MAKE)
        self.recipe_name = Use(parse_name([END_OF_LINE]))
    
    def evaluate(self):
        recipe_name = self.recipe_name.evaluate()
        recipe = self.symbol_table.get(recipe_name).value
        total = 0
        ingredient_stores = dict()
        missing_ingredients = []
        for ingredient in recipe:
            min_ingredient_cost = None
            min_store = None
            for store_name in self.symbol_table.get(ingredient).value:
                store = self.symbol_table.get(store_name).value
                if store[ingredient] and store[ingredient]["measurement"] == recipe[ingredient]["measurement"]:
                    ingredient_cost = store[ingredient]["unit cost"] * recipe[ingredient]["quantity"]
                    if min_ingredient_cost is None or ingredient_cost < min_ingredient_cost:
                        min_ingredient_cost = ingredient_cost
                        min_store = store_name
            if min_ingredient_cost is None:
                missing_ingredients.append(ingredient)
            else:
                total += min_ingredient_cost
                ingredient_stores[ingredient] = min_store
        return (recipe_name, total, ingredient_stores, missing_ingredients)