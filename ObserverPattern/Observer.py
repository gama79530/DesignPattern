"""
    All classes should extend Observer and override the following methods

    def update(self, subject=None) :


    All classes should implement the following methods (# Due to this scenario, not for this pattern)
    
    def display(self) : 
"""
import Subject

class Observer :
    def __init__(self, subject) :
        self.subject = subject
        subject.registerPushObserver(self)

    def update(self, subject=None) :
        assert False, 'This method should be overrided.'

class CurrentConditionsDisplay(Observer) :
    def update(self, subject=None) :
        if subject :
            self.temperature = subject.temperature
            self.humidity = subject.humidity
            self.display()
        else :
            temperature = self.subject.temperature
            humidity = self.subject.humidity

    def display(self) :
        print('Current conditions: {:.1f} F degrees and {:.1f} % humidity.'.format(self.temperature, self.humidity))


class StatisticsDisplay(Observer) :
    def __init__(self, subject) :
        super().__init__(subject)
        self.temperatures = []
        self.avg_temperature = None
        self.max_temperature = None
        self.min_temperature = None

    def update(self, subject=None) :
        if subject :
            self.temperatures.append(subject.temperature)
        else :
            self.temperatures.append(self.subject.temperature)
        import statistics
        self.avg_temperature = statistics.mean(self.temperatures)
        self.max_temperature = max(self.temperatures)
        self.min_temperature = min(self.temperatures)
        self.display()

    def display(self) :
        print('Avg/Max/Min temperature = {:.1f} / {:.1f} / {:.1f}'.format(self.avg_temperature, self.max_temperature, self.min_temperature))      
        
class ForecastDisplay(Observer) :
    def __init__(self, subject) :
        super().__init__(subject)
        self.current_pressure = 0.0
        self.last_pressure = 0.0

    def update(self, subject=None) :
        self.last_pressure = self.current_pressure
        if subject :
            self.current_pressure = subject.pressure
        else :
            self.current_pressure = self.subject.pressure
        self.display()

    def display(self) :
        forecast = 'Forecast : {}'
        if self.current_pressure > self.last_pressure :
            print(forecast.format('Improving weather on the way!'))
        elif self.current_pressure == self.last_pressure :
            print(forecast.format('More of the same'))
        else :
            print(forecast.format('Watch out for cooler, rainy weather'))