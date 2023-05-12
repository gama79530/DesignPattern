#include <iostream>
#include "src/header/pizza_store.h"
#include "src/header/pizza.h"

using namespace std;

int main(){
    shared_ptr<PizzaStore> pizzaStoreA = make_shared<PizzaStoreA>();
    shared_ptr<PizzaStore> pizzaStoreB = make_shared<PizzaStoreB>();
    shared_ptr<Pizza> pizza;

    pizza = pizzaStoreA->orderPizza(CHEESE_PIZZA);
    cout << "Order " << pizza->getName() << endl;
    cout << "The ingredient of pizza are: " << pizza->showIngredients() << endl;
    cout << endl;
    pizza = pizzaStoreB->orderPizza(CHEESE_PIZZA);
    cout << "Order " << pizza->getName() << endl;
    cout << "The ingredient of pizza are: " << pizza->showIngredients() << endl;
    pizza = shared_ptr<Pizza>();
    
    return 0;
}