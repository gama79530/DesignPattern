import Beverage
import Beverage.Coffee
import Beverage.Condiment

if __name__ == '__main__':
    beverage = Beverage.Condiment.Mocha(Beverage.Condiment.Milk(Beverage.Coffee.HouseBlend()))
    print(f"HouseBlend Coffee with mocha and milk: price = {beverage.get_price()}, cost = {beverage.get_cost()}, profit = {beverage.get_profit()}")
    beverage = Beverage.Coffee.DarkRoast()
    print(f"DarkRoast Coffee without any condiment: price = {beverage.get_price()}, cost = {beverage.get_cost()}, profit = {beverage.get_profit()}")
