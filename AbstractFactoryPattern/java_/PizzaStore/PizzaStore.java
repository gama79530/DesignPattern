package AbstractFactoryPattern.java_.PizzaStore;

import AbstractFactoryPattern.java_.PizzaStore.IngredientFactory.IngredientFactory;
import AbstractFactoryPattern.java_.PizzaStore.Pizza.*;

public interface PizzaStore {
    IngredientFactory getIngredientFactory();
    void setIngredientFactory(IngredientFactory ingredientFactory);
    Pizza orderPizza(PizzaType pizzaType);
}
