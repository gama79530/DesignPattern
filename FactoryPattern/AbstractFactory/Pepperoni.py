"""
    All classes should extend Pepperoni and override the following methods

    def __str__(selt)
"""

class Pepperoni :
    def __str__(self):
        assert False, 'This method should be overrided.'

class SlicedPepperoni(Pepperoni) :
    def __str__(self):
        return 'Sliced Pepperoni'