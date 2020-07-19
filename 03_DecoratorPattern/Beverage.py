"""
"""
import abc

class Beverage(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def description(self):
        pass

    @abc.abstractmethod
    def cost(self):
        pass
