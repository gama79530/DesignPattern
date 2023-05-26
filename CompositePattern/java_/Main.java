package CompositePattern.java_;

import CompositePattern.java_.Menu.*;

class Main{
    public static void main(String[] args) {
        MenuBook menu = new MenuBook("MenuBook of all MenuItems");
        SubMenu subMenu = null;
        SubMenu subMenu2 = null;
        
        subMenu = new SubMenu("Dessert");
        menu.addMenuItem(subMenu);
        subMenu.addMenuItem(new Item("Cake"));
        subMenu.addMenuItem(new Item("Cookie"));
        subMenu.addMenuItem(new Item("Ice Cream"));
        subMenu.addMenuItem(new Item("Candy"));

        subMenu = new SubMenu("Drink");
        menu.addMenuItem(subMenu);
        subMenu.addMenuItem(new Item("Milk Tea"));
        subMenu.addMenuItem(new Item("Blcak Tea"));

        subMenu2 = new SubMenu("Coffee");
        subMenu.addMenuItem(subMenu2);
        subMenu2.addMenuItem(new Item("Espresso shots"));
        subMenu2.addMenuItem(new Item("Americano"));
        subMenu2.addMenuItem(new Item("Café Latte"));
        subMenu2.addMenuItem(new Item("Cappuccino"));
        subMenu2.addMenuItem(new Item("Mocha"));
        subMenu2.addMenuItem(new Item("Caramel Macchiato"));
        
        subMenu = new SubMenu("Fried food");
        menu.addMenuItem(subMenu);
        subMenu.addMenuItem(new Item("French fries"));
        subMenu.addMenuItem(new Item("Hash Browns"));
        subMenu.addMenuItem(new Item("Chicken Nuggets"));
        
        System.out.println(menu);
    }
}