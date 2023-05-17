package CommandPattern.java_.Receiver;

public class Light implements Receiver{
    private boolean state = false;
    
    @Override
    public boolean on() {
        if(!state){
            System.out.println("Light on");
            state = true;
            return true;
        }else{
            System.out.println("Light is already on.");
            return false;
        }
    }

    @Override
    public boolean off() {
        if(state){
            System.out.println("Light off");
            state = false;
            return true;
        }else{
            System.out.println("Light is already off.");
            return false;
        }
    }
}
