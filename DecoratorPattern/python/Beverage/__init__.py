import abc

class Beverage(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_price(self):
        return NotImplemented
    
    @abc.abstractmethod
    def get_cost(self):
        return NotImplemented
    
    @abc.abstractmethod
    def get_profit(self):
        return NotImplemented
