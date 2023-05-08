package AbstractFactoryPattern.java_.PizzaStore.Pizza;
import java.util.List;
import AbstractFactoryPattern.java_.PizzaStore.Ingredient.Ingredient;

public interface Pizza {
    List<Ingredient> getIngredients();
    void setIngredients(List<Ingredient> ingredients);
    String getName();
    String showIngredients();
}
