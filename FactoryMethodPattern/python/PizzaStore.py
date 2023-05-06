import abc
import Pizza

class PizzaStore:
    @abc.abstractmethod
    def createPizza(self, type:Pizza.PizzaType, radius:int) -> Pizza.Pizza:
        return NotImplemented
    
    def orderPizza(self, type:Pizza.PizzaType, radius:int) -> None:
        pizza = self.createPizza(type, radius)
        if pizza is None:
            print(f"The {type.value} is not provided !!!")
        else:
            print(f"The {type.value} is provided. The radius of pizza is {radius} and the price of pizza is {pizza.price}")

class PizzaStoreA(PizzaStore):
    def createPizza(self, type:Pizza.PizzaType, radius:int) -> Pizza.Pizza:
        if type == Pizza.PizzaType.CheesePizza:
            return Pizza.CheesePizza(radius)
        elif type == Pizza.PizzaType.PepperoniPizza:
            return Pizza.PepperoniPizza(radius)
        else:
            return None
    

class PizzaStoreB(PizzaStore):
    def createPizza(self, type:Pizza.PizzaType, radius:int) -> Pizza.Pizza:
        if type == Pizza.PizzaType.CheesePizza:
            return Pizza.CheesePizza(radius)
        elif type == Pizza.PizzaType.VeggiePizza:
            return Pizza.VeggiePizza(radius)
        else:
            return None
        

