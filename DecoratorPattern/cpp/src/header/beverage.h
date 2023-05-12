#ifndef BEVERAGE_HEADER_INCLUDED
#define BEVERAGE_HEADER_INCLUDED
#include <memory>

using namespace std;

class Beverage{
public:
    virtual int getPrice() = 0;
    virtual int getCost() = 0;

    int getProfit();
};

class Coffee: public Beverage{
};

class DarkRoast: public Coffee{
public:
    int getPrice() override;
    int getCost() override;
};

class HouseBlend: public Coffee{
public:
    int getPrice() override;
    int getCost() override;
};

class Condiment: public Beverage{
protected:
    shared_ptr<Beverage> beverage;
    
    ~Condiment();
};

class Milk: public Condiment{
public:
    Milk(shared_ptr<Beverage> beverage);
    
    int getPrice() override;
    int getCost() override;
};

class Mocha: public Condiment{
public:
    Mocha(shared_ptr<Beverage> beverage);

    int getPrice();
    int getCost();
};

#endif