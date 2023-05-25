package IteratorPattern.java_.Garage;

public class Car implements Vehicle{
    private String description;
    private String licensePlateNumber;
    
    public Car(String description, String licensePlateNumber) {
        this.description = description;
        this.licensePlateNumber = licensePlateNumber;
    }

    @Override
    public String getDescription() {
        return this.description;
    }
    
    @Override
    public String getLicensePlateNumber() {
        return this.licensePlateNumber;
    }

    @Override
    public String toString() {
        return String.format("Car:%s, license plate number: %s", description, licensePlateNumber);
    }
}
