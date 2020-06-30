"""
    # All classes should extend Duck.
"""
import FlyBehavior
import QuackBehavior
import abc

class Duck(metaclass=abc.ABCMeta) :
    def swim(self) :
        print('All ducks float, even decoy!')

    @abc.abstractmethod
    def display(self) :
        pass
        
class MallardDuck(Duck) :
    def __init__(self) :
        self.quack = QuackBehavior.quack
        self.fly = FlyBehavior.fly_with_wings

    def display(self) :
        print('I\'m a real Mallard duck.')
    
class ModelDuck(Duck) :
    def __init__(self) :
        self.quack = QuackBehavior.quack
        self.fly = FlyBehavior.fly_no_way

    def display(self) :
        print('I\'m a real model duck.')

