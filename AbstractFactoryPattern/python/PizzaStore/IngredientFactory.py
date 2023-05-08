import abc
from .Ingredient import *

class IngredientFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def createDough(self):
        return NotImplemented
    
    @abc.abstractmethod
    def createCheese(self):
        return NotImplemented
    
    @abc.abstractmethod
    def createPepperoni(self):
        return NotImplemented
    

class IngredientFactoryOfStoreA(IngredientFactory):
    def createDough(self):
        return ThinCrustDough()
    
    def createCheese(self):
        return ReggianoCheese()
    
    def createPepperoni(self):
        return SlicedPepperoni()
    

class IngredientFactoryOfStoreB(IngredientFactory):
    def createDough(self):
        return ThickCrustDough()
    
    def createCheese(self):
        return MozzarellaCheese()
    
    def createPepperoni(self):
        return SlicedPepperoni()


