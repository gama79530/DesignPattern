"""
    # All classes should extend Observer
"""
import Subject
import abc

class Observer(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def update(self, *args):
        pass

class CurrentConditionsDisplay(Observer) :
    def __init__(self):
        self._temperature = None
        self._humidity = None

    def update(self, *args) :
        if args[0] == 'PUSH':
            self.temperature = args[1][0]
            self.humidity = args[1][1]
        elif args[0] == 'PULL':
            self.temperature = args[1].temperature
            self.humidity = args[1].humidity

        self.display()

    def display(self) :
        print('Current conditions: {:.1f} F degrees and {:.1f} % humidity.'.format(self.temperature, self.humidity))

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, newTemperature):
        self.__temperature = newTemperature

    @temperature.deleter
    def temperature(self):
        del self.__temperature

    @property
    def humidity(self):
        return self.__humidity

    @humidity.setter
    def humidity(self, newHumidity):
        self.__humidity = newHumidity

    @humidity.deleter
    def humidity(self):
        del self.__humidity

class StatisticsDisplay(Observer) :
    def __init__(self) :
        self._temperatures = []
        self._avgTemperature = None
        self._maxTemperature = None
        self._minTemperature = None

    def update(self, *args) :
        if args[0] == 'PUSH':
            self._temperatures.append(args[1][0])
        elif args[0] == 'PULL':
            self._temperatures.append(args[1].temperature)
        import statistics
        self.avgTemperature = statistics.mean(self._temperatures)
        self.maxTemperature = max(self._temperatures)
        self.minTemperature = min(self._temperatures)
        self.display()

    def display(self) :
        print('Avg/Max/Min temperature = {:.1f} / {:.1f} / {:.1f}'.format(self.avgTemperature, self.maxTemperature, self.minTemperature))      
        
    @property
    def avgTemperature(self):
        return self._avgTemperature

    @avgTemperature.setter
    def avgTemperature(self, newAvgTemperature):
        self._avgTemperature = newAvgTemperature

    @avgTemperature.deleter
    def avgTemperature(self):
        del self._avgTemperature
    
    @property
    def maxTemperature(self):
        return self._maxTemperature

    @maxTemperature.setter
    def maxTemperature(self, newMaxTemperature):
        self._maxTemperature = newMaxTemperature

    @maxTemperature.deleter
    def maxTemperature(self):
        del self._maxTemperature

    @property
    def minTemperature(self):
        return self._minTemperature

    @minTemperature.setter
    def minTemperature(self, newMinTemperature):
        self._minTemperature = newMinTemperature

    @minTemperature.deleter
    def minTemperature(self):
        del self._minTemperature

class ForecastDisplay(Observer) :
    def __init__(self) :
        self._currentPressure = 0.0
        self._lastPressure = 0.0

    def update(self, *args) :
        self.lastPressure = self.currentPressure
        if args[0] == 'PUSH':
            self.current_pressure = args[1][2]
        elif args[0] == 'PULL':
            self.current_pressure = args[1].pressure
        self.display()

    def display(self) :
        forecast = 'Forecast : {}'
        if self.currentPressure > self.lastPressure :
            print(forecast.format('Improving weather on the way!'))
        elif self.currentPressure == self.lastPressure :
            print(forecast.format('More of the same'))
        else :
            print(forecast.format('Watch out for cooler, rainy weather'))

    @property
    def currentPressure(self):
        return self._currentPressure

    @currentPressure.setter
    def currentPressure(self, newCurrentPressure):
        self._currentPressure = newCurrentPressure

    @currentPressure.deleter
    def currentPressure(self):
        self._currentPressure = 0.0

    @property
    def lastPressure(self):
        return self._lastPressure

    @lastPressure.setter
    def lastPressure(self, newLastPressure):
        self._lastPressure = newLastPressure

    @lastPressure.deleter
    def lastPressure(self):
        self._lastPressure = 0.0
