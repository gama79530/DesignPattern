"""
    # All classes should extend CaffeineBeverage
"""
import abc

class CaffeineBeverageWithHook(metaclass=abc.ABCMeta) :
    def prepareRecipe(self):
        self.boilWater()
        self.brew()
        self.pourInCup()
        if self.customerWantsCondiments():
            self.addCondiments()

    def boilWater(self):
        print("Boiling water")

    def customerWantsCondiments(self):
        return True

    def pourInCup(self):
        print("Pouring into cup")

    @abc.abstractmethod
    def addCondiments(self):
        pass

    @abc.abstractmethod
    def brew(self):
        pass

class CoffeeWithHook(CaffeineBeverageWithHook):
    def brew(self):
        print('Dripping Coffee through filter')

    def addCondiments(self):
        print("Adding Sugar and Milk")

    def customerWantsCondiments(self):
        ans = self.getUserInput()
        return ans.lower().startswith('y')

    def getUserInput(self):
        ans = input("Would you like milk and sugar with your coffee (y/n)? ")
        return ans

class TeaWithHook(CaffeineBeverageWithHook):
    def brew(self):
        print('Steeping the tea')

    def addCondiments(self):
        print("Adding Lemon")

    def customerWantsCondiments(self):
        ans = self.getUserInput()
        return ans.lower().startswith('y')

    def getUserInput(self):
        ans = input("Would you like lemon with your tea (y/n)? ")
        return ans