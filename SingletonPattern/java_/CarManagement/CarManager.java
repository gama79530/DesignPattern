package SingletonPattern.java_.CarManagement;

import java.util.*;

public class CarManager{
    private static int carSequence = 0;
    private volatile static CarManager carManager = null;
    public static CarManager getInstance(){
        if(carManager == null){
            synchronized (CarManager.class){
                if(carManager == null){
                    carManager = new CarManager();
                    carManager.setCarNumber(1);
                }
            }
        }
        return carManager;
    }

    private CarManager(){}
    
    private int carNumber = 0;
    private int waitForDestroyed = 0;
    private Queue<Car> availableCar = new LinkedList<>();
    private Set<Car> dispatchedCar = new HashSet<>();

    synchronized public int getCarNumber() {
        return carNumber;
    }

    public void setCarNumber(int carNumber) {
        if(carNumber >= 0){
            synchronized(this){
                if(carNumber > this.carNumber){
                    for(int i=carNumber - this.carNumber; i > 0; i--){
                        availableCar.add(new Car(carSequence++));
                    }
                }else if(carNumber < this.carNumber){
                    waitForDestroyed = this.carNumber - carNumber;
                    while(availableCar.poll() != null && --waitForDestroyed > 0);
                }
                this.carNumber = carNumber;
            }
        }
    }

    synchronized public int getAvailableNumber(){
        return availableCar.size();
    }

    synchronized public Car rentCar(){
        Car car = availableCar.poll();
        if(car != null){
            dispatchedCar.add(car);
        }
        return car;
    }

    public Car returnCar(Car car){
        if(car != null){
            synchronized(this){
                if(dispatchedCar.remove(car)){
                    if(waitForDestroyed > 0){
                        waitForDestroyed--;
                    }else{
                        availableCar.add(car);
                    }
                    car = null;
                }
            }
        }

        return car;
    }
}
