package FactoryMethodPattern.java_.PizzaStore;

import FactoryMethodPattern.java_.Pizza.*;

public class PizzaStoreA extends PizzaStore {

    @Override
    protected Pizza createPizza(PizzaType type, int radius) {
        if(type == PizzaType.CHEESE_PIZZA)
            return new CheesePizza(radius);
        else if(type == PizzaType.PEPPERONI_PIZZA)
            return new PepperoniPizza(radius);
        
        
        return null;
    }
}
