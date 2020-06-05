"""
    All classes should extends Duck.
"""
import FlyBehavior
import QuackBehavior

class Duck :
    flyBehavior = None
    quackBehavior = None

    def performQuack(self) :
        self.quackBehavior.quack()
    
    def performFly(self) :
        self.flyBehavior.fly()

    def swim(self) :
        print('All ducks float, even decoy!')

    def display(self) :
        assert(False, 'This is default Duck. You should override this method')
    

class MallardDuck(Duck) :
    def __init__(self) :
        self.quackBehavior = QuackBehavior.Quack()
        self.flyBehavior = FlyBehavior.FlyWithWings()

    def display(self) :
        print('I\'m a real Mallard duck.')
    
class ModelDuck(Duck) :
    def __init__(self) :
        self.flyBehavior = FlyBehavior.FlyNoWay()
        self.quackBehavior = QuackBehavior.Quack()

    def display(self) :
        print('I\'m a real model duck.')