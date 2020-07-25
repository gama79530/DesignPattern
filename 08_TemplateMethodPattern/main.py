import CaffeineBeverage
import CaffeineBeverage2

if __name__ == "__main__" :
    tea = CaffeineBeverage.TeaWithHook()
    coffee = CaffeineBeverage.CoffeeWithHook()
    print('\nMaking tea...')
    tea.prepareRecipe()
    print('\nMaking coffee...')
    coffee.prepareRecipe()
    print('\n ====== non-object-oriented way ======')
    print('\nMaking tea...')
    CaffeineBeverage2.prepare_tea()
    print('\nMaking coffee...')
    CaffeineBeverage2.prepare_coffee()
