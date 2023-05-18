#include <iostream>
#include "header/car_management.h"

using namespace std;

Car::Car(int carNo){
    this->carNo = carNo;
}

void Car::drive(int clientNo){
    cout << "\tClient " << clientNo << " is driving Car " << carNo << "." << endl;
}

int Car::getCarNo(){
    return carNo;
}

namespace{
    mutex car_manager_lock;
    CarManager *car_manager = nullptr;
}
CarManager *CarManager::getInstance(){
    if(car_manager == nullptr){
        lock_guard<mutex> lock(car_manager_lock);
        if(car_manager == nullptr){
            car_manager = new CarManager();
            car_manager->setCarNumber(1);
        }
    }
    
    return car_manager;
}

int CarManager::getCarNumber(){
    lock_guard<mutex> lock(this->instance_lock);
    return carNumber;
}

namespace{
    int car_manager_sequence = 0;
}
void CarManager::setCarNumber(int carNumber){
    if(carNumber >= 0){
        lock_guard<mutex> lock(this->instance_lock);
        if(carNumber > this->carNumber){
            for(int i = carNumber - this->carNumber; i > 0; i--){
                availableCar.push(new Car(car_manager_sequence++));
            }
        }else if(carNumber < this->carNumber){
            waitForDestroyed = this->carNumber - carNumber;
            while(waitForDestroyed && !availableCar.empty()){
                delete availableCar.front();
                availableCar.pop();
                waitForDestroyed--;
            }
        }
        this->carNumber = carNumber;
    }
}

int CarManager::getAvailableNumber(){
    lock_guard<mutex> lock(instance_lock);
    return availableCar.size();
}

Car *CarManager::rentCar(){
    lock_guard<mutex> lock(instance_lock);
    Car *car = nullptr;
    if(!availableCar.empty()){
        car = availableCar.front();
        availableCar.pop();
        dispatchedCar.insert(car);
    }

    return car;
}

Car *CarManager::returnCar(Car *car){
    if(car != nullptr){
        lock_guard<mutex> lock(instance_lock);
        if(dispatchedCar.erase(car)){
            if(waitForDestroyed){
                delete car;
                waitForDestroyed--;
            }else{
                availableCar.push(car);
            }
            car = nullptr;
        }
    }

    return car;
}

CarManager::CarManager() = default;