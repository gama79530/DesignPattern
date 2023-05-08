#ifndef PIZZA_HEADER_INCLUDED
#define PIZZA_HEADER_INCLUDED

#include <string>
#include <vector>
#include "ingredient.h"
#include "ingredient_factory.h"

using namespace std;

enum PizzaType{
    CHEESE_PIZZA,
};

class Pizza{
public:
    virtual string getName() = 0;
    virtual string showIngredients() = 0;

protected:
    vector<Ingredient*> ingredients;
};

class CheesePizza:public Pizza{
public:
    ~CheesePizza();
    Cheese* getCheese(){return cheese;}
    void setCheese(Cheese* cheese){this->cheese = cheese;}
    string showIngredients();
    
protected:
    Cheese *cheese;
};

class CheesePizzaOfStoreA: public CheesePizza{
public:
    CheesePizzaOfStoreA(IngredientFactory& ingredientFactory);
    CheesePizzaOfStoreA(IngredientFactory&& ingredientFactory);
    string getName(){return "store A cheese pizze";}
};

class CheesePizzaOfStoreB: public CheesePizza{
public:
    CheesePizzaOfStoreB(IngredientFactory& ingredientFactory);
    CheesePizzaOfStoreB(IngredientFactory&& ingredientFactory);
    string getName(){return "store B cheese pizze";}
};

#endif