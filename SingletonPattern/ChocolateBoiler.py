import threading

singleton_lock = threading.Lock()

class ChocolateBoiler :
    _instance = None

    def __new__(cls) :
        singleton_lock.acquire()
        if cls._instance is None :
            cls._instance = super().__new__(cls)
        singleton_lock.release()
        return cls._instance

    def __init__(self) :
        self.empty = True
        self.boiled = False

    def fill(self) :
        if self.empty :
            self.empty = False
            self.boiled = False
            print('Fill the boiler with a milk/chocolate mixture')

    def drain(self) :
        if not self.empty and self.boiled :
            self.empty = True
            print('Drain the boiled milk and chocolate')

    def boil(self) :
        if not self.empty and not self.boiled :
            self.boiled = True
            print('Bring the contents to a boil')
