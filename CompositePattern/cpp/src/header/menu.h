#ifndef MENU_HEADER_INCLUDED
#define MENU_HEADER_INCLUDED

#include <string>
#include <memory>
#include <vector>

using namespace std;

class MenuItem{
public:
    MenuItem(string description);
    virtual string to_string() = 0;
    virtual bool isItem() = 0;

protected:
    string description;
};

class Menu: public MenuItem{
public:
    Menu(string description);
    void addMenuItem(shared_ptr<MenuItem> &menuItem);
    void addMenuItem(shared_ptr<MenuItem> &&menuItem);
    bool removeMenuItem(shared_ptr<MenuItem> &menuItem);
    bool removeMenuItem(shared_ptr<MenuItem> &&menuItem);
    bool isItem();

protected:
    vector<shared_ptr<MenuItem>> components;
};

class MenuBook: public Menu{
public:
    MenuBook(string description);
    string to_string();
};

class SubMenu: public Menu{
public:
    SubMenu(string description);
    string to_string();
};

class Item: public MenuItem{
public:
    Item(string description);
    bool isItem();
    string to_string();
};

#endif