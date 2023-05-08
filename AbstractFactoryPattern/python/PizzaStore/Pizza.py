from enum import Enum
import abc

class PizzaType(Enum):
    CHEESE_PIZZA = 0


class Pizza(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def getName(self):
        return NotImplemented

    @abc.abstractmethod
    def showIngredients(self):
        return NotImplemented
    

class CheesePizza(Pizza):
    pass


class CheesePizzeOfStoreA(CheesePizza):
    def __init__(self, ingredientFactory) -> None:
        self.ingredients = [ingredientFactory.createDough(),]
        self.cheese = ingredientFactory.createCheese()


    def getName(self):
        return "store A cheese pizze"
    
    
    def showIngredients(self):
        ingredientsStr = self.cheese.getInfo()
        for ingredient in self.ingredients:
            ingredientsStr += (", " + ingredient.getInfo())

        return ingredientsStr



class CheesePizzeOfStoreB(CheesePizza):
    def __init__(self, ingredientFactory) -> None:
        self.ingredients = [ingredientFactory.createDough(), ingredientFactory.createPepperoni()]
        self.cheese = ingredientFactory.createCheese()


    def getName(self):
        return "store B cheese pizze"
    

    def showIngredients(self):
        ingredientsStr = self.cheese.getInfo()
        for ingredient in self.ingredients:
            ingredientsStr += (", " + ingredient.getInfo())

        return ingredientsStr

