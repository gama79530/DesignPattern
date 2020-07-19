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
        
    def setFly(self, flyBehavior):
        def wrapper(*args, **kwargs):
            kwargs['self'] = self
            return flyBehavior(*args, **kwargs)
        self.fly = wrapper
        
    def setQuack(self, quackBehavior):
        def wrapper(*args, **kwargs):
            kwargs['self'] = self
            return quackBehavior(*args, **kwargs)
        self.quack = wrapper
        
class MallardDuck(Duck) :
    def __init__(self) :
        self.setFly(FlyBehavior.flyWithWings)
        self.setQuack(QuackBehavior.quack)

    def display(self) :
        print('I\'m a real Mallard duck.')
    
class ModelDuck(Duck) :
    def __init__(self) :
        self.setFly(FlyBehavior.flyNoWay)
        self.setQuack(QuackBehavior.quack)

    def display(self) :
        print('I\'m a real model duck.')
