package AbstractFactoryPattern.java_.PizzaStore.Pizza;

import java.util.*;
import AbstractFactoryPattern.java_.PizzaStore.Ingredient.*;

public class CheesePizzaOfStoreA implements CheesePizza{
    private List<Ingredient> ingredients = null;
    private Cheese cheese = null;

    public CheesePizzaOfStoreA(Cheese cheese, List<Ingredient> ingredients) {
        this.cheese = cheese;
        this.ingredients = ingredients;
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
        return "store A cheese pizze";
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
