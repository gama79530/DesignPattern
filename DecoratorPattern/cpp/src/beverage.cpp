#include "header/beverage.h"

int Beverage::getProfit(){
    return getPrice() - getCost();
}


int DarkRoast::getPrice(){
    return 75;
}

int DarkRoast::getCost(){
    return 15;
}

int HouseBlend::getPrice(){
    return 50;
}

int HouseBlend::getCost(){
    return 10;
}

Condiment::~Condiment(){
    beverage = shared_ptr<Beverage>();
}

Milk::Milk(shared_ptr<Beverage> beverage){
    this->beverage = beverage;
}

int Milk::getPrice(){
    return beverage->getPrice() + 10;
}

int Milk::getCost(){
    return beverage->getCost() + 2;
}

Mocha::Mocha(shared_ptr<Beverage> beverage){
    this->beverage = beverage;
}

int Mocha::getPrice(){
    return beverage->getPrice() + 15;
}

int Mocha::getCost(){
    return beverage->getCost() + 5;
}

