#ifndef PIZZA_HEADER_INCLUDED
#define PIZZA_HEADER_INCLUDED
#include <string>

using namespace std;

enum PizzaType{
    CHEESE_PIZZA,
    PEPPERONI_PIZZA,
    VEGGIE_PIZZA
};

string pizzaTypeToString(PizzaType type);

class Pizza{
public:
    int radius;
    virtual int getPrice() = 0;
};

class CheesePizza: public Pizza{
public:
    CheesePizza(int radius){this->radius = radius;}
    int getPrice(){return radius * radius * 10;}
};

class PepperoniPizza: public Pizza{
public:
    PepperoniPizza(int radius){this->radius = radius;}
    int getPrice(){return radius * radius * 20;}
};

class VeggiePizza: public Pizza{
public:
    VeggiePizza(int radius){this->radius = radius;}
    int getPrice(){return radius * radius * 15;}
};

#endif