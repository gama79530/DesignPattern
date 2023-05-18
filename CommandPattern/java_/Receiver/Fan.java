package CommandPattern.java_.Receiver;

public class Fan implements Receiver{
    private static int MAX_SPEED = 5;
    private int currentLevel = 0;

    @Override
    public boolean on() {
        if(currentLevel < MAX_SPEED){
            if(++currentLevel == MAX_SPEED){
                System.out.println(String.format("The speed of fan is max level (level %d)", currentLevel));
            }else{
                System.out.println(String.format("The speed of fan is level %d", currentLevel));
            }
            return true;
        }else{
            System.out.println("The current level is already maximum.");
            return false;
        }
    }

    @Override
    public boolean off() {
        if(currentLevel > 0){
            if(--currentLevel == 0){
                System.out.println("The fan is off");
            }else{
                System.out.println(String.format("The speed of fan is level %d", currentLevel));
            }
            return true;
        }else{
            System.out.println("The fan is already off.");
            return false;
        }
    }
}
