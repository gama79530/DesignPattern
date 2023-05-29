package StatePattern.java_.Taxi;

public class Taxi {
    private State state;
    private OffDutyLights offDutyLights;
    private OnDutyLight onDutyLight;
    private Arrived arrived;

    public Taxi(){
        onDutyLight = new OnDutyLight();
        offDutyLights = new OffDutyLights();
        arrived = new Arrived();
        state = offDutyLights;
    }

    public State getState() {
        return this.state;
    }

    OffDutyLights getOffDutyLights() {
        return this.offDutyLights;
    }

    OnDutyLight getOnDutyLight() {
        return this.onDutyLight;
    }

    Arrived getArrived() {
        return this.arrived;
    }

    public void hailed(){
        System.out.println("Someone hails the taxi.");
        State previouState = state;
        state = state.hailed(this);
        if(previouState != state){
            state = state.drive(this);
        }
    }

    public void checkout(){
        System.out.println("The passenger checkout the bill.");
        state = state.checkout(this);
    }
}
