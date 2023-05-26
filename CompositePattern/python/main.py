from Menu import *

if __name__ == '__main__':
    menu = MenuBook("MenuBook of all MenuItems")
    subMenu = SubMenu("Dessert")
    menu.addMenuItem(subMenu)
    subMenu.addMenuItem(Item("Cake"))
    subMenu.addMenuItem(Item("Cookie"))
    subMenu.addMenuItem(Item("Ice Cream"))
    subMenu.addMenuItem(Item("Candy"))

    subMenu = SubMenu("Drink")
    menu.addMenuItem(subMenu)
    subMenu.addMenuItem(Item("Milk Tea"))
    subMenu.addMenuItem(Item("Blcak Tea"))

    subMenu2 = SubMenu("Coffee")
    subMenu.addMenuItem(subMenu2)
    subMenu2.addMenuItem(Item("Espresso shots"))
    subMenu2.addMenuItem(Item("Americano"))
    subMenu2.addMenuItem(Item("Café Latte"))
    subMenu2.addMenuItem(Item("Cappuccino"))
    subMenu2.addMenuItem(Item("Mocha"))
    subMenu2.addMenuItem(Item("Caramel Macchiato"))

    subMenu = SubMenu("Fried food")
    menu.addMenuItem(subMenu)
    subMenu.addMenuItem(Item("French fries"))
    subMenu.addMenuItem(Item("Hash Browns"))
    subMenu.addMenuItem(Item("Chicken Nuggets"))
    
    print(str(menu))