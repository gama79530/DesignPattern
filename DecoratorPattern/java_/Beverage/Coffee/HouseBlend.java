package DecoratorPattern.java_.Beverage.Coffee;

public class HouseBlend implements Coffee{
    @Override
    public int getPrice() {
        return 50;
    }

    @Override
    public int getCost() {
        return 10;
    }

    @Override
    public int getProfit() {
        return getPrice() - getCost();
    }
}
