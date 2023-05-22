from OfficeDevice import *

if __name__ == "__main__":
    light = Light()
    airConditioner = AirConditioner()
    waterDispenser = WaterDispenser()
    officeFacade = OfficeFacade(light, airConditioner, waterDispenser)
    officeFacade.on()
    officeFacade.brightnessUp()
    officeFacade.brightnessUp()
    officeFacade.temperatureDown()
    officeFacade.temperatureDown()
    officeFacade.temperatureDown()
    officeFacade.temperatureDown()
    officeFacade.temperatureDown()
    officeFacade.off()