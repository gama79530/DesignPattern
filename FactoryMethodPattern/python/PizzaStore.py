import abc
from enum import Enum

class PizzaType(Enum):
    CHEESE_PIZZA = "cheese flavor pizza"
    PEPPERONI_PIZZA = "pepperoni flavor pizza"
    VEGGIE_PIZZA = "veggie flavor pizza"


class Pizza:
    def __init__(self, radius:int) -> None:
        self._radius = radius

    @property
    @abc.abstractmethod
    def price(self) -> int:
        return NotImplemented
    
    @property
    def radius(self) -> int:
        return self._radius


class CheesePizza(Pizza):
    def __init__(self, radius) -> None:
        super().__init__(radius)

    @property
    def price(self):
        return (self._radius**2) * 10


class PepperoniPizza(Pizza):
    def __init__(self, radius) -> None:
        super().__init__(radius)

    @property
    def price(self):
        return (self._radius**2) * 20


class VeggiePizza(Pizza):
    def __init__(self, radius) -> None:
        super().__init__(radius)

    @property
    def price(self):
        return (self._radius**2) * 15


class PizzaStore:
    @abc.abstractmethod
    def createPizza(self, type:PizzaType, radius:int) -> Pizza:
        return NotImplemented
    
    def orderPizza(self, pizzaType:PizzaType, radius:int) -> Pizza:
        pizza = self.createPizza(pizzaType, radius)
        if pizza:
            print(f"The {pizzaType.value} is provided. The radius of pizza is {radius} and the price of pizza is {pizza.price}")
        else:
            print(f"The {pizzaType.value} is not provided !!!")

        return pizza


class PizzaStoreA(PizzaStore):
    def createPizza(self, pizzaType:PizzaType, radius:int) -> Pizza:
        if pizzaType == PizzaType.CHEESE_PIZZA:
            return CheesePizza(radius)
        elif pizzaType == PizzaType.PEPPERONI_PIZZA:
            return PepperoniPizza(radius)
    

class PizzaStoreB(PizzaStore):
    def createPizza(self, pizzaType:PizzaType, radius:int) -> Pizza:
        if pizzaType == PizzaType.CHEESE_PIZZA:
            return CheesePizza(radius)
        elif pizzaType == PizzaType.VEGGIE_PIZZA:
            return VeggiePizza(radius)
        

