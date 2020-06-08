"""
    All classes should extend Sauce and override the following methods

    def __str__(selt)
"""

class Sauce :
    def __str__(self):
        assert False, 'This method should be overrided.'

class MarinaraSauce(Sauce) :
    def __str__(self):
        return 'Marinara Sauce'

class PlumTomatoSauce(Sauce) :
    def __str__(self):
        return 'Tomato sauce with plum tomatoes'