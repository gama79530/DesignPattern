import Beverage

if __name__ == "__main__":
    beverage = Beverage.Espresso()
    print('{} ${:.2f}'.format(beverage.getDescription(), beverage.cost()))
    
    beverage2 = Beverage.DarkRoast()
    beverage2 = Beverage.Mocha(beverage2)
    beverage2 = Beverage.Mocha(beverage2)
    beverage2 = Beverage.Whip(beverage2)
    print('{} ${:.2f}'.format(beverage2.getDescription(), beverage2.cost()))
    
    beverage3 = Beverage.HouseBlend()
    beverage3 = Beverage.Soy(beverage3)
    beverage3 = Beverage.Mocha(beverage3)
    beverage3 = Beverage.Whip(beverage3)
    print('{} ${:.2f}'.format(beverage3.getDescription(), beverage3.cost()))