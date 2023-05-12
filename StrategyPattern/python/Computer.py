import abc

class CPU(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def showInfo(self):
        return NotImplemented
    

class AMD_Ryzen7_3700X(CPU):
    def showInfo(self):
        return "AMD Ryzen7 3700X"
    

class GPU(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def showInfo(self):
        return NotImplemented


class NVIDIA_GeForce_GTX_1660_SUPER(GPU):
    def showInfo(self):
        return "NVIDIA GeForce GTX 1660 SUPER"


class Computer:
    def __init__(self) -> None:
        self.cpu:CPU = None
        self.gpu1:GPU = None
        self.gpu2:GPU = None

    def showInfo(self):
        print("The component of this computer")
        print(f'CPU   : {self.cpu.showInfo()}')
        print(f'GPU 1 : {"None" if self.gpu1 is None else self.gpu1.showInfo()}')
        print(f'GPU 2 : {"None" if self.gpu2 is None else self.gpu2.showInfo()}')
        
