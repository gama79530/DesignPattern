import abc

class CPU(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def showInfo(self):
        return NotImplemented
    

class AMD_Ryzen7_3700X(CPU):
    def showInfo(self):
        return "AMD Ryzen7 3700X"