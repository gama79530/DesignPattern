package FactoryMethodPattern.java_.PizzaStore;

import FactoryMethodPattern.java_.Pizza.*;

public class PizzaStoreB extends PizzaStore{
    
    @Override
    Pizza createPizza(PizzaType type, int radius) {
        if(type == PizzaType.CHEESE_PIZZA)
            return new CheesePizza(radius);
        else if(type == PizzaType.VEGGIE_PIZZA)
            return new VeggiePizza(radius);
        else
            return null;
    }
}
