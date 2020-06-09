"""
    # All classes should extend Pizza.
"""
class Pizza :
    def __init__(self):
        self.name = None
        self.dough = None
        self.sauce = None
        self.toppings = None
        self.toppings = []

    def prepare(self) :
        print('Preparing {}'.format(self.name))

    def bake(self) :
        print('Baking {}'.format(self.name))

    def cut(self) :
        print('Cutting {}'.format(self.name))

    def box(self) :
        print('Boxing {}'.format(self.name))

    def __str__(self):
        result = "---- {} ----\n".format(self.name)
        result += ('{}\n'.format(self.dough))
        result += ('{}\n'.format(self.sauce))
        for topping in self.toppings :
            result += ('{}\n'.format(topping))
        return result

class CheesePizza(Pizza) :
    def __init__(self):
        super().__init__()
        self.name = "Cheese Pizza"
        self.dough = "Regular Crust"
        self.sauce = "Marinara Pizza Sauce"
        self.toppings.append("Fresh Mozzarella")
        self.toppings.append("Parmesan")

class ClamPizza(Pizza) :
    def __init__(self):
        super().__init__()
        self.name = "Clam Pizza"
        self.dough = "Thin crust"
        self.sauce = "White garlic sauce"
        self.toppings.append("Clams")
        self.toppings.append("Grated parmesan cheese")

class PepperoniPizza(Pizza) :
    def __init__(self):
        super().__init__()
        self.name = "Pepperoni Pizza"
        self.dough = "Crust"
        self.sauce = "Marinara sauce"
        self.toppings.add("Sliced Pepperoni")
        self.toppings.add("Sliced Onion")
        self.toppings.add("Grated parmesan cheese")

class VeggiePizza(Pizza) :
    def __init__(self):
        super().__init__()
        self.name = "Veggie Pizza"
        self.dough = "Crust"
        self.sauce = "Marinara sauce"
        self.toppings.append("Shredded mozzarella")
        self.toppings.append("Grated parmesan")
        self.toppings.append("Diced onion")
        self.toppings.append("Sliced mushrooms")
        self.toppings.append("Sliced red pepper")
        self.toppings.append("Sliced black olives")