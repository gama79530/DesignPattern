package AbstractFactoryPattern.java_.PizzaStore.Pizza;

import AbstractFactoryPattern.java_.PizzaStore.Ingredient.Cheese;

public interface CheesePizza extends Pizza{
    Cheese getCheese();
    void setCheese(Cheese cheese);
}
