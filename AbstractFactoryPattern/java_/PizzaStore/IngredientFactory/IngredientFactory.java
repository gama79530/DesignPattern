package AbstractFactoryPattern.java_.PizzaStore.IngredientFactory;

import AbstractFactoryPattern.java_.PizzaStore.Ingredient.*;

public interface IngredientFactory {
    Dough createDough();
    Cheese createCheese();
    Pepperoni createPepperoni();
}
