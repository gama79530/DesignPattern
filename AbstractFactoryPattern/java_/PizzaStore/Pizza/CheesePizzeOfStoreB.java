package AbstractFactoryPattern.java_.PizzaStore.Pizza;

import java.util.*;
import AbstractFactoryPattern.java_.PizzaStore.Ingredient.Cheese;
import AbstractFactoryPattern.java_.PizzaStore.Ingredient.Ingredient;
import AbstractFactoryPattern.java_.PizzaStore.IngredientFactory.IngredientFactory;

public class CheesePizzeOfStoreB implements CheesePizza{
    private List<Ingredient> ingredients = new ArrayList<>();
    private Cheese cheese = null;

    public CheesePizzeOfStoreB(IngredientFactory ingredientFactory) {
        ingredients.add(ingredientFactory.createDough());
        ingredients.add(ingredientFactory.createPepperoni());
        cheese = ingredientFactory.createCheese();
    }

    @Override
    public List<Ingredient> getIngredients() {
        return ingredients;
    }

    @Override
    public void setIngredients(List<Ingredient> ingredients) {
        this.ingredients = ingredients;
    }

    @Override
    public String getName() {
        return "store B cheese pizze";
    }

    @Override
    public String showIngredients() {
        String ingredientsString = cheese.getInfo();
        for(Ingredient ingredient: ingredients){
            ingredientsString += (", " + ingredient.getInfo());
        }
        return ingredientsString;
    }

    @Override
    public Cheese getCheese() {
        return cheese;    
    }

    @Override
    public void setCheese(Cheese cheese) {
        this.cheese = cheese;
    }    
}
