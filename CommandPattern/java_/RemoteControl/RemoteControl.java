package CommandPattern.java_.RemoteControl;

import java.util.*;
import CommandPattern.java_.Command.Command;

public class RemoteControl {
    private Command[] onCommands = new Command[3];
    private Command[] offCommands = new Command[3];
    private Stack<Command> history = new Stack<>();

    public void setOnCommand(Command command, int slot){
        onCommands[slot] = command;
    }

    public void setOffCommand(Command command, int slot){
        offCommands[slot] = command;
    }

    public void pressOnButton(int slot) throws CloneNotSupportedException{
        onCommands[slot].execute();
        history.push(onCommands[slot].clone());
    }

    public void pressOffButton(int slot) throws CloneNotSupportedException{
        offCommands[slot].execute();
        history.push(offCommands[slot].clone());
    }

    public void pressUndo() throws CloneNotSupportedException{
        Command command = null;
        boolean isActed = false;
        while(!history.empty() && !isActed){
            command = history.pop();
            isActed = command.undo();
        }
    }
}
