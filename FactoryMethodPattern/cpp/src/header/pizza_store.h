#ifndef PIZZA_STORE_HEADER_INCLUDED
#define PIZZA_STORE_HEADER_INCLUDED
#include "pizza.h"

class PizzaStore{
public:
    Pizza* orderPizza(PizzaType type, int radius);

protected:
    virtual Pizza* createPizza(PizzaType type, int radius) = 0;
};

class PizzaStoreA: public PizzaStore{
    Pizza* createPizza(PizzaType type, int radius);
};

class PizzaStoreB: public PizzaStore{
    Pizza* createPizza(PizzaType type, int radius);
};

#endif