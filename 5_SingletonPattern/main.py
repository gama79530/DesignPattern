import ChocolateBoiler

if __name__ == "__main__":
    boiler = ChocolateBoiler.ChocolateBoiler()
    boiler.fill()
    boiler.boil()
    boiler.drain()

    boiler2 = ChocolateBoiler.ChocolateBoiler()
    print(str((boiler is boiler2)))