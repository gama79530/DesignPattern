package StatePattern.java_.Taxi;

public class Arrived implements State{
    @Override
    public State hailed(Taxi taxi) {
        System.out.println("\tAlready hailed.");
        return this;
    }

    @Override
    public State drive(Taxi taxi) {
        System.out.println("\tWe are at your destination.");
        return this;
    }

    @Override
    public State checkout(Taxi taxi) {
        System.out.println("\tCheckout the bill.");
        return taxi.getOffDutyLights();
    }
}
