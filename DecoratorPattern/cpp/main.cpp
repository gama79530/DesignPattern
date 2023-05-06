#include <iostream>
#include "src/header/beverage.h"
#include "src/header/coffee.h"
#include "src/header/condiment.h"

using namespace std;

int main(){
{   Beverage &&beverage = Mocha(Milk(HouseBlend()));
    cout << "HouseBlend Coffee with mocha and milk: price = " << beverage.getPrice() << ", cost = " << beverage.getCost() << ", profit = " << beverage.getProfit() << endl;
}
{   Beverage &&beverage = DarkRoast();
    cout << "DarkRoast Coffee without any condiment: price = " << beverage.getPrice() << ", cost = " << beverage.getCost() << ", profit = " << beverage.getProfit() << endl;
}
    return 0;
}