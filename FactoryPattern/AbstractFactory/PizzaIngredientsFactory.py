"""
    All classes should extend ChicagoPizzaIngredientFactory and override the following methods

    def createCheese(self) :
    def createClams(self) :
    def createDough(self) :
    def createPepperoni(self) :
    def createSauce(self) :
    def createVeggies(self) :

"""
import Cheese
import Clams
import Dough
import Pepperoni
import Sauce
import Veggies

class PizzaIngredientFactory :
    def createCheese(self) :
        assert False, 'This method should be overrided.'

    def createClams(self) :
        assert False, 'This method should be overrided.'

    def createDough(self) :
        assert False, 'This method should be overrided.'
    
    def createPepperoni(self) :
        assert False, 'This method should be overrided.'
    
    def createSauce(self) :
        assert False, 'This method should be overrided.'
    
    def createVeggies(self) :
        assert False, 'This method should be overrided.'

class ChicagoPizzaIngredientFactory(PizzaIngredientFactory) :
    def createCheese(self) :
        return Cheese.MozzarellaCheese()

    def createClams(self) :
        return Clams.FrozenClams()

    def createDough(self) :
        return Dough.ThickCrustDough()
    
    def createPepperoni(self) :
        return Pepperoni.SlicedPepperoni()
    
    def createSauce(self) :
        return Sauce.PlumTomatoSauce()
    
    def createVeggies(self) :
        return [Veggies.BlackOlives(), Veggies.Spinach(), Veggies.Eggplant()]
        

class NYPizzaIngredientFactory(PizzaIngredientFactory) :
    def createCheese(self) :
        return Cheese.ReggianoCheese()

    def createClams(self) :
        return Clams.FreshClams()

    def createDough(self) :
        return Dough.ThinCrustDough()
    
    def createPepperoni(self) :
        return Pepperoni.SlicedPepperoni()
    
    def createSauce(self) :
        return Sauce.MarinaraSauce()
    
    def createVeggies(self) :
        return [Veggies.Garlic(), Veggies.Onion(), Veggies.Mushroom(), Veggies.RedPepper()]