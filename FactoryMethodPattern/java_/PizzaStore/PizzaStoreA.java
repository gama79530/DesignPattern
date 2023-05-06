package FactoryMethodPattern.java_.PizzaStore;

import FactoryMethodPattern.java_.Pizza.*;

public class PizzaStoreA extends PizzaStore {

    @Override
    Pizza createPizza(PizzaType type, int radius) {
        if(type == PizzaType.CheesePizza)
            return new CheesePizza(radius);
        else if(type == PizzaType.PepperoniPizza)
            return new PepperoniPizza(radius);
        else
            return null;
    }
}
