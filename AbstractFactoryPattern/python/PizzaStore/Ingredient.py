import abc

class Ingredient(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def getInfo(self):
        return NotImplemented
    
    
class Dough(Ingredient):
    pass


class ThickCrustDough(Ingredient):
    def getInfo(self):
        return "thick crust dough"
    

class ThinCrustDough(Ingredient):
    def getInfo(self):
        return "thin crust dough"
    
    
class Cheese(Ingredient):
    pass

    
class ReggianoCheese(Cheese):
    def getInfo(self):
        return "reggiano cheese"
    
    
class MozzarellaCheese(Cheese):
    def getInfo(self):
        return "mozzarella cheese"
    
    
class Pepperoni(Ingredient):
    pass

    
class SlicedPepperoni(Pepperoni):
    def getInfo(self):
        return "sliced pepperoni"

