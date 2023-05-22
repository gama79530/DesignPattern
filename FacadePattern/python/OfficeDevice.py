class Light:
    _MAX_LEVEL:int = 5
    def __init__(self) -> None:
        self._isOn:bool = False
        self._brightness:int = 1

    @property
    def isOn(self) -> bool:
        return self._isOn()
    
    @property
    def brightness(self) -> int:
        return self._brightness
    
    def on(self):
        if not self._isOn:
            self._isOn = True
            print("Light is on.")

    def off(self):
        if self._isOn:
            self._isOn = False
            print("Light is off.")

    def brightnessUp(self):
        if self._brightness < Light._MAX_LEVEL:
            self._brightness += 1

        if self._brightness == Light._MAX_LEVEL:
            print(f"The brightness is maximum (level {Light._MAX_LEVEL}).")
        else:
            print(f"The brightness is up (level {self._brightness}).")

    def brightnessDown(self):
        if self._brightness > 1:
            self._brightness -= 1

        if self._brightness <= 1:
            print("The brightness is minimum (level 1).")
        else:
            print(f"The brightness is down (level {self._brightness}).")


class AirConditioner:
    _MAX_TEMPERATURE:int = 30
    _MIN_TEMPERATURE:int = 16

    def __init__(self) -> None:
        self._isOn:bool = False
        self._temperature:int = AirConditioner._MAX_TEMPERATURE

    @property
    def isOn(self) -> bool:
        return self._isOn()
    
    @property
    def temperature(self) -> int:
        return self._temperature
    
    def on(self):
        if not self._isOn:
            self._isOn = True
            print("Air Conditioner is on.")

    def off(self):
        if self._isOn:
            self._isOn = False
            print("Air Conditioner is off.")

    def temperatureUp(self):
        if self._temperature < AirConditioner._MAX_TEMPERATURE:
            self._temperature += 1

        if self._temperature == AirConditioner._MAX_TEMPERATURE:
            print(f"The temperature is maximum ({AirConditioner._MAX_TEMPERATURE} Celsius).")
        else:
            print(f"The temperature is up ({self.temperature} Celsius).")

    def temperatureDown(self):
        if self._temperature > AirConditioner._MIN_TEMPERATURE:
            self._temperature -= 1

        if self._temperature == AirConditioner._MIN_TEMPERATURE:
            print(f"The temperature is minimum ({AirConditioner._MIN_TEMPERATURE} Celsius).")
        else:
            print(f"The temperature is down ({self.temperature} Celsius).")


class WaterDispenser:
    def __init__(self) -> None:
        self._isOn:bool = False

    @property
    def isOn(self) -> bool:
        return self._isOn()
    
    def on(self):
        if not self._isOn:
            self._isOn = True
            print("Water Dispenser is on.")

    def off(self):
        if self._isOn:
            self._isOn = False
            print("Water Dispenser is off.")


class OfficeFacade:
    def __init__(self, light:Light, airConditioner:AirConditioner, waterDispenser:WaterDispenser) -> None:
        self._light = light
        self._airConditioner = airConditioner
        self._waterDispenser = waterDispenser

    def isAllDeviceOn(self):
        return self._light.isOn and self._airConditioner.isOn and self._waterDispenser.isOn
    
    def on(self):
        self._light.on()
        self._airConditioner.on()
        self._waterDispenser.on()
        
    def off(self):
        self._light.off()
        self._airConditioner.off()
        self._waterDispenser.off()

    @property
    def brightness(self) -> int:
        return self._light.brightness
    
    @property
    def temperature(self) -> int:
        return self._airConditioner.temperature
    
    def brightnessUp(self):
        self._light.brightnessUp()

    def brightnessDown(self):
        self._light.brightnessDown()

    def temperatureUp(self):
        self._airConditioner.temperatureUp()

    def temperatureDown(self):
        self._airConditioner.temperatureDown()