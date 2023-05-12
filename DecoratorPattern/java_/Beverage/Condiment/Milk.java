package DecoratorPattern.java_.Beverage.Condiment;

import DecoratorPattern.java_.Beverage.Beverage;

public class Milk implements Condiment{
    private Beverage beverage;

    public Milk(Beverage beverage) {
        this.beverage = beverage;
    }

    @Override
    public int getPrice() {
        return beverage.getPrice() + 10;
    }

    @Override
    public int getCost() {
        return beverage.getCost() + 2;
    }

    @Override
    public int getProfit() {
        return getPrice() - getCost();
    }

    @Override
    public Beverage getBeverage() {
        return beverage;
    }
}
