package FacadePattern.java_.OfficeDevice;

public class WaterDispenser {
    private boolean isOn = false;
    
    public boolean getIsOn(){
        return isOn;
    }

    public void on(){
        if(!isOn){
            isOn = true;
            System.out.println("Water Dispenser is on.");
        }
    }

    public void off(){
        if(isOn){
            isOn = false;
            System.out.println("Water Dispenser is off.");
        }
    }
}
