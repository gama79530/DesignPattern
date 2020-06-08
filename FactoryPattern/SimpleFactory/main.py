import SimplePizzaFactory
import PizzaStore

if __name__ == "__main__":
    factory = SimplePizzaFactory.SimplePizzaFactory()
    store = PizzaStore.PizzaStore(factory)
    pizza = store.orderPizza("cheese")
    print("We ordered a {}\n".format(pizza.name))
    pizza = store.orderPizza("veggie")
    print("We ordered a {}\n".format(pizza.name))