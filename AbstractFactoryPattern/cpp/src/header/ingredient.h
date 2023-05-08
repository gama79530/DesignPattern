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
    string getInfo(){return "thick crust dough";}
};

class ThinCrustDough: public Dough{
public:
    string getInfo(){return "thin crust dough";}
};

class Cheese: public Ingredient{
};

class ReggianoCheese: public Cheese{
public:
    string getInfo(){return "reggiano cheese";}
};

class MozzarellaCheese: public Cheese{
public:
    string getInfo(){return "mozzarella cheese";}
};

class Pepperoni: public Ingredient{
};

class SlicedPepperoni: public Pepperoni{
public:
    string getInfo(){return "sliced pepperoni";}
};

#endif