"""
    All classes should extend Dough and override the following methods

    def __str__(selt)
"""

class Dough :
    def __str__(self):
        assert False, 'This method should be overrided.'

class ThickCrustDough(Dough) :
    def __str__(self):
        return 'ThickCrust style extra thick crust dough'

class ThinCrustDough(Dough) :
    def __str__(self):
        return 'Thin Crust Dough'
