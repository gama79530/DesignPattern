package FactoryMethodPattern.java_.Pizza;

public class VeggiePizza implements Pizza{
    private int radius;

    public VeggiePizza(int radius){
        this.radius = radius;
    }

    @Override
    public int getPrice() {
        return radius * radius * 15;
    }

    @Override
    public int getRadius() {
        return radius;
    }
}
