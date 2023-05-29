package StatePattern.java_.Taxi;

public class OffDutyLights implements State{
    @Override
    public State hailed(Taxi taxi) {
        System.out.println("\tPassenger board on the taxi.");
        
        return taxi.getOnDutyLight();
    }

    @Override
    public State drive(Taxi taxi) {
        System.out.println("\tNo passenger...");
        return this;    
    }

    @Override
    public State checkout(Taxi taxi) {
        System.out.println("\tNo passenger...");
        return this;    
    }
}
