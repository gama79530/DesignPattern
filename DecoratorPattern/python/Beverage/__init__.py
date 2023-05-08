import abc

class Beverage(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def getPrice(self):
        return NotImplemented
    
    @abc.abstractmethod
    def getCost(self):
        return NotImplemented
    
    def getProfit(self):
        return self.getPrice() - self.getCost()


