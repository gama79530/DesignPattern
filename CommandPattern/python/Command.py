import abc
import copy
from Receiver import *

class Command(metaclass=abc.ABCMeta):
    def execute(self) -> None:
        return NotImplemented

    def undo(self) -> bool:
        return NotImplemented
    

class FanOffCommand(Command):
    def __init__(self, receiver:Receiver) -> None:
        super().__init__()
        self._receiver = receiver
        self._hasStatusChange = False

    def execute(self) -> None:
        self._hasStatusChange = self._receiver.off()

    def undo(self) -> bool:
        if self._hasStatusChange:
            print("Undo:\t", end='')
            self._receiver.on()
            return True
        
        return False
    

class FanOnCommand(Command):
    def __init__(self, receiver:Receiver) -> None:
        super().__init__()
        self._receiver = receiver
        self._hasStatusChange = False

    def execute(self) -> None:
        self._hasStatusChange = self._receiver.on()

    def undo(self) -> bool:
        if self._hasStatusChange:
            print("Undo:\t", end='')
            self._receiver.off()
            return True
        
        return False
    

class LightOffCommand(Command):
    def __init__(self, receiver: Receiver) -> None:
        super().__init__()
        self._receiver = receiver
        self._hasStatusChange = False

    def execute(self) -> None:
        self._hasStatusChange = self._receiver.off()

    def undo(self) -> bool:
        if self._hasStatusChange:
            print("Undo:\t", end='')
            self._receiver.on()
            return True
        
        return False
    

class LightOnCommand(Command):
    def __init__(self, receiver: Receiver) -> None:
        super().__init__()
        self._receiver = receiver
        self._hasStatusChange = False

    def execute(self) -> None:
        self._hasStatusChange = self._receiver.on()

    def undo(self) -> bool:
        if self._hasStatusChange:
            print("Undo:\t", end='')
            self._receiver.off()
            return True
        
        return False
    

class MacroCommand(Command):
    def __init__(self, commands:list[Command]) -> None:
        super().__init__()
        self._commands = commands
        self._history:list[Command] = list()
        
    def execute(self) -> None:
        self._history = list()
        for command in self._commands:
            command.execute()
            self._history.append(copy.copy(command))

    def undo(self) -> bool:
        isActed = False
        while self._history:
            command = self._history.pop()
            isActed = isActed or command.undo()

        return isActed

