package AbstractFactoryPattern.java_;

import AbstractFactoryPattern.java_.PizzaStore.*;
import AbstractFactoryPattern.java_.PizzaStore.Pizza.*;

public class Main {
    public static void main(String[] args) {
        PizzaStore pizzaStoreA = new PizzaStoreA();
        PizzaStore pizzaStoreB = new PizzaStoreB();
        Pizza pizza = null;

        pizza = pizzaStoreA.orderPizza(PizzaType.CHEESE_PIZZA);
        System.out.println(String.format("Order %s", pizza.getName()));
        System.out.println(String.format("The ingredient of pizza are: %s", pizza.showIngredients()));
        System.out.println();
        pizza = pizzaStoreB.orderPizza(PizzaType.CHEESE_PIZZA);
        System.out.println(String.format("Order %s", pizza.getName()));
        System.out.println(String.format("The ingredient of pizza are: %s", pizza.showIngredients()));
    }
}
