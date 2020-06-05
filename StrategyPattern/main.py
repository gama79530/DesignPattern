import Duck
import FlyBehavior

if __name__ == "__main__" :

    mallard = Duck.MallardDuck()
    mallard.display()
    mallard.performQuack()
    mallard.performFly()

    print('----------')

    model_duck = Duck.ModelDuck()
    model_duck.display()
    model_duck.performQuack()
    model_duck.performFly()
    model_duck.flyBehavior = FlyBehavior.FlyRocketPowered()
    model_duck.performFly()
