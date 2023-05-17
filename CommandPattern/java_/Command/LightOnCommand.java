package CommandPattern.java_.Command;

import CommandPattern.java_.Receiver.Receiver;

public class LightOnCommand implements Command{
    private Receiver receiver;
    private boolean hasStatusChange;

    public LightOnCommand(Receiver receiver) {
        this.receiver = receiver;
    }

    @Override
    public void execute() {
        hasStatusChange = receiver.on();
    }

    @Override
    public boolean undo() {
        if(hasStatusChange){
            System.out.print("Undo:\t");
            receiver.off();
            return true;
        }
        return false;
    }

    @Override
    public Command clone() throws CloneNotSupportedException{
        return (Command)super.clone();
    }
}
