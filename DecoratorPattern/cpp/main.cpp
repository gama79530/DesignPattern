#include <iostream>
#include "src/header/beverage.h"
#include "src/header/coffee.h"
#include "src/header/condiment.h"

using namespace std;

int main(){
{   HouseBlend houseBlend;
    Milk milk(houseBlend);
    Mocha mocha(milk);
    Beverage &beverage = mocha;
    cout << "HouseBlend Coffee with mocha and milk: price = " << to_string(beverage.getPrice()) << ", cost = " << to_string(beverage.getCost()) << ", profit = " << to_string(beverage.getProfit()) << endl;
}
{   DarkRoast darkRoast;
    Beverage &beverage = darkRoast;
    cout << "DarkRoast Coffee without any condiment: price = " << to_string(beverage.getPrice()) << ", cost = " << to_string(beverage.getCost()) << ", profit = " << to_string(beverage.getProfit()) << endl;
}
    return 0;
}