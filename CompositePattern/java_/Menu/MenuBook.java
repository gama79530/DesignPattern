package CompositePattern.java_.Menu;

import java.util.*;

public class MenuBook implements Menu{
    private String description;
    private List<MenuItem> components = new ArrayList<>();

    public MenuBook(String description){
        this.description = description;
    }

    @Override
    public void addMenuItem(MenuItem menuItem){
        components.add(menuItem);
    }

    @Override
    public boolean removeMenuItem(MenuItem menuItem){
        return components.remove(menuItem);
    }

    @Override
    public String toString() {
        String output = String.format("======    %s    ======\n", description);
        for(MenuItem component: components){
            output += String.format("%s\n", component.toString());
        }

        return output;
    }
}
