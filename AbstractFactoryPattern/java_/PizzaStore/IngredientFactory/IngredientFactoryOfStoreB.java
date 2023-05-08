package AbstractFactoryPattern.java_.PizzaStore.IngredientFactory;

import AbstractFactoryPattern.java_.PizzaStore.Ingredient.*;

public class IngredientFactoryOfStoreB implements IngredientFactory{
    @Override
    public Dough createDough() {
        return new ThickCrustDough();    
    }

    @Override
    public Cheese createCheese() {
        return new MozzarellaCheese();
    }

    @Override
    public Pepperoni createPepperoni() {
        return new SlicedPepperoni();
    }
}
