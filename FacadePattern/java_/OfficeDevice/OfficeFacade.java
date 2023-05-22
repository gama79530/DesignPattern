package FacadePattern.java_.OfficeDevice;

public class OfficeFacade {
    private Light light;
    private AirConditioner airConditioner;
    private WaterDispenser waterDispenser;

    public OfficeFacade(Light light, AirConditioner airConditioner, WaterDispenser waterDispenser) {
        this.light = light;
        this.airConditioner = airConditioner;
        this.waterDispenser = waterDispenser;
    }

    public boolean isAllDeviceOn(){
        return light.getIsOn() && airConditioner.getIsOn() && waterDispenser.getIsOn();
    }

    public void on(){
        light.on();
        airConditioner.on();
        waterDispenser.on();
    }

    public void off(){
        light.off();
        airConditioner.off();
        waterDispenser.off();
    }

    public int getBrightness(){
        return light.getBrightness();
    }

    public int getTemperature(){
        return airConditioner.getTemperature();
    }

    public void brightnessUp(){
        light.brightnessUp();
    }

    public void brightnessDown(){
        light.brightnessDown();
    }

    public void temperatureUp(){
        airConditioner.temperatureUp();
    }
    
    public void temperatureDown(){
        airConditioner.temperatureDown();
    }
}
