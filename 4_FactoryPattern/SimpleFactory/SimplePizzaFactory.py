import Pizza

class SimplePizzaFactory :
    def createPizza(self, pizza_type) :
        pizza = None
        if pizza_type == 'cheese' :
            pizza = Pizza.CheesePizza()
        elif pizza_type == "pepperoni" :
            pizza = Pizza.PepperoniPizza()
        elif pizza_type == "clam" :
            pizza = Pizza.ClamPizza()
        elif pizza_type == "veggie" :
            pizza = Pizza.VeggiePizza()
        return pizza