#ifndef COFFEE_HEADER_INCLUDED
#define COFFEE_HEADER_INCLUDED

#include "beverage.h"

class Coffee: public Beverage{
};

class DarkRoast: public Coffee{
public:
    int getPrice(){return 75;}
    int getCost(){return 15;}
    int getProfit(){return getPrice() - getCost();}
};

class HouseBlend: public Coffee{
public:
    int getPrice(){return 50;}
    int getCost(){return 10;}
    int getProfit(){return getPrice() - getCost();}
};

#endif