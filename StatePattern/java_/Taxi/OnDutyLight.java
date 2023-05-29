package StatePattern.java_.Taxi;

public class OnDutyLight implements State{
    @Override
    public State hailed(Taxi taxi) {
        System.out.println("\tAlready hailed.");
        return this;
    }

    @Override
    public State drive(Taxi taxi) {
        System.out.println("\tTake passenger to their destination.");
        return taxi.getArrived();
    }

    @Override
    public State checkout(Taxi taxi) {
        System.out.println("\tThe passenger's destination is not arrived.");
        return this;
    }
}
