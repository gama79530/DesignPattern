package FactoryMethodPattern.java_.Pizza;

public class PepperoniPizza implements Pizza{
    private int radius;

    public PepperoniPizza(int radius){
        this.radius = radius;
    }

    @Override
    public int getPrice() {
        return radius * radius * 20;
    }

    @Override
    public int getRadius() {
        return radius;
    }

    @Override
    public void setRadius(int radius) {
        this.radius = radius;
    }
}
