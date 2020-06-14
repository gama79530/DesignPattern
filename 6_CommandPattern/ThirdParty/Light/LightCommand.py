import Command

class LightCommand(Command.Command) :    
    def __init__(self, light) :
        self.light = light
        self.prev_level = None
        
    def undo(self) :
        self.light.dim(self.prev_level)

class DimmerLightOffCommand(LightCommand) :
    def __init__(self, light) :
        self.light = light
    
    def execute(self) :
        self.prev_level = self.light.level
        self.level.off()

class DimmerLightOnCommand(LightCommand) :
    def __init__(self, light) :
        self.light = light
    
    def execute(self) :
        self.prev_level = self.light.level
        self.level.dim(75)

class LightOffCommand(LightCommand) :
    def __init__(self, light) :
        self.light = light
    
    def execute(self) :
        self.prev_level = self.light.level
        self.light.off()

class LightOnCommand(LightCommand) :
    def __init__(self, light) :
        self.light = light
    
    def execute(self) :
        self.prev_level = self.light.level
        self.light.on()
