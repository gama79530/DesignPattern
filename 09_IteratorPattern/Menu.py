"""
    # All classes should extend Menu
# """
import abc
import MenuItem

class Menu(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __iter__(self):
        pass

class CafeMenu(Menu):
    def __init__(self):
        self._menuItems = {}
        self.addItem("Veggie Burger and Air Fries", "Veggie burger on a whole wheat bun, lettuce, tomato, and fries", True, 3.99)
        self.addItem("Soup of the day", "A cup of the soup of the day, with a side salad", False, 3.69)
        self.addItem("Burrito", "A large burrito, with whole pinto beans, salsa, guacamole", True, 4.29)

    def addItem(self, name, description, vegetarian, price):
        menuItem = MenuItem.MenuItem(name, description, vegetarian, price)
        self._menuItems[menuItem.name] = menuItem

    def __iter__(self):
        return iter(self._menuItems.values())

class DinerMenu(Menu):
    def __init__(self):
        self._maxItems = 6
        self._menuItems = []
        self.addItem("Vegetarian BLT", "(Fakin') Bacon with lettuce & tomato on whole wheat", True, 2.99)
        self.addItem("BLT", "Bacon with lettuce & tomato on whole wheat", False, 2.99)
        self.addItem("Soup of the day", "Soup of the day, with a side of potato salad", False, 3.29)
        self.addItem("Hotdog", "A hot dog, with saurkraut, relish, onions, topped with cheese", False, 3.05)
        self.addItem("Steamed Veggies and Brown Rice", "Steamed vegetables over brown rice", True, 3.99)
        self.addItem("Pasta", "Spaghetti with Marinara Sauce, and a slice of sourdough bread", True, 3.89)

    def addItem(self, name, description, vegetarian, price):
        if len(self._menuItems) >= self._maxItems:
            print("Sorry, menu is full! Can't add item to menu")
        else:
            menuItem = MenuItem.MenuItem(name, description, vegetarian, price)
            self._menuItems.append(menuItem)

    def __iter__(self):
        return iter(self._menuItems)

class PancakeHouseMenu(Menu):
    def __init__(self):
        self._menuItems = []
        self.addItem("K&B's Pancake Breakfast", "Pancakes with scrambled eggs, and toast", True, 2.99)
        self.addItem("Regular Pancake Breakfast", "Pancakes with fried eggs, sausage", False, 2.99)
        self.addItem("Blueberry Pancakes", "Pancakes made with fresh blueberries", True, 3.49)
        self.addItem("Waffles", "Waffles, with your choice of blueberries or strawberries", True, 3.59)

    def addItem(self, name, description, vegetarian, price):
        menuItem = MenuItem.MenuItem(name, description, vegetarian, price)
        self._menuItems.append(menuItem)

    def __iter__(self):
        return iter(self._menuItems)
