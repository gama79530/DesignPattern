#include "header/pizza_store.h"
#include <string>
#include <iostream>

PizzaStoreA::PizzaStoreA(){
    ingredientFactory = make_unique<IngredientFactoryOfStoreA>();
}

shared_ptr<Pizza> PizzaStoreA::orderPizza(PizzaType pizzaType){
    if(pizzaType == CHEESE_PIZZA){
        shared_ptr<Cheese> cheese = ingredientFactory->createCheese(); 
        shared_ptr<vector<shared_ptr<Ingredient>>> ingredients = make_shared<vector<shared_ptr<Ingredient>>>();
        auto t = ingredientFactory->createDough();
        ingredients->push_back(ingredientFactory->createDough());
        return make_shared<CheesePizzaOfStoreA>(cheese, ingredients);
    }

    return shared_ptr<Pizza>();
}

PizzaStoreB::PizzaStoreB(){
    ingredientFactory = make_unique<IngredientFactoryOfStoreB>();
}

shared_ptr<Pizza> PizzaStoreB::orderPizza(PizzaType pizzaType){
    if(pizzaType == CHEESE_PIZZA){
        shared_ptr<Cheese> cheese = ingredientFactory->createCheese(); 
        shared_ptr<vector<shared_ptr<Ingredient>>> ingredients = make_shared<vector<shared_ptr<Ingredient>>>();
        ingredients->push_back(ingredientFactory->createDough());
        ingredients->push_back(ingredientFactory->createPepperoni());
        return make_shared<CheesePizzaOfStoreB>(cheese, ingredients);
    }

    return shared_ptr<Pizza>();
}

