#include <string>
#include "header/pizza.h"

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