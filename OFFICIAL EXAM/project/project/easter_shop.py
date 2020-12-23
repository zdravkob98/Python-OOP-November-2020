class EasterShop:
    def __init__(self, name, chocolate_factory, egg_factory, paint_factory):
        self.name = name
        self.chocolate_factory = chocolate_factory
        self.egg_factory = egg_factory
        self.paint_factory = paint_factory
        self.storage = {}

    def add_chocolate_ingredient(self, type: str, quantity: int):
        self.chocolate_factory.add_ingredient(type, quantity)

    def add_egg_ingredient(self, type: str, quantity: int):
        self.egg_factory.add_ingredient(type, quantity)

    def add_paint_ingredient(self, type: str, quantity: int):
        self.paint_factory.add_ingredient(type, quantity)

    def make_chocolate(self, recipe: str):
        self.chocolate_factory.make_chocolate(recipe)
        if recipe in self.storage.keys():
            self.storage[recipe] += 1
        else:
            self.storage[recipe] = 1

    def paint_egg(self, color: str, egg_type: str):
        if egg_type in self.egg_factory.products and color in self.paint_factory.products:
            if self.egg_factory.products[egg_type] >= 1 and self.paint_factory.products[color] >= 1:
                product_name = f"{color} {egg_type}"
                if product_name not in self.storage:
                    self.storage[product_name] = 1
                else:
                    self.storage[product_name] += 1
                self.egg_factory.remove_ingredient(egg_type, 1)
                self.paint_factory.remove_ingredient(color, 1)
            else:
                raise ValueError("Invalid commands")
        else:
            raise ValueError("Invalid commands")

    def __repr__(self):
        result = []
        result.append(f'Shop name: {self.name}')
        result.append('Shop Storage:')
        for k, v in self.storage.items():
            result.append(f'{k}: {v}')

        return '\n'.join(result)
