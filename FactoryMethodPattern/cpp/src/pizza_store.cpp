#include <iostream>
#include "header/pizza_store.h"

using namespace std;

void PizzaStore::orderPizza(PizzaType type, int radius){
    Pizza* pizza = createPizza(type, radius);
    if(pizza == nullptr){
        cout << "The " << pizzaTypeToString(type) << " is not provided !!!" << endl;
    }else{
        cout << "The " << pizzaTypeToString(type) << " is provided. The radius of pizza is " << pizza->radius << " and the price of pizza is " << pizza->getPrice() << endl;
    }
}

Pizza* PizzaStoreA::createPizza(PizzaType type, int radius){
    if(type == CHEESE_PIZZA)
        return new CheesePizza(radius);
    else if(type == PEPPERONI_PIZZA)
        return new PepperoniPizza(radius);

    return nullptr;
}

Pizza* PizzaStoreB::createPizza(PizzaType type, int radius){
    if(type == CHEESE_PIZZA)
        return new CheesePizza(radius);
    else if(type == VEGGIE_PIZZA)
        return new VeggiePizza(radius);

    return nullptr;
}