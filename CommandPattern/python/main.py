import Receiver
import Command
import RemoteControl

if __name__ == '__main__':
    light = Receiver.Light()
    fan = Receiver.Fan()

    remoteControl = RemoteControl.RemoteControl()
    commands = list()
    commands.append(Command.LightOnCommand(light))
    commands.append(Command.FanOnCommand(fan))
    remoteControl.setOnCommand(Command.LightOnCommand(light), 0)
    remoteControl.setOnCommand(Command.FanOnCommand(fan), 1)
    remoteControl.setOnCommand(Command.MacroCommand(commands), 2)
    
    commands = list()
    commands.append(Command.LightOffCommand(light))
    commands.append(Command.FanOffCommand(fan))
    remoteControl.setOffCommand(Command.LightOffCommand(light), 0)
    remoteControl.setOffCommand(Command.FanOffCommand(fan), 1)
    remoteControl.setOffCommand(Command.MacroCommand(commands), 2)

    print("Button set 1")
    remoteControl.pressOnButton(0)
    remoteControl.pressOffButton(0)
    
    print("\nButton set 2")
    remoteControl.pressOnButton(1)
    remoteControl.pressOnButton(1)
    remoteControl.pressOnButton(1)
    remoteControl.pressOnButton(1)
    remoteControl.pressOnButton(1)
    remoteControl.pressOnButton(1)
    remoteControl.pressOffButton(1)
    remoteControl.pressUndo()

    print("\nButton set 3")
    remoteControl.pressOnButton(2)
    remoteControl.pressOffButton(2)
    remoteControl.pressOffButton(2)
    remoteControl.pressUndo()
    remoteControl.pressUndo()
    remoteControl.pressUndo()
    remoteControl.pressUndo()
