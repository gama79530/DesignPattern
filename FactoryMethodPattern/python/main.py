import Pizza
import PizzaStore

if __name__ == '__main__':
    pizzaStoreA = PizzaStore.PizzaStoreA()
    pizzaStoreB = PizzaStore.PizzaStoreB()

    print(f"Order {Pizza.PizzaType.CheesePizza.value} from store A")
    pizzaStoreA.orderPizza(Pizza.PizzaType.CheesePizza, 6)
    print(f"Order {Pizza.PizzaType.PepperoniPizza.value} from store A")
    pizzaStoreA.orderPizza(Pizza.PizzaType.PepperoniPizza, 8)
    print(f"Order {Pizza.PizzaType.VeggiePizza.value} from store A")
    pizzaStoreA.orderPizza(Pizza.PizzaType.VeggiePizza, 10)
    print()
    print(f"Order {Pizza.PizzaType.CheesePizza.value} from store B")
    pizzaStoreB.orderPizza(Pizza.PizzaType.CheesePizza, 10)
    print(f"Order {Pizza.PizzaType.PepperoniPizza.value} from store B")
    pizzaStoreB.orderPizza(Pizza.PizzaType.PepperoniPizza, 8)
    print(f"Order {Pizza.PizzaType.VeggiePizza.value} from store B")
    pizzaStoreB.orderPizza(Pizza.PizzaType.VeggiePizza, 6)