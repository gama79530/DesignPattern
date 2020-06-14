class Light :
    def __init__(self, location) :
        self.location = location
        self.level = 0

    def on(self) :
        self.level = 100
        print("Light is on")

    def off(self) :
        self.level = 0
        print("Light is off")

    def dim(self, level) :
        self.level = level
        if self.level :
            print('Light is dimmed to {}%'.format(str(self.level)))
        else :
            self.off()