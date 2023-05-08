package FactoryMethodPattern.java_.PizzaStore;

import FactoryMethodPattern.java_.Pizza.*;

public abstract class PizzaStore {
    abstract Pizza createPizza(PizzaType type, int radius);
    
    public Pizza orderPizza(PizzaType type, int radius){
        Pizza pizza = createPizza(type, radius);
        if(pizza == null){
            System.out.println(String.format("The %s is not provided !!!", type.getInfo()));
        }else{
            System.out.println(String.format("The %s is provided. The radius of pizza is %d and the price of pizza is %d", type.getInfo(), radius, pizza.getPrice()));
        }

        return pizza;
    }
}
