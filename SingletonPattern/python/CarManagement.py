import threading
import abc

class Car:
    def __init__(self, carNo) -> None:
        self.carNo = carNo

    def drive(self, clientNo):
        print(f"\tClient {clientNo} is driving Car {self.carNo}.")


class CarManagerMeta(type):
    _instance = None
    _lock = threading.Lock()
    
    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__call__(*args, *kwargs)
                    cls._instance.carNumber = 1
        
        return cls._instance
    
    @staticmethod
    def synchronized(func):
        def wrap(self, *args, **kwargs):
            with self._lock:
                return func(self, *args, **kwargs)
            
        return wrap


class CarManager(metaclass=CarManagerMeta):
    _carSequence = 0

    def __init__(self) -> None:
        self._carNumber = 0
        self._waitForDestroyed = 0
        self._availableCar = list()
        self._dispatchedCar = set()
        self._lock = threading.Lock()

    @property
    @CarManagerMeta.synchronized
    def carNumber(self):
        return self._carNumber

    @carNumber.setter
    @CarManagerMeta.synchronized
    def carNumber(self, val):
        if val >= 0:
            if val > self._carNumber:
                for _ in range(val - self._carNumber):
                    self._availableCar.append(Car(CarManager._carSequence))
                    CarManager._carSequence += 1

            elif val < self._carNumber:
                waitForDestroyed = self._carNumber - val
                while self._availableCar and waitForDestroyed:
                    self._availableCar.pop(0)
                    waitForDestroyed -= 1

            self._carNumber = val

    @CarManagerMeta.synchronized
    def getAvailableNumber(self) ->int:
        return len(self._availableCar)

    @CarManagerMeta.synchronized
    def rentCar(self) -> Car:
        car = self._availableCar.pop(0) if self._availableCar else None
        if car is not None:
            self._dispatchedCar.add(car)

        return car
    
    @CarManagerMeta.synchronized
    def returnCar(self, car:Car) -> None:
        if car in self._dispatchedCar:
            self._dispatchedCar.remove(car)
            if self._waitForDestroyed:
                self._waitForDestroyed-= 1
                del car
            else:
                self._availableCar.append(car)

