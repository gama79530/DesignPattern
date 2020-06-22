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
       pass 
#   public void print() {
#     System.out.println("\n" + getName());
#     System.out.println(", " + getDescription());
#     System.out.println("---------------------");
    
#     Iterator iterator = menuComponents.iterator();
#     while (iterator.hasNext()) {
#       MenuComponent menuComponent = (MenuComponent)iterator.next();
#       menuComponent.print();
#     }
#   }
  
    def createIterator(self):
        pass
#   public Iterator createIterator() {
#     if (iterator == null) {
#       iterator = new CompositeIterator(menuComponents.iterator());
#     }
#     return iterator;
#   }

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
  