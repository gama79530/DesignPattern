import abc

class Old_CPU(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def getName(self) -> str:
        return NotImplemented
    

class Pentium4(Old_CPU):
    def getName(self) -> str:
        return "Pentium 4"