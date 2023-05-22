package FacadePattern.java_.OfficeDevice;

public class Light {
    private static int MAX_LEVEL = 5;
    private boolean isOn = false;
    private int brightness = 1;

    public boolean getIsOn() {
        return this.isOn;
    }

    public int getBrightness() {
        return this.brightness;
    }

    public void on(){
        if(!isOn){
            isOn = true;
            System.out.println("Light is on.");
        }
    }

    public void off(){
        if(isOn){
            isOn = false;
            System.out.println("Light is off.");
        }
    }

    void brightnessUp(){
        if(brightness >= MAX_LEVEL || ++brightness == MAX_LEVEL){
            System.err.println(String.format("The brightness is maximum (level %d).", MAX_LEVEL));
        }else{
            System.out.println(String.format("The brightness is up (level %d).", brightness));
        }
    }

    void brightnessDown(){
        if(brightness <= 1 || --brightness == 1){
            System.err.println("The brightness is minimum (level 1).");
        }else{
            System.out.println(String.format("The brightness is down (level %d).", brightness));
        }
    }
}
