class Waitress:
    def __init__(self, all_menus):
        self.all_menus = all_menus

    def printMenu(self):
        self.all_menus.print()

    def printVegetarianMenu(self):
        iterator = self.all_menus.createIterator()
        print("\nVEGETARIAN MENU\n----")
        while iterator.hasNext():
            menu_component = iterator.next()
            if menu_component.isVegetarian():
                menu_component.print()