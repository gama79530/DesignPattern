import abc
from enum import Enum

class PizzaType(Enum):
    CheesePizza = "cheese flavor pizza"
    PepperoniPizza = "pepperoni flavor pizza"
    VeggiePizza = "veggie flavor pizza"


class Pizza:
    def __init__(self, radius) -> None:
        self._radius = radius

    @property
    @abc.abstractmethod
    def price(self):
        return NotImplemented
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, val):
        self._radius = val


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


