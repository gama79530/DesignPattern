from enum import Enum
import abc

class PizzaType(Enum):
    CHEESE_PIZZA = 0


class Pizza(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def ingredients(self):
        return NotImplemented

    @abc.abstractmethod
    def getName(self):
        return NotImplemented

    @abc.abstractmethod
    def showIngredients(self):
        return NotImplemented
    

class CheesePizza(Pizza):
    @property
    @abc.abstractmethod
    def cheese(self):
        return NotImplemented


class CheesePizzeOfStoreA(CheesePizza):
    def __init__(self, ingredientFactory) -> None:
        self._ingredients = [ingredientFactory.createDough(),]
        self._cheese = ingredientFactory.createCheese()

    @property
    def ingredients(self):
        return self._ingredients
    
    @ingredients.setter
    def ingredients(self, val):
        self._ingredients = val

    def getName(self):
        return "store A cheese pizze"
    
    def showIngredients(self):
        ingredientsStr = self._cheese.getInfo()
        for ingredient in self._ingredients:
            ingredientsStr += (", " + ingredient.getInfo())

        return ingredientsStr
    
    @property
    def cheese(self):
        return self._cheese
    
    @cheese.setter
    def cheese(self, val):
        self._cheese = val



class CheesePizzeOfStoreB(CheesePizza):
    def __init__(self, ingredientFactory) -> None:
        self._ingredients = [ingredientFactory.createDough(), ingredientFactory.createPepperoni()]
        self._cheese = ingredientFactory.createCheese()

    @property
    def ingredients(self):
        return self._ingredients
    
    @ingredients.setter
    def ingredients(self, val):
        self._ingredients = val

    def getName(self):
        return "store B cheese pizze"
    
    def showIngredients(self):
        ingredientsStr = self._cheese.getInfo()
        for ingredient in self._ingredients:
            ingredientsStr += (", " + ingredient.getInfo())

        return ingredientsStr
    
    @property
    def cheese(self):
        return self._cheese
    
    @cheese.setter
    def cheese(self, val):
        self._cheese = val

