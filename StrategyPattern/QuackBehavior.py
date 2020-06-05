"""
    All classes should implement the following methods

    1. def quack(self) :
"""

class Quack :
    def quack(self) :
        print('Quack!')

class Squack(Quack) :
    def quack(self) :
        print('Squack!')

class MuteQuack(Quack) :
    def quack(self) :
        print('<<Silence>>!')