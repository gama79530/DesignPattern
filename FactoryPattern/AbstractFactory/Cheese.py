"""
    All classes should extend Cheese and override the following methods

    def __str__(selt)
"""

class Cheese :
    def __str__(self) :
        assert False, 'This method should be overrided.'

class MozzarellaCheese(Cheese) :
    def __str__(self) :
        return 'Shredded Mozzarella'

class ParmesanCheese(Cheese) :
    def __str__(self) :
        return 'Shredded Parmesan'

class ReggianoCheese(Cheese) :
    def __str__(self) :
        return 'Reggiano Cheese'
