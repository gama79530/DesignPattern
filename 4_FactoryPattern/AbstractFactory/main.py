import PizzaStore

if __name__ == "__main__":
    nyStore = PizzaStore.NYPizzaStore()
    chicagoStore = PizzaStore.ChicagoPizzaStore()

    pizza = nyStore.orderPizza("cheese")
    print('Ethan ordered a {}\n'.format(str(pizza)))
 
    pizza = chicagoStore.orderPizza("cheese")
    print('Joel ordered a {}\n'.format(str(pizza)))
    
    pizza = nyStore.orderPizza("clam")
    print('Ethan ordered a {}\n'.format(str(pizza)))
 
    pizza = chicagoStore.orderPizza("clam")
    print('Joel ordered a {}\n'.format(str(pizza)))

    pizza = nyStore.orderPizza("pepperoni")
    print('Ethan ordered a {}\n'.format(str(pizza)))
 
    pizza = chicagoStore.orderPizza("pepperoni")
    print('Joel ordered a {}\n'.format(str(pizza)))

    pizza = nyStore.orderPizza("veggie")
    print('Ethan ordered a {}\n'.format(str(pizza)))
 
    pizza = chicagoStore.orderPizza("veggie")
    print('Joel ordered a {}\n'.format(str(pizza)))