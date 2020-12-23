from project.factory.factory import Factory


class ChocolateFactory(Factory):
    def __init__(self, name: str, capacity: int):
        super().__init__(name, capacity)
        self.recipes = {}
        self.products = {}

    def add_ingredient(self, ingredient_type: str, quantity: int):
        if ingredient_type == "white chocolate" or ingredient_type == "dark chocolate" or ingredient_type == "milk chocolate" or ingredient_type == "sugar":
            if self.can_add(quantity):
                if ingredient_type in self.ingredients.keys():
                    self.ingredients[ingredient_type] += quantity
                else:
                    self.ingredients[ingredient_type] = quantity
            else:
                raise ValueError("Not enough space in factory")
        else:
            raise TypeError(f"Ingredient of type {ingredient_type} not allowed in {Factory.__class__.__name__}")

    def remove_ingredient (self, ingredient_type: str, quantity: int):
        if ingredient_type in self.ingredients.keys():
            if self.ingredients[ingredient_type] >= quantity:
                self.ingredients[ingredient_type] -= quantity
            else:
                raise ValueError("Ingredient quantity cannot be less than zero")
        else:
            raise KeyError("No such product in the factory")

    def add_recipe(self, recipe_name: str, recipe: dict):
        if recipe_name in self.recipes.keys():
            self.recipes[recipe_name] = recipe
        else:
            self.recipes[recipe_name] = recipe

    def make_chocolate(self, recipe_name: str):
        if recipe_name in self.recipes.keys():
            for p in self.recipes[recipe_name]:
                self.remove_ingredient(p, 1)
            if recipe_name in self.products:
                self.products[recipe_name] += 1
            else:
                self.products[recipe_name] = 1
        else:
            raise TypeError("No such recipe")

