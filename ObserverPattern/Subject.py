"""
    All classes should extends Subject.
"""

class Subject :
    pushObserver = []
    pullObserver = []

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
    temperature = None
    humidity = None
    pressure = None

    def simulateChange(self, temperature, humidity, pressure) :
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.hasChange()