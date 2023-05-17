package CommandPattern.java_.Receiver;

public class Fan implements Receiver{
    private static int MAX_SPEED = 5;
    private int state = 0;

    @Override
    public boolean on() {
        if(state < MAX_SPEED){
            if(++state == MAX_SPEED){
                System.out.println(String.format("The speed of fan is max level (level %d)", state));
            }else{
                System.out.println(String.format("The speed of fan is level %d", state));
            }
            return true;
        }else{
            System.out.println("The current level is maximum.");
            return false;
        }
    }

    @Override
    public boolean off() {
        if(state > 0){
            if(--state == 0){
                System.out.println("The fan is off");
            }else{
                System.out.println(String.format("The speed of fan is level %d", state));
            }
            return true;
        }else{
            System.out.println("The fan is already off.");
            return false;
        }
    }
}
