from .. import Beverage

class Coffee(Beverage):
    def get_profit(self):
        return self.get_price() - self.get_cost()

class DarkRoast(Coffee):
    def get_price(self):
        return 75
    
    def get_cost(self):
        return 15

class HouseBlend(Coffee):
    def get_price(self):
        return 50
    
    def get_cost(self):
        return 10