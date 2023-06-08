import abc

class Proxy(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def addBalanceAccount(self, balanceAccount:int):
        return NotImplemented
    
    @abc.abstractmethod
    def subtractBalanceAccount(self, balanceAccount:int):
        return NotImplemented
    
    @property
    @abc.abstractmethod
    def balanceAccount(self) -> int:
        return NotImplemented

