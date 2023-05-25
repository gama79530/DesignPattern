import abc

class Vehicle(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def description(self)-> str:
        return NotImplemented
    
    @property
    @abc.abstractmethod
    def licensePlateNumber(self)-> str:
        return NotImplemented
    
    @abc.abstractmethod
    def __str__(self) -> str:
        return NotImplemented
    

class Motorcycle(Vehicle):
    def __init__(self, description, licensePlateNumber) -> None:
        self._description = description
        self._licensePlateNumber = licensePlateNumber

    @property
    def description(self)-> str:
        return self._description
    
    @property
    def licensePlateNumber(self) -> str:
        return self._licensePlateNumber
    
    def __str__(self) -> str:
        return f"Motorcycle:{self._description}, license plate number: {self._licensePlateNumber}"
    

class Car(Vehicle):
    def __init__(self, description, licensePlateNumber) -> None:
        self._description = description
        self._licensePlateNumber = licensePlateNumber

    @property
    def description(self)-> str:
        return self._description
    
    @property
    def licensePlateNumber(self) -> str:
        return self._licensePlateNumber
    
    def __str__(self) -> str:
        return f"Car:{self._description}, license plate number: {self._licensePlateNumber}"
    

class Garage:
    def __init__(self) -> None:
        self._vehicles = list()

    def addVehicle(self, vehicle:Vehicle):
        self._vehicles.append(vehicle)

    def __iter__(self):
        return iter(self._vehicles)
    
