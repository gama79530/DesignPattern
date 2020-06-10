import Duck
import FlyBehavior

if __name__ == "__main__" :

    mallard_duck = Duck.MallardDuck()
    mallard_duck.display()
    mallard_duck.performQuack()
    mallard_duck.performFly()

    print('----------')

    model_duck = Duck.ModelDuck()
    model_duck.display()
    model_duck.performQuack()
    model_duck.performFly()
    model_duck.fly_behavior = FlyBehavior.FlyRocketPowered()
    model_duck.performFly()
