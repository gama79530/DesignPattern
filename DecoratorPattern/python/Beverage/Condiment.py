from . import Beverage

class Condiment(Beverage):
    def __init__(self, beverage:Beverage) -> None:
        super().__init__()
        self.beverage = beverage

    def get_profit(self):
        return self.get_price() - self.get_cost()
    

class Milk(Condiment):
    def get_price(self):
        return self.beverage.get_price() + 10
    
    def get_cost(self):
        return self.beverage.get_cost() + 2


class Mocha(Condiment):
    def get_price(self):
        return self.beverage.get_price() + 15
    
    def get_cost(self):
        return self.beverage.get_cost() + 5
    