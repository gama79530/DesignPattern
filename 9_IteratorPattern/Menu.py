"""
    # All classes should extend Menu and override the following or methods.
    def createIterator(self) :
"""
import MenuItem
import Iterator

class Menu :
    def createIterator(self) :
        assert False, 'This method should be overrided.' 

class CafeMenu(Menu):
    def __init__(self):
        self.menu_items = {}
        self.addItem("Veggie Burger and Air Fries", "Veggie burger on a whole wheat bun, lettuce, tomato, and fries", True, 3.99)
        self.addItem("Soup of the day", "A cup of the soup of the day, with a side salad", False, 3.69)
        self.addItem("Burrito", "A large burrito, with whole pinto beans, salsa, guacamole", True, 4.29)

    def addItem(self, name, description, vegetarian, price):
        menu_item = MenuItem.MenuItem(name, description, vegetarian, price)
        self.menu_items[menu_item.name] = menu_item

    def createIterator(self) :
        return Iterator.CafeMenuIterator(self.menu_items)
    
class DinerMenu(Menu):
    def __init__(self):
        self.max_items = 6
        self.menu_items = []
        self.addItem("Vegetarian BLT", "(Fakin') Bacon with lettuce & tomato on whole wheat", True, 2.99)
        self.addItem("BLT", "Bacon with lettuce & tomato on whole wheat", False, 2.99)
        self.addItem("Soup of the day", "Soup of the day, with a side of potato salad", False, 3.29)
        self.addItem("Hotdog", "A hot dog, with saurkraut, relish, onions, topped with cheese", False, 3.05)
        self.addItem("Steamed Veggies and Brown Rice", "Steamed vegetables over brown rice", True, 3.99)
        self.addItem("Pasta", "Spaghetti with Marinara Sauce, and a slice of sourdough bread", True, 3.89)

    def addItem(self, name, description, vegetarian, price):
        if len(self.menu_items) >= self.max_items:
            print("Sorry, menu is full! Can't add item to menu")
        else:
            menu_item = MenuItem.MenuItem(name, description, vegetarian, price)
            self.menu_items.append(menu_item)

    def createIterator(self) :
        return Iterator.DinerMenuIterator(self.menu_items)
    
class PancakeHouseMenu(Menu):
    def __init__(self):
        self.menu_items = []
        self.addItem("K&B's Pancake Breakfast", "Pancakes with scrambled eggs, and toast", True, 2.99)
        self.addItem("Regular Pancake Breakfast", "Pancakes with fried eggs, sausage", False, 2.99)
        self.addItem("Blueberry Pancakes", "Pancakes made with fresh blueberries", True, 3.49)
        self.addItem("Waffles", "Waffles, with your choice of blueberries or strawberries", True, 3.59)

    def addItem(self, name, description, vegetarian, price):
        menu_item = MenuItem.MenuItem(name, description, vegetarian, price)
        self.menu_items.append(menu_item)
    
    def createIterator(self):
        return Iterator.PancakeHouseMenuIterator(self.menu_items)
