package FactoryMethodPattern.java_;

import FactoryMethodPattern.java_.Pizza.PizzaType;
import FactoryMethodPattern.java_.PizzaStore.*;

public class Main {
    public static void main(String[] args) {
        PizzaStore pizzaStoreA = new PizzaStoreA();
        PizzaStore pizzaStoreB = new PizzaStoreB();

        System.out.println(String.format("Order %s from store A", PizzaType.CHEESE_PIZZA.getInfo()));
        pizzaStoreA.orderPizza(PizzaType.CHEESE_PIZZA, 6);
        System.out.println(String.format("Order %s from store A", PizzaType.PEPPERONI_PIZZA.getInfo()));
        pizzaStoreA.orderPizza(PizzaType.PEPPERONI_PIZZA, 8);
        System.out.println(String.format("Order %s from store A", PizzaType.VEGGIE_PIZZA.getInfo()));
        pizzaStoreA.orderPizza(PizzaType.VEGGIE_PIZZA, 10);
        System.out.println();
        System.out.println(String.format("Order %s from store B", PizzaType.CHEESE_PIZZA.getInfo()));
        pizzaStoreB.orderPizza(PizzaType.CHEESE_PIZZA, 10);
        System.out.println(String.format("Order %s from store B", PizzaType.PEPPERONI_PIZZA.getInfo()));
        pizzaStoreB.orderPizza(PizzaType.PEPPERONI_PIZZA, 8);
        System.out.println(String.format("Order %s from store B", PizzaType.VEGGIE_PIZZA.getInfo()));
        pizzaStoreB.orderPizza(PizzaType.VEGGIE_PIZZA, 6);
    }
}
