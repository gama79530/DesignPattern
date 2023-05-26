package CompositePattern.java_.Menu;

import java.util.*;

public class SubMenu implements Menu{
    private String description;
    private List<MenuItem> components = new ArrayList<>();

    public SubMenu(String description){
        this.description = description;
    }

    @Override
    public void addMenuItem(MenuItem item){
        components.add(item);
    }

    @Override
    public boolean removeMenuItem(MenuItem item){
        return components.remove(item);
    }

    @Override
    public String toString() {
        String output = String.format("SubMenu %s:\n", description);
        for(MenuItem component: components){
            if(component instanceof Item){
                output += String.format("\t%s\n", component.toString());
            }else{
                output += String.format("\n\t%s", component.toString().replace("\n", "\n\t"));
            }

        }

        return output;
    }
}
