class Waitress:
    def __init__(self, pancakeHouseMenu, dinerMenu, cafeMenu):
        self.pancakeHouseMenu = pancakeHouseMenu
        self.dinerMenu = dinerMenu
        self.cafeMenu = cafeMenu

    def printMenu(self, iterator=None):
        if iterator:
            while True:
                try:
                    menuItem = next(iterator)
                    print('{}, {} -- {}'.format(menuItem.name, menuItem.price, menuItem.description))
                except StopIteration:
                    break
        else:
            pancakeIterator = iter(self.pancakeHouseMenu)
            dinerIterator = iter(self.dinerMenu)
            cafeIterator = iter(self.cafeMenu)
            print("MENU\n----\nBREAKFAST")
            self.printMenu(pancakeIterator)
            print("\nLUNCH")
            self.printMenu(dinerIterator)
            print("\nDINNER")
            self.printMenu(cafeIterator)
