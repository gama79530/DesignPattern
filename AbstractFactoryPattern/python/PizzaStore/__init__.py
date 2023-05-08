import abc

class PizzaStore(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def orderPizza(self):
        return NotImplemented
    

class PizzaStoreA(PizzaStore):
    def __init__(self) -> None:
        from . import IngredientFactory
        super().__init__()
        self.ingredientFactory = IngredientFactory.IngredientFactoryOfStoreA()
    
    
    def orderPizza(self, pizzaType):
        from . import Pizza
        if(pizzaType == Pizza.PizzaType.CHEESE_PIZZA):
            return Pizza.CheesePizzeOfStoreA(self.ingredientFactory)
    

class PizzaStoreB(PizzaStore):
    def __init__(self) -> None:
        from . import IngredientFactory
        super().__init__()
        self.ingredientFactory = IngredientFactory.IngredientFactoryOfStoreB()
    
    
    def orderPizza(self, pizzaType):
        from . import Pizza
        if(pizzaType == Pizza.PizzaType.CHEESE_PIZZA):
            return Pizza.CheesePizzeOfStoreB(self.ingredientFactory)


