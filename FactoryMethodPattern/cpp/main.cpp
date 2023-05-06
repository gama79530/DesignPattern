#include <iostream>
#include "src/header/pizza.h"
#include "src/header/pizza_store.h"

using namespace std;

int main(){
    PizzaStore &&pizzaStoreA = PizzaStoreA();
    PizzaStore &&pizzaStoreB = PizzaStoreB();

    cout << "Order " << pizzaTypeToString(CHEESE_PIZZA) << " from store A" << endl;
    pizzaStoreA.orderPizza(CHEESE_PIZZA, 6);
    cout << "Order " << pizzaTypeToString(PEPPERONI_PIZZA) << " from store A" << endl;
    pizzaStoreA.orderPizza(PEPPERONI_PIZZA, 8);
    cout << "Order " << pizzaTypeToString(VEGGIE_PIZZA) << " from store A" << endl;
    pizzaStoreA.orderPizza(VEGGIE_PIZZA, 10);
    cout << endl;
    cout << "Order " << pizzaTypeToString(CHEESE_PIZZA) << " from store B" << endl;
    pizzaStoreB.orderPizza(CHEESE_PIZZA, 10);
    cout << "Order " << pizzaTypeToString(PEPPERONI_PIZZA) << " from store B" << endl;
    pizzaStoreB.orderPizza(PEPPERONI_PIZZA, 8);
    cout << "Order " << pizzaTypeToString(VEGGIE_PIZZA) << " from store B" << endl;
    pizzaStoreB.orderPizza(VEGGIE_PIZZA, 6);

    return 0;
}