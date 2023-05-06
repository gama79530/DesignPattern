import abc
from enum import Enum

class PizzaType(Enum):
    CheesePizza = "cheese flavor pizza"
    PepperoniPizza = "pepperoni flavor pizza"
    VeggiePizza = "veggie flavor pizza"


class Pizza:
    def __init__(self, radius) -> None:
        self.radius = radius

    @property
    @abc.abstractmethod
    def price(self):
        return NotImplemented


class CheesePizza(Pizza):
    def __init__(self, radius) -> None:
        super().__init__(radius)

    @property
    def price(self):
        return (self.radius**2) * 10


class PepperoniPizza(Pizza):
    def __init__(self, radius) -> None:
        super().__init__(radius)

    @property
    def price(self):
        return (self.radius**2) * 20


class VeggiePizza(Pizza):
    def __init__(self, radius) -> None:
        super().__init__(radius)

    @property
    def price(self):
        return (self.radius**2) * 15


