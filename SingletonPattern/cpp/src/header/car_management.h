#ifndef CAR_MANAGEMENT_HEADER_INCLUDED
#define CAR_MANAGEMENT_HEADER_INCLUDED

#include <thread>
#include <mutex> 
#include <queue>
#include <unordered_set>

using namespace std;

class Car{
public:
    Car(int carNo){this->carNo = carNo;}
    int getCarNo(){return carNo;}
    void setCarNo(){this->carNo = carNo;}
    void drive(int clientNo);

private:
    int carNo = 0;
};

class CarManager{
public:
    static CarManager* getInstance();

    int getCarNumber();
    void setCarNumber(int carNumber);
    int getAvailableNumber();
    Car* rentCar();
    Car* returnCar(Car* car);

private:
    static int carSequence;
    static CarManager* carManager;
    static mutex static_lock;
    
    CarManager(){};

    int carNumber = 0;
    int waitForDestroyed = 0;
    queue<Car*> availableCar;
    unordered_set<Car*> dispatchedCar;
    mutex instance_lock;
};

#endif