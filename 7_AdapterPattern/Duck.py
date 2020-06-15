"""
    # All concrete classes should extend Duck and implement the following methods
    def quack(self) :
    def fly(self) :
"""

class Duck :
    def quack(self) :
        assert False, 'This method should be overrided.'

    def fly(self) :
        assert False, 'This method should be overrided.'

class MallardDuck(Duck) :
    def quack(self) :
        print('Quack')

    def fly(self) :
        print("I'm flying")
