#ifndef CONDIMENT_HEADER_INCLUDED
#define CONDIMENT_HEADER_INCLUDED

#include "beverage.h"

class Condiment: public Beverage{
};

class Milk: public Condiment{
public:
    Milk(Beverage& beverage){this->beverage = &beverage;}
    Milk(Beverage&& beverage){this->beverage = &beverage;}
    int getPrice(){return this->beverage->getPrice() + 10;}
    int getCost(){return this->beverage->getCost() + 2;}
    int getProfit(){return getPrice() - getCost();}
private:
    Beverage *beverage;
};

class Mocha: public Condiment{
public:
    Mocha(Beverage& beverage){this->beverage = &beverage;}
    Mocha(Beverage&& beverage){this->beverage = &beverage;}
    int getPrice(){return this->beverage->getPrice() + 15;}
    int getCost(){return this->beverage->getCost() + 5;}
    int getProfit(){return getPrice() - getCost();}
private:
    Beverage *beverage;
};

#endif