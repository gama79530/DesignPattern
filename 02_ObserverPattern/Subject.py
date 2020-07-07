"""
    # All classes should extend Subject.
"""
import abc

class Subject(metaclass=abc.ABCMeta) :
    def __init__(self):
        self._pushObservers = []
        self._pullObservers = []

    def registerPushObserver(self, observer) :
        self._pushObservers.append(observer)

    def removePushObserver(self, observer) :
        try :
            self._pushObservers.remove(observer)
        except ValueError :
            pass

    def registerPullObserver(self, observer) :
        self._pullObservers.append(observer)

    def removePullObserver(self, observer) :
        try :
            self._pullObservers.remove(observer)
        except ValueError :
            pass

    @abc.abstractmethod
    def notifyPushObserver(self):
        pass

    def notifyPullObserver(self):
        for observer in self._pullObservers:
            observer.update('PULL', self)

    def notifyObserver(self) :
        self.notifyPushObserver()
        self.notifyPullObserver()

    def hasChange(self) :
        self.notifyObserver()

class WeatherData(Subject) :
    def __init__(self):
        super().__init__()
        self._temperature = None
        self._humidity = None
        self._pressure = None
            
    def simulateChange(self, newTemperature, newHumidity, newPressure) :
        self.temperature = newTemperature
        self.humidity = newHumidity
        self.pressure = newPressure
        self.hasChange()

    def notifyPushObserver(self):
        data = [self.temperature, self.humidity, self.pressure]
        for observer in self._pushObservers:
            observer.update('PUSH', data)

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, newTemperature):
        self._temperature = newTemperature

    @temperature.deleter
    def temperature(self):
        del self._temperature

    @property
    def humidity(self):
        return self._humidity

    @humidity.setter
    def humidity(self, newHumidity):
        self._humidity = newHumidity

    @humidity.deleter
    def humidity(self):
        del self._humidity

    @property
    def pressure(self):
        return self._pressure

    @pressure.setter
    def pressure(self, newPressure):
        self._pressure = newPressure

    @pressure.deleter
    def pressure(self):
        del self._pressure
