package CommandPattern.java_.Receiver;

public class Light implements Receiver{
    private boolean isOn = false;
    
    @Override
    public boolean on() {
        if(!isOn){
            System.out.println("Light on");
            isOn = true;
            return true;
        }else{
            System.out.println("Light is already on.");
            return false;
        }
    }

    @Override
    public boolean off() {
        if(isOn){
            System.out.println("Light off");
            isOn = false;
            return true;
        }else{
            System.out.println("Light is already off.");
            return false;
        }
    }
}
