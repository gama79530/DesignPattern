import abc

class State(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def hailed(self, taxi:'Taxi') -> 'State':
        return NotImplemented
    
    @abc.abstractmethod
    def drive(self, taxi:'Taxi') -> 'State':
        return NotImplemented
    
    @abc.abstractmethod
    def checkout(self, taxi:'Taxi') -> 'State':
        return NotImplemented
    

class OffDutyLights(State):
    def hailed(self, taxi: 'Taxi') -> State:
        print("\tPassenger board on the taxi.")
        return taxi._onDutyLight
    
    def drive(self, taxi: 'Taxi') -> State:
        print("\tNo passenger...")
        return self
    
    def checkout(self, taxi: 'Taxi') -> State:
        print("\tNo passenger...")
        return self
    

class OnDutyLight(State):
    def hailed(self, taxi: 'Taxi') -> State:
        print("\tAlready hailed.")
        return self
    
    def drive(self, taxi: 'Taxi') -> State:
        print("\tTake passenger to their destination.")
        return taxi._arrived
    
    def checkout(self, taxi: 'Taxi') -> State:
        print("\tThe passenger's destination is not arrived.")
        return self


class Arrived(State):
    def hailed(self, taxi: 'Taxi') -> State:
        print("\tAlready hailed.")
        return self
    
    def drive(self, taxi: 'Taxi') -> State:
        print("\tWe are at your destination.")
        return self
    
    def checkout(self, taxi: 'Taxi') -> State:
        print("\tCheckout the bill.")
        return taxi._offDutyLights
    

class Taxi:
    def __init__(self) -> None:
        self._offDutyLights = OffDutyLights()
        self._onDutyLight = OnDutyLight()
        self._arrived = Arrived()
        self._state = self._offDutyLights

    @property
    def state(self):
        return self._state
    
    def hailed(self):
        print("Someone hails the taxi.")
        previouState = self.state
        self._state = self._state.hailed(self)
        if previouState != self._state:
            self._state = self._state.drive(self)

    def checkout(self):
        print("The passenger checkout the bill.")
        self._state = self._state.checkout(self)