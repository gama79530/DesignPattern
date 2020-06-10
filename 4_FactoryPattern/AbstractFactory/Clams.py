"""
    # All classes should extend Clams and override the following methods
    def __str__(selt)
"""

class Clams :
    def __str__(self):
        assert False, 'This method should be overrided.'

class FreshClams(Clams) :
    def __str__(self) :
        return 'Fresh Clams from Long Island Sound'

class FrozenClams(Clams) :
    def __str__(self) :
        return 'Frozen Clams from Chesapeake Bay'