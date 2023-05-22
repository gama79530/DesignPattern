#ifndef OFFICE_DEVICE_HEADER_INCLUDED
#define OFFICE_DEVICE_HEADER_INCLUDED

#include <memory>

using namespace std;

namespace{
    int Light_MAX_LEVEL = 5;
    int AIR_CONDITIONER_MAX_TEMPERATURE = 30;
    int AIR_CONDITIONER_MIN_TEMPERATURE = 16;
}

class Light{
public:
    bool getIsOn();
    int getBrightness();
    void on();
    void off();
    void brightnessUp();
    void brightnessDown();

private:
    bool isOn = false;
    int brightness = 1;
};

class AirConditioner{
public:
    bool getIsOn();
    int getTemperature();
    void on();
    void off();
    void temperatureUp();
    void temperatureDown();

private:
    bool isOn = false;
    int temperature = AIR_CONDITIONER_MAX_TEMPERATURE;
};

class WaterDispenser{
public:
    bool getIsOn();
    void on();
    void off();

private:
    bool isOn = false;
};

class OfficeFacade{
public:
    OfficeFacade(shared_ptr<Light> &light, shared_ptr<AirConditioner> &airConditioner, shared_ptr<WaterDispenser> &waterDispenser);
    OfficeFacade(shared_ptr<Light> &&light, shared_ptr<AirConditioner> &&airConditioner, shared_ptr<WaterDispenser> &&waterDispenser);
    bool isAllDeviceOn();
    void on();
    void off();
    int getBrightness();
    int getTemperature();
    void brightnessUp();
    void brightnessDown();
    void temperatureUp();
    void temperatureDown();

private:
    shared_ptr<Light> light;
    shared_ptr<AirConditioner> airConditioner;
    shared_ptr<WaterDispenser> waterDispenser;
};

#endif