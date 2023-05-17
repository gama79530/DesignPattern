package CommandPattern.java_.Command;

import java.util.*;

public class MacroCommand implements Command{
    private List<Command> commands;
    private Stack<Command> history;
    
    public MacroCommand(List<Command> commands) {
        this.commands = commands;
    }

    @Override
    public void execute() throws CloneNotSupportedException{
        history = new Stack<>();
        for(Command command: commands){
            command.execute();
            history.push(command.clone());
        }
    }

    @Override
    public boolean undo() throws CloneNotSupportedException {
        boolean isActed = false;
        Command command = null;
        while(!history.empty()){
            command = history.pop();
            isActed = isActed || command.undo();
        }

        return isActed;
    }

    public Command clone() throws CloneNotSupportedException{
        return (Command)super.clone();
    }
}
