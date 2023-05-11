#include <iostream>
#include "header/car_management.h"

using namespace std;


void Car::drive(int clientNo){
    cout << "\tClient " << clientNo << " is driving Car " << carNo << "." << endl;
}

CarManager* CarManager::getInstance(){
    if(carManager == nullptr){
        lock_guard<mutex> lock(static_lock);
        if(carManager == nullptr){
            carManager = new CarManager();
            carManager->setCarNumber(1);
        }
    }
    
    return carManager;
}

int CarManager::getCarNumber(){
    lock_guard<mutex> lock(this->instance_lock);
    return carNumber;
}

void CarManager::setCarNumber(int carNumber){
    if(carNumber >= 0){
        lock_guard<mutex> lock(this->instance_lock);
        if(carNumber > this->carNumber){
            for(int i = carNumber - this->carNumber; i > 0; i--){
                availableCar.push(new Car(carSequence++));
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

Car* CarManager::rentCar(){
    lock_guard<mutex> lock(instance_lock);
    Car *car = nullptr;
    if(!availableCar.empty()){
        car = availableCar.front();
        availableCar.pop();
        dispatchedCar.insert(car);
    }

    return car;
}

Car* CarManager::returnCar(Car* car){
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


int CarManager::carSequence = 0;
CarManager* CarManager::carManager = nullptr;
mutex CarManager::static_lock = mutex();
