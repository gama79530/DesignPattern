#include <iostream>
#include "src/header/pizza_store.h"
#include "src/header/pizza.h"

using namespace std;

int main(){
    PizzaStore &&pizzaStoreA = PizzaStoreA();
    PizzaStore &&pizzaStoreB = PizzaStoreB();
    Pizza *pizza = nullptr;

    pizza = pizzaStoreA.orderPizza(CHEESE_PIZZA);
    cout << "Order " << pizza->getName() << endl;
    cout << "The ingredient of pizza are: " << pizza->showIngredients() << endl;
    cout << endl;
    delete pizza;
    pizza = pizzaStoreB.orderPizza(CHEESE_PIZZA);
    cout << "Order " << pizza->getName() << endl;
    cout << "The ingredient of pizza are: " << pizza->showIngredients() << endl;
    delete pizza;
    
    return 0;
}