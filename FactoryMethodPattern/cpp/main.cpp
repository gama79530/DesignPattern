#include <iostream>
#include "src/header/pizza_store.h"

using namespace std;

int main(){
    PizzaStore &&pizzaStoreA = PizzaStoreA();
    PizzaStore &&pizzaStoreB = PizzaStoreB();
    shared_ptr<Pizza> pizza;

    cout << "Order " << pizzaTypeToString(CHEESE_PIZZA) << " from store A" << endl;
    pizza = pizzaStoreA.orderPizza(CHEESE_PIZZA, 6);
    cout << "Order " << pizzaTypeToString(PEPPERONI_PIZZA) << " from store A" << endl;
    pizza = pizzaStoreA.orderPizza(PEPPERONI_PIZZA, 8);
    cout << "Order " << pizzaTypeToString(VEGGIE_PIZZA) << " from store A" << endl;
    pizza = pizzaStoreA.orderPizza(VEGGIE_PIZZA, 10);
    cout << endl;
    cout << "Order " << pizzaTypeToString(CHEESE_PIZZA) << " from store B" << endl;
    pizza = pizzaStoreB.orderPizza(CHEESE_PIZZA, 10);
    cout << "Order " << pizzaTypeToString(PEPPERONI_PIZZA) << " from store B" << endl;
    pizza = pizzaStoreB.orderPizza(PEPPERONI_PIZZA, 8);
    cout << "Order " << pizzaTypeToString(VEGGIE_PIZZA) << " from store B" << endl;
    pizza = pizzaStoreB.orderPizza(VEGGIE_PIZZA, 6);
    
    return 0;
}