"""
    # All classes should extend Veggies and override the following methods
    def __str__(selt)
"""

class Veggies :
    def __str__(self):
        assert False, 'This method should be overrided.'

class BlackOlives(Veggies) :
    def __str__(self):
        return 'Black Olives'
        
class Garlic(Veggies) :
    def __str__(self):
        return 'Garlic'

class Mushroom(Veggies) :
    def __str__(self):
        return 'Mushrooms'

class Onion(Veggies) :
    def __str__(self):
        return 'Onion'

class RedPepper(Veggies) :
    def __str__(self):
        return 'Red Pepper'

class Spinach(Veggies) :
    def __str__(self):
        return 'Spinach'

class Eggplant(Veggies) :
    def __str__(self):
        return 'Eggplant'