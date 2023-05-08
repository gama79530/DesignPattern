#ifndef BEVERAGE_HEADER_INCLUDED
#define BEVERAGE_HEADER_INCLUDED

class Beverage{
public:
    virtual int getPrice() = 0;
    virtual int getCost() = 0;
    int getProfit(){return getPrice() - getCost();};
};

#endif