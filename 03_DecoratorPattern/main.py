import Beverage
import BaseBeverage
import Condiment

if __name__ == "__main__":
    beverage = BaseBeverage.Espresso()
    print('{} ${:.2f}'.format(beverage.description, beverage.cost()))
    
    beverage2 = BaseBeverage.DarkRoast()
    beverage2 = Condiment.Mocha(beverage2)
    beverage2 = Condiment.Mocha(beverage2)
    beverage2 = Condiment.Whip(beverage2)
    print('{} ${:.2f}'.format(beverage2.description, beverage2.cost()))
    
    beverage3 = BaseBeverage.HouseBlend()
    beverage3 = Condiment.Soy(beverage3)
    beverage3 = Condiment.Mocha(beverage3)
    beverage3 = Condiment.Whip(beverage3)
    print('{} ${:.2f}'.format(beverage3.description, beverage3.cost()))
