"""
    # All concrete classes should extend Turkey and implement the following methods
    def gobble(self) :
    def fly(self) :
"""

class Turkey :
    def gobble(self) :
        assert False, 'This method should be overrided.'

    def fly(self) :
        assert False, 'This method should be overrided.'

class WildTurkey(Turkey) :
    def gobble(self) :
        print('Gobble gobble')

    def fly(self) :
        print("I'm flying a short distance")
