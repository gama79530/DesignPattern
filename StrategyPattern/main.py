import Duck
import FlyBehavior

if __name__ == "__main__" :

    mallard = Duck.MallardDuck()
    mallard.display()
    mallard.perform_quack()
    mallard.perform_fly()

    print('----------')

    model_duck = Duck.ModelDuck()
    model_duck.display()
    model_duck.perform_quack()
    model_duck.perform_fly()
    model_duck.flyBehavior = FlyBehavior.FlyRocketPowered()
    model_duck.perform_fly()
