import Beverage

if __name__ == '__main__':
    beverage = Beverage.Mocha(Beverage.Milk(Beverage.HouseBlend()))
    print(f"HouseBlend Coffee with mocha and milk: price = {beverage.getPrice()}, cost = {beverage.getCost()}, profit = {beverage.getProfit()}")
    beverage = Beverage.DarkRoast()
    print(f"DarkRoast Coffee without any condiment: price = {beverage.getPrice()}, cost = {beverage.getCost()}, profit = {beverage.getProfit()}")
