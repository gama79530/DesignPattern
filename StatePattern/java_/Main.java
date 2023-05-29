package StatePattern.java_;

import StatePattern.java_.Taxi.Taxi;

class Main{
    public static void main(String[] args) {
        Taxi taxi  = new Taxi();
        taxi.hailed();
        taxi.checkout();
        taxi.hailed();
        taxi.hailed();
        taxi.checkout();
        taxi.checkout();
    }
}