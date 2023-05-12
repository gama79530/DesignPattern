#ifndef PIZZA_STORE_HEADER_INCLUDED
#define PIZZA_STORE_HEADER_INCLUDED
#include <string>
#include <memory>

using namespace std;

enum PizzaType{
    CHEESE_PIZZA,
    PEPPERONI_PIZZA,
    VEGGIE_PIZZA
};

string pizzaTypeToString(PizzaType type);

class Pizza{
public:
    virtual int getPrice() = 0;
    int getRadius();

protected:
    int radius;
};

class CheesePizza: public Pizza{
public:
    CheesePizza(int radius);
    int getPrice() override;
};

class PepperoniPizza: public Pizza{
public:
    PepperoniPizza(int radius);
    int getPrice();
};

class VeggiePizza: public Pizza{
public:
    VeggiePizza(int radius);
    int getPrice();
};

class PizzaStore{
public:
    shared_ptr<Pizza> orderPizza(PizzaType type, int radius);

protected:
    virtual shared_ptr<Pizza> createPizza(PizzaType type, int radius) = 0;
};

class PizzaStoreA: public PizzaStore{
protected:
    shared_ptr<Pizza> createPizza(PizzaType type, int radius) override;
};

class PizzaStoreB: public PizzaStore{
protected:
    shared_ptr<Pizza> createPizza(PizzaType type, int radius);
};

#endif