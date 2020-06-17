import CaffeineBeverage

if __name__ == "__main__" :
    tea = CaffeineBeverage.TeaWithHook()
    coffee = CaffeineBeverage.CoffeeWithHook()
    print('\nMaking tea...')
    tea.prepareRecipe()
    print('\nMaking coffee...')
    coffee.prepareRecipe()