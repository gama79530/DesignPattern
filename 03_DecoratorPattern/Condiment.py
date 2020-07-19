import abc
from Beverage import Beverage

class Condiment(Beverage) :
    def __init__(self, beverage) :
        self._beverage = beverage

    @property
    def beverage(self):
        return self._beverage

class Milk(Condiment) :
    @property
    def description(self) :
        return self.beverage.description + ', Milk'

    def cost(self) :
        return 0.1 + self.beverage.cost()

class Mocha(Condiment) :
    @property
    def description(self) :
        return self.beverage.description + ', Mocha'

    def cost(self) :
        return 0.2 + self.beverage.cost()

class Soy(Condiment) :
    @property
    def description(self) :
        return self.beverage.description + ', Soy'

    def cost(self) :
        return 0.15 + self.beverage.cost()
        
class Whip(Condiment) :
    @property
    def description(self) :
        return self.beverage.description + ', Whip'

    def cost(self) :
        return 0.1 + self.beverage.cost()