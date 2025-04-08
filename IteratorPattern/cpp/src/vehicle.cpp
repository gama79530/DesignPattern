#include "vehicle.h"

Motorcycle::Motorcycle(string description, string licensePlateNumber)
{
    this->description = description;
    this->licensePlateNumber = licensePlateNumber;
}

string Motorcycle::getDescription()
{
    return description;
}

string Motorcycle::getLicensePlateNumber()
{
    return licensePlateNumber;
}

string Motorcycle::toString()
{
    return "Motorcycle:" + description + ", license plate number: " + licensePlateNumber;
}

Car::Car(string description, string licensePlateNumber)
{
    this->description = description;
    this->licensePlateNumber = licensePlateNumber;
}

string Car::getDescription()
{
    return description;
}

string Car::getLicensePlateNumber()
{
    return licensePlateNumber;
}

string Car::toString()
{
    return "Car:" + description + ", license plate number: " + licensePlateNumber;
}