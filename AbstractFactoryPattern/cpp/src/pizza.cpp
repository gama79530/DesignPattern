#include "header/pizza.h"

Pizza::Pizza(shared_ptr<vector<shared_ptr<Ingredient>>> ingredients){
    this->ingredients = ingredients;
}

CheesePizza::CheesePizza(shared_ptr<Cheese> cheese, shared_ptr<vector<shared_ptr<Ingredient>>> ingredients):Pizza(ingredients){
    this->cheese = cheese;
}

shared_ptr<Cheese> CheesePizza::getCheese(){
    return cheese;
}

void CheesePizza::setCheese(shared_ptr<Cheese> cheese){
    this->cheese = cheese;
}

string CheesePizza::showIngredients(){
    string ingredientsString = cheese->getInfo();
    for(auto ingredient: *ingredients){
        ingredientsString += (", " + ingredient->getInfo());
    }

    return ingredientsString;
}

CheesePizzaOfStoreA::CheesePizzaOfStoreA(shared_ptr<Cheese> cheese, shared_ptr<vector<shared_ptr<Ingredient>>> ingredients):CheesePizza(cheese, ingredients){
}

string CheesePizzaOfStoreA::getName(){
    return "store A cheese pizze";
}

CheesePizzaOfStoreB::CheesePizzaOfStoreB(shared_ptr<Cheese> cheese, shared_ptr<vector<shared_ptr<Ingredient>>> ingredients):CheesePizza(cheese, ingredients){
}

string CheesePizzaOfStoreB::getName(){
    return "store B cheese pizze";
}
