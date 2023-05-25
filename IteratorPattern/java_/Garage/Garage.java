package IteratorPattern.java_.Garage;

import java.util.*;

public class Garage {
    private List<Vehicle> vehicles = new ArrayList<>();

    public void addVehicle(Vehicle vehicle){
        vehicles.add(vehicle);
    }

    public Iterator<Vehicle> createIterator(){
        return vehicles.iterator();
    }
}
