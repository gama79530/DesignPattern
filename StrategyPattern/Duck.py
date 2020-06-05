"""
    All classes should extends Duck.
"""
import FlyBehavior
import QuackBehavior

class Duck :
    fly_behavior = None
    quack_behavior = None

    def perform_quack(self) :
        self.quack_behavior.quack()
    
    def perform_fly(self) :
        self.fly_behavior.fly()

    def swim(self) :
        print('All ducks float, even decoy!')

    def display(self) :
        assert(False, 'This is default Duck. You should override this method')
    

class MallardDuck(Duck) :
    def __init__(self) :
        self.quack_behavior = QuackBehavior.Quack()
        self.fly_behavior = FlyBehavior.FlyWithWings()

    def display(self) :
        print('I\'m a real Mallard duck.')
    
class ModelDuck(Duck) :
    def __init__(self) :
        self.fly_behavior = FlyBehavior.FlyNoWay()
        self.quack_behavior = QuackBehavior.Quack()

    def display(self) :
        print('I\'m a real model duck.')