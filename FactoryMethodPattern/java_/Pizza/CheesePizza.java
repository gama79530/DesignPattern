package FactoryMethodPattern.java_.Pizza;

public class CheesePizza implements Pizza{
    private int radius;

    public CheesePizza(int radius){
        this.radius = radius;
    }

    @Override
    public int getPrice() {
        return radius * radius * 10;
    }

    @Override
    public int getRadius() {
        return radius;
    }
}
