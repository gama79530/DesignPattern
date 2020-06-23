import MenuComponent
import Waitress

if __name__ == "__main__":
    pancake_house_menu = MenuComponent.Menu("PANCAKE HOUSE MENU", "Breakfast")
    diner_menu = MenuComponent.Menu("DINER MENU", "Lunch")
    cafe_menu = MenuComponent.Menu("CAFE MENU", "Dinner")
    dessert_menu = MenuComponent.Menu("DESSERT MENU", "Dessert of course!")
    coffee_menu = MenuComponent.Menu("COFFEE MENU", "Stuff to go with your afternoon coffee")
    all_menus = MenuComponent.Menu("ALL MENUS", "All menus combined")

    all_menus.add(pancake_house_menu)
    all_menus.add(diner_menu)
    all_menus.add(cafe_menu)
    diner_menu.add(dessert_menu)
    cafe_menu.add(coffee_menu)

    pancake_house_menu.add(MenuComponent.MenuItem("K&B's Pancake Breakfast", "Pancakes with scrambled eggs, and toast", True, 2.99))
    pancake_house_menu.add(MenuComponent.MenuItem("Regular Pancake Breakfast", "Pancakes with fried eggs, sausage", False, 2.99))
    pancake_house_menu.add(MenuComponent.MenuItem("Blueberry Pancakes", "Pancakes made with fresh blueberries, and blueberry syrup", True, 3.49))
    pancake_house_menu.add(MenuComponent.MenuItem("Waffles", "Waffles, with your choice of blueberries or strawberries", True, 3.59))

    diner_menu.add(MenuComponent.MenuItem("Vegetarian BLT", "(Fakin') Bacon with lettuce & tomato on whole wheat", True, 2.99))
    diner_menu.add(MenuComponent.MenuItem("BLT", "Bacon with lettuce & tomato on whole wheat", False, 2.99))
    diner_menu.add(MenuComponent.MenuItem("Soup of the day", "A bowl of the soup of the day, with a side of potato salad", False, 3.29))
    diner_menu.add(MenuComponent.MenuItem("Hotdog", "A hot dog, with saurkraut, relish, onions, topped with cheese", False, 3.05))
    diner_menu.add(MenuComponent.MenuItem("Steamed Veggies and Brown Rice", "Steamed vegetables over brown rice", True, 3.99))
    diner_menu.add(MenuComponent.MenuItem("Pasta", "Spaghetti with Marinara Sauce, and a slice of sourdough bread", True, 3.89))
    diner_menu.add(dessert_menu)

    dessert_menu.add(MenuComponent.MenuItem("Apple Pie", "Apple pie with a flakey crust, topped with vanilla icecream", True, 1.59))
    dessert_menu.add(MenuComponent.MenuItem("Cheesecake", "Creamy New York cheesecake, with a chocolate graham crust", True, 1.99))
    dessert_menu.add(MenuComponent.MenuItem("Sorbet", "A scoop of raspberry and a scoop of lime", True, 1.89))

    cafe_menu.add(MenuComponent.MenuItem("Veggie Burger and Air Fries", "Veggie burger on a whole wheat bun, lettuce, tomato, and fries", True, 3.99))
    cafe_menu.add(MenuComponent.MenuItem("Soup of the day", "A cup of the soup of the day, with a side salad", False, 3.69))
    cafe_menu.add(MenuComponent.MenuItem("Burrito", "A large burrito, with whole pinto beans, salsa, guacamole", True, 4.29))
    cafe_menu.add(coffee_menu)

    coffee_menu.add(MenuComponent.MenuItem("Coffee Cake", "Crumbly cake topped with cinnamon and walnuts", True, 1.59))
    coffee_menu.add(MenuComponent.MenuItem("Bagel", "Flavors include sesame, poppyseed, cinnamon raisin, pumpkin", False, 0.69))
    coffee_menu.add(MenuComponent.MenuItem("Biscotti", "Three almond or hazelnut biscotti cookies", True, 0.89))

    waitress = Waitress.Waitress(all_menus)
    waitress.printMenu()