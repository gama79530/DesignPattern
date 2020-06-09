"""
    # All classes should extend Subject.
"""

class Subject :
    def __init__(self):
        self.pushObserver = []
        self.pullObserver = []

    def registerPushObserver(self, observer) :
        self.pushObserver.append(observer)

    def removePushObserver(self, observer) :
        try :
            self.pushObserver.remove(observer)
        except ValueError :
            pass

    def registerPullObserver(self, observer) :
        self.pullObserver.append(observer)

    def removePullObserver(self, observer) :
        try :
            self.pullObserver.remove(observer)
        except ValueError :
            pass

    def notifyObserver(self) :
        for observer in self.pushObserver :
            observer.update(self)

        for observer in self.pullObserver :
            observer.update()

    def hasChange(self) :
        self.notifyObserver()

class WeatherData(Subject) :
    def __init__(self):
        super().__init__()
        self.temperature = None
        self.humidity = None
        self.pressure = None

    def simulateChange(self, temperature, humidity, pressure) :
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.hasChange()