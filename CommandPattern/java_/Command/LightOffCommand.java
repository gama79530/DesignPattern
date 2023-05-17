package CommandPattern.java_.Command;

import CommandPattern.java_.Receiver.Receiver;

public class LightOffCommand implements Command{
    private Receiver receiver;
    private boolean hasStatusChange;

    public LightOffCommand(Receiver receiver) {
        this.receiver = receiver;
    }

    @Override
    public void execute() {
        hasStatusChange = receiver.off();
    }

    @Override
    public boolean undo() {
        if(hasStatusChange){
            System.out.print("Undo:\t");
            receiver.on();
            return true;
        }
        return false;
    }

    @Override
    public Command clone() throws CloneNotSupportedException{
        return (Command)super.clone();
    }
}
