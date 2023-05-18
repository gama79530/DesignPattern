package CommandPattern.java_;

import java.util.*;
import CommandPattern.java_.Receiver.*;
import CommandPattern.java_.Command.*;
import CommandPattern.java_.RemoteControl.*;

class Main{
    public static void main(String[] args) throws CloneNotSupportedException {
        Light light = new Light();
        Fan fan = new Fan();
        
        RemoteControl remoteControl = new RemoteControl();
        List<Command> commands = new ArrayList<>();
        commands.add(new LightOnCommand(light));
        commands.add(new FanOnCommand(fan));
        remoteControl.setOnCommand(new LightOnCommand(light), 0);
        remoteControl.setOnCommand(new FanOnCommand(fan), 1);
        remoteControl.setOnCommand(new MacroCommand(commands), 2);
        
        commands = new ArrayList<>();
        commands.add(new LightOffCommand(light));
        commands.add(new FanOffCommand(fan));
        remoteControl.setOffCommand(new LightOffCommand(light), 0);
        remoteControl.setOffCommand(new FanOffCommand(fan), 1);
        remoteControl.setOffCommand(new MacroCommand(commands), 2);

        System.out.println("Button set 1");
        remoteControl.pressOnButton(0);
        remoteControl.pressOffButton(0);

        System.out.println("\nButton set 2");
        remoteControl.pressOnButton(1);
        remoteControl.pressOnButton(1);
        remoteControl.pressOnButton(1);
        remoteControl.pressOnButton(1);
        remoteControl.pressOnButton(1);
        remoteControl.pressOnButton(1);
        remoteControl.pressOffButton(1);
        remoteControl.pressUndo();

        System.out.println("\nButton set 3");
        remoteControl.pressOnButton(2);
        remoteControl.pressOffButton(2);
        remoteControl.pressOffButton(2);
        remoteControl.pressUndo();
        remoteControl.pressUndo();
        remoteControl.pressUndo();
        remoteControl.pressUndo();
    }
}