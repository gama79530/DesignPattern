class PizzaStore :
    factory = None

    def __init__(self, factory):
        self.factory = factory

    def orderPizza(self, pizza_type) :
        pizza = self.factory.createPizza(pizza_type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza