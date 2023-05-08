package AbstractFactoryPattern.java_.PizzaStore;

import AbstractFactoryPattern.java_.PizzaStore.IngredientFactory.*;
import AbstractFactoryPattern.java_.PizzaStore.Pizza.*;

public class PizzaStoreA implements PizzaStore{
    private IngredientFactory ingredientFactory = new IngredientFactoryOfStoreA();

    @Override
    public IngredientFactory getIngredientFactory() {
        return ingredientFactory;
    }

    @Override
    public void setIngredientFactory(IngredientFactory ingredientFactory) {
        this.ingredientFactory = ingredientFactory;
    }

    @Override
    public Pizza orderPizza(PizzaType pizzaType) {
        if(pizzaType == PizzaType.CHEESE_PIZZA){
            return new CheesePizzeOfStoreA(ingredientFactory);
        }

        return null;
    }
    
}
