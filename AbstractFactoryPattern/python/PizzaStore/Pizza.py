from enum import Enum
import abc
from .Ingredient import *

class PizzaType(Enum):
    CHEESE_PIZZA = 0


class Pizza(metaclass=abc.ABCMeta):
    def __init__(self, ingredients:list[Ingredient]) -> None:
        self.ingredients = ingredients

    @abc.abstractmethod
    def getName(self) -> str:
        return NotImplemented

    @abc.abstractmethod
    def showIngredients(self) -> str:
        return NotImplemented
    

class CheesePizza(Pizza):
    def __init__(self, cheese:Cheese, ingredients:list[Ingredient]) -> None:
        super().__init__(ingredients)
        self.cheese = cheese


class CheesePizzeOfStoreA(CheesePizza):
    def __init__(self, cheese:Cheese, ingredients:list[Ingredient]) -> None:
        super().__init__(cheese, ingredients)
        
    def getName(self) -> str:
        return "store A cheese pizze"
    
    def showIngredients(self) -> str:
        ingredientsStr = self.cheese.getInfo()
        for ingredient in self.ingredients:
            ingredientsStr += (", " + ingredient.getInfo())

        return ingredientsStr


class CheesePizzeOfStoreB(CheesePizza):
    def __init__(self, cheese:Cheese, ingredients:list[Ingredient]) -> None:
        super().__init__(cheese, ingredients)

    def getName(self) -> str:
        return "store B cheese pizze"    

    def showIngredients(self) -> str:
        ingredientsStr = self.cheese.getInfo()
        for ingredient in self.ingredients:
            ingredientsStr += (", " + ingredient.getInfo())

        return ingredientsStr


