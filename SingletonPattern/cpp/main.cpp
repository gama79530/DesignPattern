#include <iostream>
#include <thread>
#include <chrono> 
#include "src/header/car_management.h"

using namespace std;

void task(int clientNo){
    CarManager *carManager = CarManager::getInstance();
    string info = "\tClient " + to_string(clientNo) + " rent a car: ";
    Car *car = carManager->rentCar();
    info += (car == nullptr) ? "No available car" : ("car " + to_string(car->getCarNo()));
    cout << info << endl;
    if(car != nullptr){
        this_thread::sleep_for(chrono::microseconds(20));
        car->drive(clientNo);
        car = carManager->returnCar(car);
    }
}

int main(){
    thread clients[2];
    cout << "Round 1: available car = " << CarManager::getInstance()->getAvailableNumber() << endl;
    for(int i=0; i<2; i++){
        clients[i] = thread(task, i);
    }

    for(int i=0; i<2; i++){
        clients[i].join();
    }
    
    CarManager::getInstance()->setCarNumber(2);
    cout << "Round 2: available car = " << CarManager::getInstance()->getAvailableNumber() << endl;
    for(int i=0; i<2; i++){
        clients[i] = thread(task, i);
    }

    for(int i=0; i<2; i++){
        clients[i].join();
    }   
    
    CarManager::getInstance()->setCarNumber(1);
    cout << "Round 3: available car = " << CarManager::getInstance()->getAvailableNumber() << endl;
    for(int i=0; i<2; i++){
        clients[i] = thread(task, i);
    }

    for(int i=0; i<2; i++){
        clients[i].join();
    }   

    return 0;
}