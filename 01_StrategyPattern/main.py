import Duck
import FlyBehavior

if __name__ == "__main__":

    mallard_duck = Duck.MallardDuck()
    mallard_duck.display()
    mallard_duck.quack()
    mallard_duck.fly()
    print('----------')
    model_duck = Duck.ModelDuck()
    model_duck.display()
    model_duck.quack()
    model_duck.fly()
    print('----- change fly behavior at runtime -----')
    model_duck.setFly(FlyBehavior.flyRocketPowered)
    model_duck.fly()
