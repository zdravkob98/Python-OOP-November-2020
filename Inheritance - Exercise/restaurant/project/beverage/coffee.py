from project.beverage.hot_beverage import HotBeverage

class Coffee(HotBeverage):
    COFFEE_MILLILITERS = 50
    COFFEE_PRICE = 3.50

    def __init__(self, name, caffeine: float):
        super().__init__(name = name, price = self.COFFEE_PRICE, milliliters = self.COFFEE_MILLILITERS)
        self.__caffeine = caffeine


    @property
    def caffeine(self):
        return self.__caffeine