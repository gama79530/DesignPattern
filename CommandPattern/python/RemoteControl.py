import copy
from Command import *

class RemoteControl:
    def __init__(self) -> None:
        self._onCommands:list[Command] = [None, None, None]
        self._offCommands:list[Command] = [None, None, None]
        self._history:list[Command] = list()

    def setOnCommand(self, command:Command, slot:int) -> None:
        self._onCommands[slot] = command

    def setOffCommand(self, command:Command, slot:int) -> None:
        self._offCommands[slot] = command

    def pressOnButton(self, slot:int) -> None:
        self._onCommands[slot].execute()
        self._history.append(copy.copy(self._onCommands[slot]))

    def pressOffButton(self, slot:int) -> None:
        self._offCommands[slot].execute()
        self._history.append(copy.copy(self._offCommands[slot]))

    def pressUndo(self) -> None:
        isActed = False
        while self._history and not isActed:
            command = self._history.pop()
            isActed = command.undo()


