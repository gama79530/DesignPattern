#ifndef VEHICLE_HEADER_INCLUDED
#define VEHICLE_HEADER_INCLUDED

#include <string>

using namespace std;

class Vehicle{
public:
    virtual string getDescription() = 0;
    virtual string getLicensePlateNumber() = 0;
    virtual string toString() = 0;
};

class Motorcycle: public Vehicle{
public:
    Motorcycle(string description, string licensePlateNumber);
    string getDescription();
    string getLicensePlateNumber();
    string toString();

private:
    string description;
    string licensePlateNumber;
};

class Car: public Vehicle{
public:
    Car(string description, string licensePlateNumber);
    string getDescription();
    string getLicensePlateNumber();
    string toString();

private:
    string description;
    string licensePlateNumber;
};

#endif
