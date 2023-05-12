import PizzaStore

if __name__ == '__main__':
    pizzaStoreA = PizzaStore.PizzaStoreA()
    pizzaStoreB = PizzaStore.PizzaStoreB()

    print(f"Order {PizzaStore.PizzaType.CHEESE_PIZZA.value} from store A")
    pizzaStoreA.orderPizza(PizzaStore.PizzaType.CHEESE_PIZZA, 6)
    print(f"Order {PizzaStore.PizzaType.PEPPERONI_PIZZA.value} from store A")
    pizzaStoreA.orderPizza(PizzaStore.PizzaType.PEPPERONI_PIZZA, 8)
    print(f"Order {PizzaStore.PizzaType.VEGGIE_PIZZA.value} from store A")
    pizzaStoreA.orderPizza(PizzaStore.PizzaType.VEGGIE_PIZZA, 10)
    print()
    print(f"Order {PizzaStore.PizzaType.CHEESE_PIZZA.value} from store B")
    pizzaStoreB.orderPizza(PizzaStore.PizzaType.CHEESE_PIZZA, 10)
    print(f"Order {PizzaStore.PizzaType.PEPPERONI_PIZZA.value} from store B")
    pizzaStoreB.orderPizza(PizzaStore.PizzaType.PEPPERONI_PIZZA, 8)
    print(f"Order {PizzaStore.PizzaType.VEGGIE_PIZZA.value} from store B")
    pizzaStoreB.orderPizza(PizzaStore.PizzaType.VEGGIE_PIZZA, 6)