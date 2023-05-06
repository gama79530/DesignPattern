#include <iostream>
#include "src/header/beverage.h"
#include "src/header/coffee.h"
#include "src/header/condiment.h"

using namespace std;

int main(){
{   Beverage &&beverage = Mocha(Milk(HouseBlend()));
    cout << "HouseBlend Coffee with mocha and milk: price = " << to_string(beverage.getPrice()) << ", cost = " << to_string(beverage.getCost()) << ", profit = " << to_string(beverage.getProfit()) << endl;
}
{   Beverage &&beverage = DarkRoast();
    cout << "DarkRoast Coffee without any condiment: price = " << to_string(beverage.getPrice()) << ", cost = " << to_string(beverage.getCost()) << ", profit = " << to_string(beverage.getProfit()) << endl;
}
    return 0;
}