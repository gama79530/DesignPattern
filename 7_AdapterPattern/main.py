import Adapter
import Duck
import Turkey

if __name__ == "__main__":
    duck = Duck.MallardDuck()
    turkey = Turkey.WildTurkey()
    print('--- Turkey Adapter ---')
    turkey_adapter = Adapter.TurkeyAdapter(turkey)
    turkey_adapter2 = Adapter.TurkeyAdapter2()
    print("\nThe Duck says...")
    turkey.gobble()
    turkey.fly()
    print("\nThe Duck says...")
    duck.quack()
    duck.fly()
    print("\nThe Turkey Adapter says...")
    turkey_adapter.quack()
    turkey_adapter.fly()
    print("\nThe Turkey Adapter 2 says...")
    turkey_adapter2.quack()
    turkey_adapter2.fly()
    print('\n--- Duck Adapter ---')
    duck_adapter = Adapter.DuckAdapter(duck)
    duck_adapter2 = Adapter.DuckAdapter2()
    print("\nThe Duck Adapter says...")
    for i in range(5) :
        duck_adapter.gobble()
        duck_adapter.fly()
    print("\nThe Duck Adapter 2 says...")
    for i in range(5) :
        duck_adapter2.gobble()
        duck_adapter2.fly()