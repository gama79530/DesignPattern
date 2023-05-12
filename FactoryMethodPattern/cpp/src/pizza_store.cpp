#include <iostream>
#include "header/pizza_store.h"

using namespace std;

string pizzaTypeToString(PizzaType type){
    if(type == CHEESE_PIZZA)
        return "cheese flavor pizza";
    else if(type == PEPPERONI_PIZZA)
        return "pepperoni flavor pizza";
    else if(type == VEGGIE_PIZZA)
        return "veggie flavor pizza";

    return "";
}

int Pizza::getRadius(){
    return radius;
}

CheesePizza::CheesePizza(int radius){
    this->radius = radius;
}

int CheesePizza::getPrice(){
    return radius * radius * 10;
}

PepperoniPizza::PepperoniPizza(int radius){
    this->radius = radius;
}

int PepperoniPizza::getPrice(){
    return radius * radius * 20;
}

VeggiePizza::VeggiePizza(int radius){
    this->radius = radius;
}

int VeggiePizza::getPrice(){
    return radius * radius * 15;
}

shared_ptr<Pizza> PizzaStore::orderPizza(PizzaType type, int radius){
    shared_ptr<Pizza> pizza = createPizza(type, radius);
    if(pizza == nullptr){
        cout << "The " << pizzaTypeToString(type) << " is not provided !!!" << endl;
    }else{
        cout << "The " << pizzaTypeToString(type) << " is provided. The radius of pizza is " << pizza->getRadius() << " and the price of pizza is " << pizza->getPrice() << endl;
    }

    return pizza;
}

shared_ptr<Pizza> PizzaStoreA::createPizza(PizzaType type, int radius){
    if(type == CHEESE_PIZZA)
        return make_shared<CheesePizza>(radius);
    else if(type == PEPPERONI_PIZZA)
        return make_shared<PepperoniPizza>(radius);

    return shared_ptr<Pizza>();
}

shared_ptr<Pizza> PizzaStoreB::createPizza(PizzaType type, int radius){
    if(type == CHEESE_PIZZA)
        return make_shared<CheesePizza>(radius);
    else if(type == VEGGIE_PIZZA)
        return make_shared<VeggiePizza>(radius);

    return shared_ptr<Pizza>();
}