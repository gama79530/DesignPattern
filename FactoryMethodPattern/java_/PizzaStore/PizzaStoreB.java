package FactoryMethodPattern.java_.PizzaStore;

import FactoryMethodPattern.java_.Pizza.*;

public class PizzaStoreB extends PizzaStore{
    
    @Override
    Pizza createPizza(PizzaType type, int radius) {
        if(type == PizzaType.CheesePizza)
            return new CheesePizza(radius);
        else if(type == PizzaType.VeggiePizza)
            return new VeggiePizza(radius);
        else
            return null;
    }
}
