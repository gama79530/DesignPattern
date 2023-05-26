#include <queue>
#include "header/menu.h"


MenuItem::MenuItem(string description){
    this->description = description;
}

Menu::Menu(string description): MenuItem(description){};

void Menu::addMenuItem(shared_ptr<MenuItem> &menuItem){
    components.push_back(menuItem);
}

void Menu::addMenuItem(shared_ptr<MenuItem> &&menuItem){
    components.push_back(menuItem);
}

bool Menu::removeMenuItem(shared_ptr<MenuItem> &menuItem){
    for(auto it=components.begin(); it != components.end(); it++){
        if(*it == menuItem){
            components.erase(it);
            return true;
        }
    }

    return false;
}

bool Menu::removeMenuItem(shared_ptr<MenuItem> &&menuItem){
    for(auto it=components.begin(); it != components.end(); it++){
        if(*it == menuItem){
            components.erase(it);
            return true;
        }
    }

    return false;
}

bool Menu::isItem(){
    return false;
}

MenuBook::MenuBook(string description): Menu(description){};

string MenuBook::to_string(){
    string output = "======    " + description + "    ======\n";
    for(auto component: components){
        output += (component->to_string() + "\n");
    }

    return output;
}

SubMenu::SubMenu(string description): Menu(description){};

string SubMenu::to_string(){
    string output = "SubMenu " + description +":\n";
    for(auto component: components){
        if(component->isItem()){
            output += ("\t" + component->to_string() + "\n");
        }else{
            string s = component->to_string();
            int pos = s.find("\n", 0);
            while(pos != string::npos){
                s.replace(pos, 1, "\n\t");
                pos = s.find("\n", pos+2);
            }
            output += ("\n\t" + s);
        }
    }

    return output;
}

Item::Item(string description): MenuItem(description){};


bool Item::isItem(){
    return true;
}

string Item::to_string(){
    return description;
}
