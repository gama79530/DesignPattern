import Menu
import Waitress

if __name__ == "__main__":
    pancakeHouse_menu = Menu.PancakeHouseMenu()
    diner_menu = Menu.DinerMenu()
    cafe_menu = Menu.CafeMenu()
    
    waitress = Waitress.Waitress(pancakeHouse_menu, diner_menu, cafe_menu)
    waitress.printMenu()