package DecoratorPattern.java_;

import DecoratorPattern.java_.Beverage.*;
import DecoratorPattern.java_.Beverage.Coffee.*;
import DecoratorPattern.java_.Beverage.Condiment.*;

public class Main {
    public static void main(String[] args) {
        Beverage beverage = null;

        beverage = new Mocha(new Milk(new HouseBlend()));
        System.out.println(String.format("HouseBlend Coffee with mocha and milk: price = %d, cost = %d, profit = %d", beverage.getPrice(), beverage.getCost(), beverage.getProfit()));
        
        beverage = new DarkRoast();
        System.out.println(String.format("DarkRoast Coffee without any condiment: price = %d, cost = %d, profit = %d", beverage.getPrice(), beverage.getCost(), beverage.getProfit()));
    }
}
