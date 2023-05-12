import abc
from .Ingredient import *
from .IngredientFactory import *
from .Pizza import *

class PizzaStore(metaclass=abc.ABCMeta):
    def __init__(self, ingredientFactory:IngredientFactory) -> None:
        self.ingredientFactory = ingredientFactory

    @abc.abstractmethod
    def orderPizza(self) -> Pizza:
        return NotImplemented
    

class PizzaStoreA(PizzaStore):
    def __init__(self) -> None:
        super().__init__(IngredientFactoryOfStoreA())
    
    def orderPizza(self, pizzaType) -> Pizza:
        if(pizzaType == PizzaType.CHEESE_PIZZA):
            cheese = self.ingredientFactory.createCheese()
            ingredients = list()
            ingredients.append(self.ingredientFactory.createDough())
            
            return CheesePizzeOfStoreA(cheese, ingredients)
    

class PizzaStoreB(PizzaStore):
    def __init__(self) -> None:
        super().__init__(IngredientFactoryOfStoreB())
    
    def orderPizza(self, pizzaType) -> Pizza:
        if(pizzaType == PizzaType.CHEESE_PIZZA):
            cheese = self.ingredientFactory.createCheese()
            ingredients = list()
            ingredients.append(self.ingredientFactory.createDough())
            ingredients.append(self.ingredientFactory.createPepperoni())

            return CheesePizzeOfStoreB(cheese, ingredients)


