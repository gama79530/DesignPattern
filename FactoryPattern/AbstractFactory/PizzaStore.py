"""
    # All classes should extend PizzaStore and override the following methods
    def createPizza(self) :
"""
import PizzaIngredientsFactory
import Pizza

class PizzaStore :
    def createPizza(self, pizza_type) :
        assert False, 'This method should be overrided.'
        
    def orderPizza(self, pizza_type) :
        pizza = self.createPizza(pizza_type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

class ChicagoPizzaStore(PizzaStore) :
    def createPizza(self, pizza_type) :
        pizza = None
        ingredientFactory = PizzaIngredientsFactory.ChicagoPizzaIngredientFactory()
        if pizza_type == 'cheese' :
            pizza = Pizza.CheesePizza(ingredientFactory)
            pizza.name = 'Chicago Style Cheese Pizza'
        elif pizza_type == 'veggie' :
            pizza = Pizza.VeggiePizza(ingredientFactory)
            pizza.name = 'Chicago Style Veggie Pizza'
        elif pizza_type == 'clam' :
            pizza = Pizza.ClamPizza(ingredientFactory)
            pizza.name = 'Chicago Style Clam Pizza'
        elif pizza_type == 'pepperoni' :
            pizza = Pizza.PepperoniPizza(ingredientFactory)
            pizza.name = 'Chicago Style Pepperoni Pizza'
        return pizza

class NYPizzaStore(PizzaStore) :
    def createPizza(self, pizza_type) :
        pizza = None
        ingredientFactory = PizzaIngredientsFactory.NYPizzaIngredientFactory()
        if pizza_type == 'cheese' :
            pizza = Pizza.CheesePizza(ingredientFactory)
            pizza.name = 'New York Style Cheese Pizza'
        elif pizza_type == 'veggie' :
            pizza = Pizza.VeggiePizza(ingredientFactory)
            pizza.name = 'New York Style Veggie Pizza'
        elif pizza_type == 'clam' :
            pizza = Pizza.ClamPizza(ingredientFactory)
            pizza.name = 'New York Style Clam Pizza'
        elif pizza_type == 'pepperoni' :
            pizza = Pizza.PepperoniPizza(ingredientFactory)
            pizza.name = 'New York Style Pepperoni Pizza'
        return pizza