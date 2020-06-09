"""
    # All classes should extend FlyBehavior and override the following or methods.
    def fly(self) :
"""
class FlyBehavior :
    def fly(self) :
        assert False, 'This method should be overrided.' 

class FlyWithWings(FlyBehavior) :
    def fly(self) :
        print('I\'m flying!')

class FlyNoWay(FlyBehavior) :
    def fly(self) :
        print('I can\'t fly.')

class FlyRocketPowered(FlyBehavior) :
    def fly(self) :
        print('I\'m flying with rocket!')