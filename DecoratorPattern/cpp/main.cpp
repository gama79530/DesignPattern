#include <iostream>
#include "src/header/beverage.h"

using namespace std;

int main(){
    shared_ptr<Beverage> beverage;
    beverage = make_shared<Mocha>(make_shared<Milk>(make_shared<HouseBlend>()));
    cout << "HouseBlend Coffee with mocha and milk: price = " << beverage->getPrice() << ", cost = " << beverage->getCost() << ", profit = " << beverage->getProfit() << endl;
    beverage = make_shared<DarkRoast>();
    cout << "DarkRoast Coffee without any condiment: price = " << beverage->getPrice() << ", cost = " << beverage->getCost() << ", profit = " << beverage->getProfit() << endl;

    return 0;
}