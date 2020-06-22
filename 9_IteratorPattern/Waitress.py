class Waitress:
    def __init__(self, pancakeHouseMenu, dinerMenu, cafeMenu):
        self.pancakeHouseMenu = pancakeHouseMenu
        self.dinerMenu = dinerMenu
        self.cafeMenu = cafeMenu
    
    def printMenu(self, iterator=None):
        if iterator:
            while (iterator.hasNext()):
                menu_item = iterator.next()
                print('{}, {} -- {}'.format(menu_item.name, menu_item.price, menu_item.description))
        else:
            pancakeIterator = self.pancakeHouseMenu.createIterator()
            dinerIterator = self.dinerMenu.createIterator()
            cafeIterator = self.cafeMenu.createIterator()
            print("MENU\n----\nBREAKFAST")
            self.printMenu(pancakeIterator)
            print("\nLUNCH")
            self.printMenu(dinerIterator)
            print("\nDINNER")
            self.printMenu(cafeIterator)