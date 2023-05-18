#ifndef CAR_MANAGEMENT_HEADER_INCLUDED
#define CAR_MANAGEMENT_HEADER_INCLUDED

#include <thread>
#include <mutex> 
#include <queue>
#include <unordered_set>

using namespace std;


class Car{
public:
    friend class CarManager;
    
    void drive(int clientNo);
    int getCarNo();
    
private:
    int carNo = 0;
    
    Car(int carNo);
    ~Car() = default;
};

class CarManager{
public:
    static CarManager *getInstance();

    CarManager(const CarManager &) = delete;
    CarManager& operator=(CarManager &) = delete;
    ~CarManager() = delete;
    
    int getCarNumber();
    void setCarNumber(int carNumber);
    int getAvailableNumber();
    Car *rentCar();
    Car *returnCar(Car *car);

private:
    CarManager();

    int carNumber = 0;
    int waitForDestroyed = 0;
    queue<Car*> availableCar;
    unordered_set<Car*> dispatchedCar;
    mutex instance_lock;
};

#endif