package IteratorPattern.java_;

import java.util.*;
import IteratorPattern.java_.Garage.*;

public class Main {
    public static void main(String[] args) {
        Garage garage = new Garage();
        garage.addVehicle(new Motorcycle("Harley", "014X-X54A"));
        garage.addVehicle(new Car("Toyota Corolla Altis", "0XS7-7LE5"));
        garage.addVehicle(new Car("Nissan GT-R", "1S7W-8A1S"));

        for(Iterator<Vehicle> iterator = garage.createIterator(); iterator.hasNext();){
            System.out.println(iterator.next());
        }
    }
}
