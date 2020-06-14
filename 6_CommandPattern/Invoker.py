import Command

class RemoteControlWithUndo :
    def __init__(self) :
        no_command = Command.NoCommand()
        self.on_commands = [no_command, no_command, no_command, no_command, no_command, no_command, no_command]
        self.off_commands = [no_command, no_command, no_command, no_command, no_command, no_command, no_command]
        self.undo_command = no_command

    def setCommand(self, slot, on_command, off_command) :
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command

    def onButtonWasPushed(self, slot) :
        self.on_commands[slot].execute()
        self.undo_command = self.on_commands[slot]

    def offButtonWasPushed(self, slot) :
        self.off_commands[slot].execute()
        self.undo_command = self.on_commands[slot]

    def undoButtonWasPushed(self) :
        self.undo_command.undo()

    def __str__(self) :
        result = '\n------ Remote Control -------\n'
        for i in range(len(self.on_commands)) :
            result += ('[slot {}] {}    {}\n'.format(str(i), self.on_commands[i].__class__.__name__, self.off_commands[i].__class__.__name__))
        result += ('[undo] {}\n'.format(self.undo_command.__class__.__name__))
        return result
