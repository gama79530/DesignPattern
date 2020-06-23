"""
    # All classes should extend MenuComponent.
"""
import Iterator

class MenuComponent:
    def add(self, menu_component):
        raise AttributeError()
  
    def remove(self, menu_component):
        raise AttributeError()

    def getChild(self, i):
        raise AttributeError()
  
    def print(self):
        raise AttributeError()
  
    def createIterator(self):
        raise AttributeError()

class Menu(MenuComponent):
    def __init__(self, name, description):
        self.iterator = None
        self.menu_components = []
        self.name = name
        self.description = description

    def add(self, menu_component):
        self.menu_components.append(menu_component)

    def remove(self, menu_component):
        self.menu_components.remove(menu_component)

    def getChild(self, i):
        return self.menu_components[i]
  
    def print(self):
       print("\n{}".format(self.name)) 
       print(", {}".format(self.description)) 
       print("---------------------")
       for menu_component in self.menu_components:
           menu_component.print()
  
    def createIterator(self):
        if self.iterator is None:
            self.iterator = Iterator.CompositeIterator(Iterator.ListIterator(self.menu_components))
        return self.iterator

class MenuItem(MenuComponent):
    def __init__(self, name, description, vegetarian, price):
        self.name = name
        self.description = description
        self.vegetarian = vegetarian
        self.price = price
  
    def print(self):
        print('  {}{}, {}'.format(self.name, ('(v)' if self.vegetarian else ''), self.price)) 
        print('    -- {}'.format(self.description)) 
  
    def createIterator(self):
        return Iterator.NullIterator()
  