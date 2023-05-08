#ifndef INGREDIENT_FACTORY_HEADER_INCLUDED
#define INGREDIENT_FACTORY_HEADER_INCLUDED

#include "ingredient.h"

class IngredientFactory{
public:
    virtual Dough* createDough() = 0;
    virtual Cheese* createCheese() = 0;
    virtual Pepperoni* createPepperoni() = 0;
};

class IngredientFactoryOfStoreA: public IngredientFactory{
public:
    Dough* createDough(){return new ThinCrustDough();}
    Cheese* createCheese(){return new ReggianoCheese();}
    Pepperoni* createPepperoni(){return new SlicedPepperoni();}
};

class IngredientFactoryOfStoreB: public IngredientFactory{
public:
    Dough* createDough(){return new ThickCrustDough();}
    Cheese* createCheese(){return new MozzarellaCheese();}
    Pepperoni* createPepperoni(){return new SlicedPepperoni();}
};

#endif