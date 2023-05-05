import abc

class GPU(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def showInfo(self):
        return NotImplemented


class NVIDIA_GeForce_GTX_1660_SUPER(GPU):
    def showInfo(self):
        return "NVIDIA GeForce GTX 1660 SUPER"