#ifndef INGREDIENT_FACTORY_HEADER_INCLUDED
#define INGREDIENT_FACTORY_HEADER_INCLUDED
#include <memory>
#include "ingredient.h"

class IngredientFactory{
public:
    virtual shared_ptr<Dough> createDough() = 0;
    virtual shared_ptr<Cheese> createCheese() = 0;
    virtual shared_ptr<Pepperoni> createPepperoni() = 0;
};

class IngredientFactoryOfStoreA: public IngredientFactory{
public:
    shared_ptr<Dough> createDough() override;
    shared_ptr<Cheese> createCheese() override;
    shared_ptr<Pepperoni> createPepperoni() override;
};

class IngredientFactoryOfStoreB: public IngredientFactory{
public:
    shared_ptr<Dough> createDough() override;
    shared_ptr<Cheese> createCheese() override;
    shared_ptr<Pepperoni> createPepperoni() override;
};

#endif