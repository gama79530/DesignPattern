package FactoryMethodPattern.java_;

import FactoryMethodPattern.java_.Pizza.PizzaType;
import FactoryMethodPattern.java_.PizzaStore.*;

public class Main {
    public static void main(String[] args) {
        PizzaStore pizzaStoreA = new PizzaStoreA();
        PizzaStore pizzaStoreB = new PizzaStoreB();

        System.out.println(String.format("Order %s from store A", PizzaType.CheesePizza.getInfo()));
        pizzaStoreA.orderPizza(PizzaType.CheesePizza, 6);
        System.out.println(String.format("Order %s from store A", PizzaType.PepperoniPizza.getInfo()));
        pizzaStoreA.orderPizza(PizzaType.PepperoniPizza, 8);
        System.out.println(String.format("Order %s from store A", PizzaType.VeggiePizza.getInfo()));
        pizzaStoreA.orderPizza(PizzaType.VeggiePizza, 10);
        System.out.println();
        System.out.println(String.format("Order %s from store B", PizzaType.CheesePizza.getInfo()));
        pizzaStoreB.orderPizza(PizzaType.CheesePizza, 10);
        System.out.println(String.format("Order %s from store B", PizzaType.PepperoniPizza.getInfo()));
        pizzaStoreB.orderPizza(PizzaType.PepperoniPizza, 8);
        System.out.println(String.format("Order %s from store B", PizzaType.VeggiePizza.getInfo()));
        pizzaStoreB.orderPizza(PizzaType.VeggiePizza, 6);
    }
}
