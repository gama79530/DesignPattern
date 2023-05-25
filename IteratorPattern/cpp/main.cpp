#include <iostream>
#include "src/header/vehicle.h"
#include "src/header/garage.h"
#include "src/garage.cpp"

int main(){
    Container<shared_ptr<Vehicle>> garage;

    garage.add(make_shared<Motorcycle>("Harley", "014X-X54A"));
    garage.add(make_shared<Car>("Toyota Corolla Altis", "0XS7-7LE5"));
    garage.add(make_shared<Car>("Nissan GT-R", "1S7W-8A1S"));
    auto iterator = garage.createIterator();
    while(iterator->hasNext()){
        cout << iterator->next()->toString() << endl;
    }

    return 0;
}