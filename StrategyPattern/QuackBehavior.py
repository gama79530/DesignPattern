"""
    All classes should extend FlyBehavior and override the following methods.

    def quack(self) :
"""

class QuackBehavior :
    def quack(self) :
        assert False, 'This method should be overrided.' 

class Quack(QuackBehavior) :
    def quack(self) :
        print('Quack!')

class Squack(QuackBehavior) :
    def quack(self) :
        print('Squack!')

class MuteQuack(QuackBehavior) :
    def quack(self) :
        print('<<Silence>>!')