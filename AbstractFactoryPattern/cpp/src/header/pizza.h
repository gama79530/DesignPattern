#ifndef PIZZA_HEADER_INCLUDED
#define PIZZA_HEADER_INCLUDED

#include <string>
#include <vector>
#include <memory>
#include "ingredient.h"

using namespace std;

enum PizzaType{
    CHEESE_PIZZA,
};

class Pizza{
public:
    virtual string getName() = 0;
    virtual string showIngredients() = 0;

    Pizza(shared_ptr<vector<shared_ptr<Ingredient>>> ingredients);

protected:
    shared_ptr<vector<shared_ptr<Ingredient>>> ingredients;
};

class CheesePizza:public Pizza{
public:
    CheesePizza(shared_ptr<Cheese> cheese, shared_ptr<vector<shared_ptr<Ingredient>>> ingredients);

    shared_ptr<Cheese> getCheese();
    void setCheese(shared_ptr<Cheese> cheese);
    string showIngredients() override;
    
protected:
    shared_ptr<Cheese> cheese;
};

class CheesePizzaOfStoreA: public CheesePizza{
public:
    CheesePizzaOfStoreA(shared_ptr<Cheese> cheese, shared_ptr<vector<shared_ptr<Ingredient>>> ingredients);

    string getName() override;
};

class CheesePizzaOfStoreB: public CheesePizza{
public:
    CheesePizzaOfStoreB(shared_ptr<Cheese> cheese, shared_ptr<vector<shared_ptr<Ingredient>>> ingredients);

    string getName() override;
};

#endif