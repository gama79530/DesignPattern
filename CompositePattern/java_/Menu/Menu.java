package CompositePattern.java_.Menu;

public interface Menu extends MenuItem{
    void addMenuItem(MenuItem menuItem);
    boolean removeMenuItem(MenuItem menuItem);
}
