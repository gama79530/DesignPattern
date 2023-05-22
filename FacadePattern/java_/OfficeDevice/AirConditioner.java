package FacadePattern.java_.OfficeDevice;

public class AirConditioner {
    private static int MAX_TEMPERATURE = 30;
    private static int MIN_TEMPERATURE = 16;
    private boolean isOn = false;
    private int temperature = MAX_TEMPERATURE;
    
    public boolean getIsOn(){
        return isOn;
    }
    
    public int getTemperature(){
        return temperature;
    }

    public void on(){
        if(!isOn){
            isOn = true;
            System.out.println("Air Conditioner is on.");
        }
    }

    public void off(){
        if(isOn){
            isOn = false;
            System.out.println("Air Conditioner is off.");
        }
    }

    public void temperatureUp(){
        if(temperature >= MAX_TEMPERATURE || ++temperature == MAX_TEMPERATURE){
            System.err.println(String.format("The temperature is maximum (%d Celsius).", MAX_TEMPERATURE));
        }else{
            System.out.println(String.format("The temperature is up (%d Celsius).", temperature));
        }
    }

    public void temperatureDown(){
        if(temperature <= MIN_TEMPERATURE || --temperature == MIN_TEMPERATURE){
            System.err.println(String.format("The temperature is minimun (%d Celsius).", MIN_TEMPERATURE));
        }else{
            System.out.println(String.format("The temperature is down (%d Celsius).", temperature));
        }
    }
}
