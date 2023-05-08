import Pizza
import PizzaStore

if __name__ == '__main__':
    pizzaStoreA = PizzaStore.PizzaStoreA()
    pizzaStoreB = PizzaStore.PizzaStoreB()

    print(f"Order {Pizza.PizzaType.CHEESE_PIZZA.value} from store A")
    pizzaStoreA.orderPizza(Pizza.PizzaType.CHEESE_PIZZA, 6)
    print(f"Order {Pizza.PizzaType.PEPPERONI_PIZZA.value} from store A")
    pizzaStoreA.orderPizza(Pizza.PizzaType.PEPPERONI_PIZZA, 8)
    print(f"Order {Pizza.PizzaType.VEGGIE_PIZZA.value} from store A")
    pizzaStoreA.orderPizza(Pizza.PizzaType.VEGGIE_PIZZA, 10)
    print()
    print(f"Order {Pizza.PizzaType.CHEESE_PIZZA.value} from store B")
    pizzaStoreB.orderPizza(Pizza.PizzaType.CHEESE_PIZZA, 10)
    print(f"Order {Pizza.PizzaType.PEPPERONI_PIZZA.value} from store B")
    pizzaStoreB.orderPizza(Pizza.PizzaType.PEPPERONI_PIZZA, 8)
    print(f"Order {Pizza.PizzaType.VEGGIE_PIZZA.value} from store B")
    pizzaStoreB.orderPizza(Pizza.PizzaType.VEGGIE_PIZZA, 6)