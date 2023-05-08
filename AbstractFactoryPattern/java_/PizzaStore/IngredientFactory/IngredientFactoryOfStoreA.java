package AbstractFactoryPattern.java_.PizzaStore.IngredientFactory;

import AbstractFactoryPattern.java_.PizzaStore.Ingredient.*;

public class IngredientFactoryOfStoreA implements IngredientFactory{
    @Override
    public Dough createDough() {
        return new ThinCrustDough();    
    }

    @Override
    public Cheese createCheese() {
        return new ReggianoCheese();
    }

    @Override
    public Pepperoni createPepperoni() {
        return new SlicedPepperoni();
    }
}
