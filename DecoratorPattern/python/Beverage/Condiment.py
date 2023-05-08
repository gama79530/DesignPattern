from . import Beverage

class Condiment(Beverage):
    def __init__(self, beverage:Beverage) -> None:
        self.beverage = beverage
    

class Milk(Condiment):
    def getPrice(self):
        return self.beverage.getPrice() + 10
    
    def getCost(self):
        return self.beverage.getCost() + 2


class Mocha(Condiment):
    def getPrice(self):
        return self.beverage.getPrice() + 15
    
    def getCost(self):
        return self.beverage.getCost() + 5
    