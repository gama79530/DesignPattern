package StatePattern.java_.Taxi;

interface State{
    State hailed(Taxi taxi);
    State drive(Taxi taxi);
    State checkout(Taxi taxi);
}