import abc

class Receiver(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def on(self) -> bool:
        return NotImplemented
    
    def off(self) -> bool:
        return NotImplemented
    

class Light(Receiver):
    def __init__(self) -> None:
        super().__init__()
        self._isOn = False

    def on(self) -> bool:
        if not self._isOn:
            print("Light on")
            self._isOn = True
            return True
        else:
            print("Light is already on.")
            return False

    def off(self) -> bool:
        if self._isOn:
            print("Light off")
            self._isOn = False
            return True
        else:
            print("Light is already off.")
            return False
        

class Fan(Receiver):
    _MAX_SPEED:int = 5
    
    def __init__(self) -> None:
        super().__init__()
        self._currentLevel:int = 0

    def on(self) -> bool:
        if self._currentLevel < Fan._MAX_SPEED:
            self._currentLevel += 1
            if self._currentLevel == Fan._MAX_SPEED:
                print(f"The speed of fan is max level (level {self._currentLevel})")
            else:
                print(f"The speed of fan is level {self._currentLevel}")
            
            return True
        else:
            print("The current level is already maximum.")
            return False

    def off(self) -> bool:
        if self._currentLevel > 0:
            self._currentLevel -= 1
            if self._currentLevel == 0:
                print(f"The fan is off")
            else:
                print(f"The speed of fan is level {self._currentLevel}")

            return True
        else:
            print("The fan is already off.")
            return False


