#include <iostream>
#include "src/header/menu.h"

using namespace std;

int main(){
    MenuBook menu("MenuBook of all MenuItems");
    shared_ptr<SubMenu> subMenu;
    shared_ptr<SubMenu> subMenu2;

    subMenu = make_shared<SubMenu>("Dessert");
    menu.addMenuItem(subMenu);
    subMenu->addMenuItem(make_shared<Item>("Cake"));
    subMenu->addMenuItem(make_shared<Item>("Cookie"));
    subMenu->addMenuItem(make_shared<Item>("Ice Cream"));
    subMenu->addMenuItem(make_shared<Item>("Candy"));

    subMenu = make_shared<SubMenu>("Drink");
    menu.addMenuItem(subMenu);
    subMenu->addMenuItem(make_shared<Item>("Milk Tea"));
    subMenu->addMenuItem(make_shared<Item>("Blcak Tea"));

    subMenu2 = make_shared<SubMenu>("Coffee");
    subMenu->addMenuItem(subMenu2);
    subMenu2->addMenuItem(make_shared<Item>("Espresso shots"));
    subMenu2->addMenuItem(make_shared<Item>("Americano"));
    subMenu2->addMenuItem(make_shared<Item>("Café Latte"));
    subMenu2->addMenuItem(make_shared<Item>("Cappuccino"));
    subMenu2->addMenuItem(make_shared<Item>("Mocha"));
    subMenu2->addMenuItem(make_shared<Item>("Caramel Macchiato"));
    
    subMenu = make_shared<SubMenu>("Fried food");
    menu.addMenuItem(subMenu);
    subMenu->addMenuItem(make_shared<Item>("French fries"));
    subMenu->addMenuItem(make_shared<Item>("Hash Browns"));
    subMenu->addMenuItem(make_shared<Item>("Chicken Nuggets"));

    cout << menu.to_string() << endl;

    return 0;
}