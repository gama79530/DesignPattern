"""
    All classes should extend Pizza and override the following methods

    def prepare(self) :
"""

class Pizza :
    name = None
    ingredient_factory = None
    
    cheese = None
    clams = None
    dough = None
    pepperoni = None
    sauce = None
    veggies = None
    
    def __init__(self, ingredient_factory) :
        self.ingredient_factory = ingredient_factory
    
    def prepare(self) :
        assert False, 'This method should be overrided.'

    def bake(self) :
        print('Bake for 25 minutes at 350.')

    def cut(self) :
        print('Cutting the pizza into diagonal slices.')

    def box(self) :
        print('Place pizza in official PizzaStore box.')

    def __str__(self) :
        result = '---- {} ----\n'.format(self.name)
        if self.dough :
            result += ('{}\n'.format(str(self.dough)))
        if self.sauce :
            result += ('{}\n'.format(str(self.sauce)))
        if self.cheese :
            result += ('{}\n'.format(str(self.cheese)))
        if self.veggies :
            for i, veggie in enumerate(self.veggies) :
                if i :
                    result += (',{}'.format(str(veggie)))
                else :
                    result += str(veggie)
            result += '\n'
        if self.clams :
            result += ('{}\n'.format(str(self.clams)))
        if self.pepperoni :
            result += ('{}\n'.format(str(self.pepperoni)))
        return result

class CheesePizza(Pizza) :
    def prepare(self) :
        print('Preparing {}'.format(self.name))
        self.dough = self.ingredient_factory.createDough()
        self.sauce = self.ingredient_factory.createSauce()
        self.cheese = self.ingredient_factory.createCheese()

class ClamPizza(Pizza) :
    def prepare(self) :
        print('Preparing {}'.format(self.name))
        self.dough = self.ingredient_factory.createDough()
        self.sauce = self.ingredient_factory.createSauce()
        self.cheese = self.ingredient_factory.createCheese()
        self.clams = self.ingredient_factory.createClams()

class PepperoniPizza(Pizza) :
    def prepare(self) :
        print('Preparing {}'.format(self.name))
        self.dough = self.ingredient_factory.createDough()
        self.sauce = self.ingredient_factory.createSauce()
        self.cheese = self.ingredient_factory.createCheese()
        self.veggies = self.ingredient_factory.createVeggies()
        self.pepperoni = self.ingredient_factory.createPepperoni()

class VeggiePizza(Pizza) :
    def prepare(self) :
        print('Preparing {}'.format(self.name))
        self.dough = self.ingredient_factory.createDough()
        self.sauce = self.ingredient_factory.createSauce()
        self.cheese = self.ingredient_factory.createCheese()
        self.veggies = self.ingredient_factory.createVeggies()