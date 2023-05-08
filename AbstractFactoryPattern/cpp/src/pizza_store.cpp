#include "header/pizza_store.h"

PizzaStore::~PizzaStore(){
    delete ingredientFactory;
}

Pizza* PizzaStoreA::orderPizza(PizzaType pizzaType){
    if(pizzaType == CHEESE_PIZZA)
        return new CheesePizzaOfStoreA(*ingredientFactory);

    return nullptr;
}

Pizza* PizzaStoreB::orderPizza(PizzaType pizzaType){
    if(pizzaType == CHEESE_PIZZA)
        return new CheesePizzaOfStoreB(*ingredientFactory);

    return nullptr;
}

