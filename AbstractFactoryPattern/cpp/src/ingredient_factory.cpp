#include "header/ingredient_factory.h"


shared_ptr<Dough> IngredientFactoryOfStoreA::createDough(){
    return make_shared<ThinCrustDough>();
}

shared_ptr<Cheese> IngredientFactoryOfStoreA::createCheese(){
    return make_shared<ReggianoCheese>();
}

shared_ptr<Pepperoni> IngredientFactoryOfStoreA::createPepperoni(){
    return make_shared<SlicedPepperoni>();
}

shared_ptr<Dough> IngredientFactoryOfStoreB::createDough(){
    return make_shared<ThickCrustDough>();
}

shared_ptr<Cheese> IngredientFactoryOfStoreB::createCheese(){
    return make_shared<MozzarellaCheese>();
}

shared_ptr<Pepperoni> IngredientFactoryOfStoreB::createPepperoni(){
    return make_shared<SlicedPepperoni>();
}