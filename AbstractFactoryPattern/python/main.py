from PizzaStore import *
from PizzaStore.Pizza import *

if __name__ == '__main__':
    pizzaStoreA = PizzaStoreA()
    pizzaStoreB = PizzaStoreB()

    pizza = pizzaStoreA.orderPizza(PizzaType.CHEESE_PIZZA)
    print(f"Order {pizza.getName()}")
    print(f"The ingredient of pizza are: {pizza.showIngredients()}")
    print()
    pizza = pizzaStoreB.orderPizza(PizzaType.CHEESE_PIZZA)
    print(f"Order {pizza.getName()}")
    print(f"The ingredient of pizza are: {pizza.showIngredients()}")


