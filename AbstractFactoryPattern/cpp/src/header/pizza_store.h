#ifndef PIZZA_STORE_HEADER_INCLUDED
#define PIZZA_STORE_HEADER_INCLUDED

#include "ingredient_factory.h"
#include "pizza.h"

class PizzaStore{
public:
    virtual shared_ptr<Pizza> orderPizza(PizzaType pizzaType) = 0;

protected:
    unique_ptr<IngredientFactory> ingredientFactory;
};

class PizzaStoreA: public PizzaStore{
public:
    PizzaStoreA();
    shared_ptr<Pizza> orderPizza(PizzaType pizzaType);
};


class PizzaStoreB: public PizzaStore{
public:
    PizzaStoreB();
    shared_ptr<Pizza> orderPizza(PizzaType pizzaType);
};

#endif