import abc

class PizzaStore(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def ingredientFactory(self):
        return NotImplemented
    
    @abc.abstractmethod
    def orderPizza(self):
        return NotImplemented
    

class PizzaStoreA(PizzaStore):
    def __init__(self) -> None:
        from . import IngredientFactory
        super().__init__()
        self._ingredientFactory = IngredientFactory.IngredientFactoryOfStoreA()
    
    @property
    def ingredientFactory(self):
        return self._ingredientFactory
    
    @ingredientFactory.setter
    def ingredientFactory(self, val):
        self._ingredientFactory = val
    
    def orderPizza(self, pizzaType):
        from . import Pizza
        if(pizzaType == Pizza.PizzaType.CHEESE_PIZZA):
            return Pizza.CheesePizzeOfStoreA(self._ingredientFactory)
    

class PizzaStoreB(PizzaStore):
    def __init__(self) -> None:
        from . import IngredientFactory
        super().__init__()
        self._ingredientFactory = IngredientFactory.IngredientFactoryOfStoreB()
    
    @property
    def ingredientFactory(self):
        return self._ingredientFactory
    
    @ingredientFactory.setter
    def ingredientFactory(self, val):
        self._ingredientFactory = val
    
    def orderPizza(self, pizzaType):
        from . import Pizza
        if(pizzaType == Pizza.PizzaType.CHEESE_PIZZA):
            return Pizza.CheesePizzeOfStoreB(self._ingredientFactory)
