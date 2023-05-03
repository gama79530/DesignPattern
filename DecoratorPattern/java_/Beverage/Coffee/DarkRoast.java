package DecoratorPattern.java_.Beverage.Coffee;

public class DarkRoast implements Coffee{
    @Override
    public int getPrice() {
        return 75;
    }

    @Override
    public int getCost() {
        return 15;    
    }

    @Override
    public int getProfit() {
        return getPrice() - getCost();
    }
}
