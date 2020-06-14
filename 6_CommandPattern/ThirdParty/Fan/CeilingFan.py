class CeilingFan :
    status = {
        'HIGH' : 3, 
        'MEDIUM' : 2, 
        'LOW' : 1, 
        'OFF' : 0
    }
    
    def __init__(self, location) :
        self.location = location
        self.speed = self.status['OFF']

    def high(self) :
        self.speed = self.status['HIGH']
        print('{} ceiling fan is on high'.format(self.location))

    def medium(self) :
        self.speed = self.status['MEDIUM']
        print('{} ceiling fan is on medium'.format(self.location))

    def low(self) :
        self.speed = self.status['LOW']
        print('{} ceiling fan is on low'.format(self.location))

    def off(self) :
        self.speed = self.status['OFF']
        print('{} ceiling fan is off'.format(self.location))
