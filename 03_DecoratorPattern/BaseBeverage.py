import abc
from Beverage import Beverage

class BaseBeverage(Beverage):
    def __init__(self):
        self._description = None

    @property
    def description(self):
        return self._description

class Espresso(BaseBeverage):
    def __init__(self):
        self._description = 'Espresso'

    def cost(self) :
        return 1.99

class HouseBlend(BaseBeverage) :
    def __init__(self) :
        self._description = 'House Blend Coffee'

    def cost(self) :
        return 0.89

class DarkRoast(BaseBeverage) :
    def __init__(self) :
        self._description = 'Dark Roast Coffee'

    def cost(self) :
        return 0.99
        
class Decaf(BaseBeverage) :
    def __init__(self) :
        self._description = 'Decaf'

    def cost(self) :
        return 1.05
