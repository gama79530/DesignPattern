import abc

class Beverage(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def getPrice(self) -> int:
        return NotImplemented
    
    @abc.abstractmethod
    def getCost(self) -> int:
        return NotImplemented
    
    def getProfit(self) -> int:
        return self.getPrice() - self.getCost()


class Coffee(Beverage):
    pass


class DarkRoast(Coffee):
    def getPrice(self) -> int:
        return 75
    
    def getCost(self) -> int:
        return 15


class HouseBlend(Coffee):
    def getPrice(self) -> int:
        return 50
    
    def getCost(self) -> int:
        return 10
    

class Condiment(Beverage):
    def __init__(self, beverage:Beverage) -> None:
        self._beverage = beverage

    @property
    def beverage(self) -> Beverage:
        return self._beverage

    
class Milk(Condiment):
    def getPrice(self):
        return self._beverage.getPrice() + 10
    
    def getCost(self):
        return self._beverage.getCost() + 2


class Mocha(Condiment):
    def getPrice(self) -> int:
        return self._beverage.getPrice() + 15
    
    def getCost(self) -> int:
        return self._beverage.getCost() + 5
    