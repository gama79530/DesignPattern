package FacadePattern.java_;
import FacadePattern.java_.OfficeDevice.*;

public class Main{
    public static void main(String[] args) {
        Light light = new Light();
        AirConditioner airConditioner = new AirConditioner();
        WaterDispenser waterDispenser = new WaterDispenser();
        OfficeFacade officeFacade = new OfficeFacade(light, airConditioner, waterDispenser);
        officeFacade.on();
        officeFacade.brightnessUp();
        officeFacade.brightnessUp();
        officeFacade.temperatureDown();
        officeFacade.temperatureDown();
        officeFacade.temperatureDown();
        officeFacade.temperatureDown();
        officeFacade.temperatureDown();
        officeFacade.off();
    }
}