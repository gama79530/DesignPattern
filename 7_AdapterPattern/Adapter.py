import Turkey
import Duck

class DuckAdapter(Turkey.Turkey) :
    def __init__(self, duck) :
        import random
        self.duck = duck
        self.rand = random.randrange

    def gobble(self) :
        self.duck.quack()

    def fly(self) :
        if self.rand(5) :
            self.duck.fly()

class DuckAdapter2(Duck.MallardDuck, Turkey.Turkey) :
    def __init__(self) :
        import random
        self.rand = random.randrange

    def gobble(self) :
        self.quack()

    def fly(self) :
        if self.rand(5) :
            super().fly()

class TurkeyAdapter(Duck.Duck) :
    def __init__(self, turkey) :
        self.turkey = turkey

    def quack(self) :
        self.turkey.gobble()

    def fly(self) :
        for i in range(5) :
            self.turkey.fly()

class TurkeyAdapter2(Turkey.WildTurkey, Duck.Duck) :
    def quack(self) :
        self.gobble()

    def fly(self) :
        for i in range(5) :
            super().fly()
