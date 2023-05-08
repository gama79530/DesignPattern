package DecoratorPattern.java_.Beverage.Condiment;

import DecoratorPattern.java_.Beverage.Beverage;

public interface Condiment extends Beverage{
    Beverage getBeverage();
    void setBeverage(Beverage beverage);
}
