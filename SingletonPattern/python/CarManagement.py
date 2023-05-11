import threading
import abc

class Car:
    def __init__(self, carNo) -> None:
        self._carNo = carNo

    def drive(self, clientNo):
        print(f"\tClient {clientNo} is driving Car {self._carNo}.")

    @property
    def carNo(self):
        return self._carNo


class CarManagerMeta(type):
    _carManager = None
    _lock = threading.Lock()
    
    def __call__(cls, *args, **kwargs):
        if cls._carManager is None:
            with cls._lock:
                if cls._carManager is None:
                    cls._carManager = super().__call__(*args, *kwargs)
                    cls._carManager.carNumber = 1
        
        return cls._carManager
    
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
    def carNumber(self, val:int):
        if val >= 0:
            @CarManagerMeta.synchronized
            def sync_block(self:CarManager):
                if val > self._carNumber:
                    for _ in range(val - self._carNumber):
                        self._availableCar.append(Car(CarManager._carSequence))
                        CarManager._carSequence += 1
                elif val < self._carNumber:
                    waitForDestroyed = self._carNumber - val
                    while waitForDestroyed and self._availableCar:
                        self._availableCar.pop(0)
                        waitForDestroyed -= 1
                self._carNumber = val

            sync_block(self)

    @CarManagerMeta.synchronized
    def getAvailableNumber(self) ->int:
        return len(self._availableCar)

    @CarManagerMeta.synchronized
    def rentCar(self) -> Car:
        car = self._availableCar.pop(0) if self._availableCar else None
        if car:
            self._dispatchedCar.add(car)

        return car
    

    def returnCar(self, car:Car) -> Car:
        if car:
            @CarManagerMeta.synchronized
            def sync_block(self:CarManager):
                nonlocal car
                if car in self._dispatchedCar:
                    self._dispatchedCar.remove(car)
                    if self._waitForDestroyed:
                        self._waitForDestroyed-= 1
                        car = None
                    else:
                        self._availableCar.append(car)

            sync_block(self)

        return car


