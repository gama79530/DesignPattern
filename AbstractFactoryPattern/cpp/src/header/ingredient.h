#ifndef INGREDIENT_HEADER_INCLUDED
#define INGREDIENT_HEADER_INCLUDED
#include <string>

using namespace std;

class Ingredient{
public:
   virtual string getInfo() = 0;
};

class Dough: public Ingredient{
};

class ThickCrustDough: public Dough{
public:
    string getInfo() override;
};

class ThinCrustDough: public Dough{
public:
    string getInfo() override;
};

class Cheese: public Ingredient{
};

class ReggianoCheese: public Cheese{
public:
    string getInfo() override;
};

class MozzarellaCheese: public Cheese{
public:
    string getInfo() override;
};

class Pepperoni: public Ingredient{
};

class SlicedPepperoni: public Pepperoni{
public:
    string getInfo() override;
};

#endif