package CommandPattern.java_.Command;

public interface Command extends Cloneable{
    void execute() throws CloneNotSupportedException;
    boolean undo() throws CloneNotSupportedException;
    Command clone() throws CloneNotSupportedException;
}
