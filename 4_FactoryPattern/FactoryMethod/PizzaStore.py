"""
    # All classes should extend PizzaStore and override the following methods
    def createPizza(self) :
"""
import Pizza

class PizzaStore :
    def createPizza(self, pizza_type) :
        assert False, 'This method should be overrided.'

    def orderPizza(self, pizza_type) :
        pizza = self.createPizza(pizza_type)
        print('--- Making a {} ---'.format(pizza.name))
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

class ChicagoPizzaStore(PizzaStore) :
    def createPizza(self, pizza_type) :
        if pizza_type == 'cheese' :
            return Pizza.ChicagoStyleCheesePizza()
        elif pizza_type == 'veggie' :
            return Pizza.ChicagoStyleVeggiePizza()
        elif pizza_type == 'clam' :
            return Pizza.ChicagoStyleClamPizza()
        elif pizza_type == 'pepperoni' :
            return Pizza.ChicagoStylePepperoniPizza()

class NYPizzaStore(PizzaStore) :
    def createPizza(self, pizza_type) :
        if pizza_type == 'cheese' :
            return Pizza.NYStyleCheesePizza()
        elif pizza_type == 'veggie' :
            return Pizza.NYStyleVeggiePizza()
        elif pizza_type == 'clam' :
            return Pizza.NYStyleClamPizza()
        elif pizza_type == 'pepperoni' :
            return Pizza.NYStylePepperoniPizza()