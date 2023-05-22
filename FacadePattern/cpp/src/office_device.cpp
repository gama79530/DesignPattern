#include <iostream>
#include "header/office_device.h"

bool Light::getIsOn(){
    return isOn;
}

int Light::getBrightness(){
    return brightness;
}

void Light::on(){
    if(!isOn){
        isOn = true;
        cout << "Light is on." << endl;
    }
}

void Light::off(){
    if(isOn){
        isOn = false;
        cout << "Light is off." << endl;
    }
}

void Light::brightnessUp(){
    if(brightness >= Light_MAX_LEVEL || ++brightness == Light_MAX_LEVEL){
        cout << "The current brightness is maximum (level " << Light_MAX_LEVEL << ")." << endl;
    }else{
        cout << "The brightness is up (level " << brightness << ")." << endl;;
    }
}

void Light::brightnessDown(){
    if(brightness <= 1 || --brightness == 1){
        cout << "The current brightness is minimum (level 1)." << endl;
    }else{
        cout << "The brightness is down (level " << brightness << ")." << endl;
    }
}


bool AirConditioner::getIsOn(){
    return isOn;
}

int AirConditioner::getTemperature(){
    return temperature;
}

void AirConditioner::on(){
    if(!isOn){
        isOn = true;
        cout << "Air Conditioner is on." << endl;
    }
}

void AirConditioner::off(){
    if(isOn){
        isOn = false;
        cout << "Air Conditioner is off." << endl;
    }
}

void AirConditioner::temperatureUp(){
    if(temperature >= AIR_CONDITIONER_MAX_TEMPERATURE || ++temperature == AIR_CONDITIONER_MAX_TEMPERATURE){
        cout <<"The temperature is maximum (" << AIR_CONDITIONER_MAX_TEMPERATURE << " Celsius)." << endl;
    }else{
        cout << "The temperature is up (" << temperature << " Celsius)." << endl;
    }
}

void AirConditioner::temperatureDown(){
    if(temperature <= AIR_CONDITIONER_MIN_TEMPERATURE || --temperature == AIR_CONDITIONER_MIN_TEMPERATURE){
        cout <<"The temperature is minimum (" << AIR_CONDITIONER_MIN_TEMPERATURE << " Celsius)." << endl;
    }else{
        cout << "The temperature is down (" << temperature << " Celsius)." << endl;
    }
}


bool WaterDispenser::getIsOn(){
    return isOn;
}

void WaterDispenser::on(){
    if(!isOn){
        isOn = true;
        cout << "Water Dispenser is on." << endl;
    }
}

void WaterDispenser::off(){
    if(isOn){
        isOn = false;
        cout << "Water Dispenser is off." << endl;
    }
}


OfficeFacade::OfficeFacade(shared_ptr<Light> &light, shared_ptr<AirConditioner> &airConditioner, shared_ptr<WaterDispenser> &waterDispenser){
    this->light = light;
    this->airConditioner = airConditioner;
    this->waterDispenser = waterDispenser;
}

OfficeFacade::OfficeFacade(shared_ptr<Light> &&light, shared_ptr<AirConditioner> &&airConditioner, shared_ptr<WaterDispenser> &&waterDispenser){
    this->light = light;
    this->airConditioner = airConditioner;
    this->waterDispenser = waterDispenser;
}

bool OfficeFacade::isAllDeviceOn(){
    return light->getIsOn() && airConditioner->getIsOn() && waterDispenser->getIsOn();
}

void OfficeFacade::on(){
    light->on();
    airConditioner->on();
    waterDispenser->on();
}

void OfficeFacade::off(){
    light->off();
    airConditioner->off();
    waterDispenser->off();
}

int OfficeFacade::getBrightness(){
    return light->getBrightness();
}

int OfficeFacade::getTemperature(){
    return airConditioner->getTemperature();
}

void OfficeFacade::brightnessUp(){
    light->brightnessUp();
}

void OfficeFacade::brightnessDown(){
    light->brightnessDown();
}

void OfficeFacade::temperatureUp(){
    airConditioner->temperatureUp();
}

void OfficeFacade::temperatureDown(){
    airConditioner->temperatureDown();
}
