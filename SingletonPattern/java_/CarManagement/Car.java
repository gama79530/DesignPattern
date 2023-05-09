package SingletonPattern.java_.CarManagement;

public class Car{
    private int carNo;

    public Car(int carNo){
        this.carNo = carNo;
    }

    public int getCarNo() {
        return this.carNo;
    }

    public void setCarNo(int carNo) {
        this.carNo = carNo;
    }

    public void drive(int clientNo){
        System.out.println(String.format("\tClient %d is driving Car %d.", clientNo, carNo));    
    }
}
