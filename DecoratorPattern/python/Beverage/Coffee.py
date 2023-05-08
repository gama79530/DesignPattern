from . import Beverage

class Coffee(Beverage):
    pass


class DarkRoast(Coffee):
    def getPrice(self):
        return 75
    
    def getCost(self):
        return 15


class HouseBlend(Coffee):
    def getPrice(self):
        return 50
    
    def getCost(self):
        return 10