#include "src/header/office_device.h"

int main(){
    shared_ptr<Light> light = make_shared<Light>();
    shared_ptr<AirConditioner> airConditioner = make_shared<AirConditioner>();
    shared_ptr<WaterDispenser> waterDispenser = make_shared<WaterDispenser>();
    OfficeFacade officeFacade(light, airConditioner, waterDispenser);
    officeFacade.on();
    officeFacade.brightnessUp();
    officeFacade.brightnessUp();
    officeFacade.temperatureDown();
    officeFacade.temperatureDown();
    officeFacade.temperatureDown();
    officeFacade.temperatureDown();
    officeFacade.temperatureDown();
    officeFacade.off();

    return 0;
}