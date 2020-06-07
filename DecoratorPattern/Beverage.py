"""
    All concrete classes should extend Beverage.

    All concrete classes should overide the following attributes.
    description = None

    All concrete classes should implement the following methods.
    def cost(self) :
"""
class Beverage :
    description = None

    def getDescription(self) :
        return self.description

class Espresso(Beverage) :
    description = 'Espresso'

    def cost(self) :
        return 1.99

class HouseBlend(Beverage) :
    description = 'House Blend Coffee'

    def cost(self) :
        return 0.89

class DarkRoast(Beverage) :
    description = 'Dark Roast Coffee'

    def cost(self) :
        return 0.99
        
class Decaf(Beverage) :
    description = 'Decaf'

    def cost(self) :
        return 1.05

"""
    All decorator classes should extend Condiment and override the following methods.
    def getDescription(self) :
    def cost(self) :
"""

class Condiment(Beverage) :
    beverage = None

    def __init__(self, beverage) :
        self.beverage = beverage

    def getDescription(self) :
        assert False, 'This method should be overrided.'

class Milk(Condiment) :
    def getDescription(self) :
        return self.beverage.getDescription() + ', Milk'

    def cost(self) :
        return 0.1 + self.beverage.cost()

class Mocha(Condiment) :
    def getDescription(self) :
        return self.beverage.getDescription() + ', Mocha'
        
    def cost(self) :
        return 0.2 + self.beverage.cost()

class Soy(Condiment) :
    def getDescription(self) :
        return self.beverage.getDescription() + ', Soy'
        
    def cost(self) :
        return 0.15 + self.beverage.cost()
        

class Whip(Condiment) :
    def getDescription(self) :
        return self.beverage.getDescription() + ', Whip'
        
    def cost(self) :
        return 0.1 + self.beverage.cost()