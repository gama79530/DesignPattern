import Command
class CeilingFanCommand(Command.Command) :
    def __init__(self, ceiling_fan) :
        self.ceiling_fan = ceiling_fan
        self.prev_speed = self.ceiling_fan.status['OFF']

    def undo(self) :
        if self.prev_speed == self.ceiling_fan.status['HIGH'] :
            self.ceiling_fan.high()
        elif self.prev_speed == self.ceiling_fan.status['MEDIUM'] :
            self.ceiling_fan.medium()
        elif self.prev_speed == self.ceiling_fan.status['LOW'] :
            self.ceiling_fan.low()
        elif self.prev_speed == self.ceiling_fan.status['OFF'] :
            self.ceiling_fan.off()

class CeilingFanHighCommand(CeilingFanCommand) :
    def execute(self) :
        self.prev_speed = self.ceiling_fan.speed
        self.ceiling_fan.high()

class CeilingFanLowCommand(CeilingFanCommand) :
    def execute(self) :
        self.prev_speed = self.ceiling_fan.speed
        self.ceiling_fan.low()

class CeilingFanMediumCommand(CeilingFanCommand) :
    def execute(self) :
        self.prev_speed = self.ceiling_fan.speed
        self.ceiling_fan.medium()

class CeilingFanOffCommand(CeilingFanCommand) :
    def execute(self) :
        self.prev_speed = self.ceiling_fan.speed
        self.ceiling_fan.off()
