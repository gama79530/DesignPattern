import abc
from .Ingredient import *

class IngredientFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def createDough(self) -> Dough:
        return NotImplemented
    
    @abc.abstractmethod
    def createCheese(self) -> Cheese:
        return NotImplemented
    
    @abc.abstractmethod
    def createPepperoni(self) -> Pepperoni:
        return NotImplemented
    

class IngredientFactoryOfStoreA(IngredientFactory):
    def createDough(self) -> Dough:
        return ThinCrustDough()
    
    def createCheese(self) -> Cheese:
        return ReggianoCheese()
    
    def createPepperoni(self) -> Pepperoni:
        return SlicedPepperoni()
    

class IngredientFactoryOfStoreB(IngredientFactory):
    def createDough(self) -> Dough:
        return ThickCrustDough()
    
    def createCheese(self) -> Cheese:
        return MozzarellaCheese()
    
    def createPepperoni(self) -> Pepperoni:
        return SlicedPepperoni()


