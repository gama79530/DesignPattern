class Computer:
    def __init__(self) -> None:
        self.cpu = None
        self.gpu1 = None
        self.gpu2 = None

    def showInfo(self):
        print("The component of this computer")
        print(f'CPU   : {self.cpu.showInfo()}')
        print(f'GPU 1 : {"None" if self.gpu1 is None else self.gpu1.showInfo()}')
        print(f'GPU 2 : {"None" if self.gpu2 is None else self.gpu2.showInfo()}')
        
