#include "header/pizza.h"

using namespace std;

CheesePizza::~CheesePizza(){
    delete cheese;
}

string CheesePizza::showIngredients(){
    string ingredientsString = cheese->getInfo();
    for(auto ingredient: ingredients){
        ingredientsString += (", " + ingredient->getInfo());
    }

    return ingredientsString;
}

CheesePizzaOfStoreA::CheesePizzaOfStoreA(IngredientFactory& ingredientFactory){
    ingredients.push_back(ingredientFactory.createDough());
    cheese = ingredientFactory.createCheese();
}

CheesePizzaOfStoreA::CheesePizzaOfStoreA(IngredientFactory&& ingredientFactory){
    ingredients.push_back(ingredientFactory.createDough());
    cheese = ingredientFactory.createCheese();
}

CheesePizzaOfStoreB::CheesePizzaOfStoreB(IngredientFactory& ingredientFactory){
    ingredients.push_back(ingredientFactory.createDough());
    ingredients.push_back(ingredientFactory.createPepperoni());
    cheese = ingredientFactory.createCheese();
}

CheesePizzaOfStoreB::CheesePizzaOfStoreB(IngredientFactory&& ingredientFactory){
    ingredients.push_back(ingredientFactory.createDough());
    cheese = ingredientFactory.createCheese();
}