"""
    # All classes should extend Duck.
"""
import FlyBehavior
import QuackBehavior
import abc

class Duck(metaclass=abc.ABCMeta) :
    @property
    def fly(self):
        return self._fly()

    @property.setter
    def fly(self, flyBehavior):
        self._fly = flyBehavior

    def quack(self):
        return self._quack()

    def swim(self) :
        print('All ducks float, even decoy!')

    @abc.abstractmethod
    def display(self) :
        pass
        
class MallardDuck(Duck) :
    # def __init__(self) :
    #     self._quack = QuackBehavior.quack
    #     self._fly = FlyBehavior.fly_with_wings

    def display(self) :
        print('I\'m a real Mallard duck.')
    
class ModelDuck(Duck) :
    def __init__(self) :
        self._quack = QuackBehavior.quack
        self._fly = FlyBehavior.fly_no_way

    def display(self) :
        print('I\'m a real model duck.')

# class Duck(metaclass=abc.ABCMeta) :
#     def __init__(self) :
#         self._quack = None
#         self._fly = None

#     def fly(self):
#         return self._fly()

#     def quack(self):
#         return self._quack()

#     def swim(self) :
#         print('All ducks float, even decoy!')

#     @abc.abstractmethod
#     def display(self) :
#         pass
        
# class MallardDuck(Duck) :
#     def __init__(self) :
#         self._quack = QuackBehavior.quack
#         self._fly = FlyBehavior.fly_with_wings

#     def display(self) :
#         print('I\'m a real Mallard duck.')
    
# class ModelDuck(Duck) :
#     def __init__(self) :
#         self._quack = QuackBehavior.quack
#         self._fly = FlyBehavior.fly_no_way

#     def display(self) :
#         print('I\'m a real model duck.')

