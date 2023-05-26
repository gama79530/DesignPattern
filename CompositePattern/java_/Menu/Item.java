package CompositePattern.java_.Menu;

public class Item implements MenuItem{
    private String description;

    public Item(String description) {
        this.description = description;
    }

    @Override
    public String toString() {
        return description;
    }
}
