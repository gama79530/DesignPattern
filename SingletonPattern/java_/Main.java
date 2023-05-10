package SingletonPattern.java_;

import SingletonPattern.java_.CarManagement.*;

public class Main {    
    public static void main(String[] args) throws InterruptedException {
        final class Client extends Thread{
            int clientNo = 0;

            Client(int clientNo){
                this.clientNo = clientNo;
            }
            
            @Override
            public void run() {
                CarManager manager = CarManager.getInstance();
                String info = String.format("\tClient %d rent a car: ", clientNo);
                Car car = manager.rentCar();
                info += (car == null ? "No available car" : String.format("car %d", car.getCarNo()));
                System.out.println(info);
                if(car != null){
                    try {
                        Thread.sleep(20);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                    car.drive(clientNo);
                    car = manager.returnCar(car);
                }
            }
        };

        Client[] clients = new Client[2];
        System.out.println(String.format("Round 1: available car = %d", CarManager.getInstance().getAvailableNumber()));
        for(int i=0; i<2; i++){
            clients[i] = new Client(i);
            clients[i].start();
        }

        for(int i=0; i<2; i++){
            clients[i].join();
        }

        CarManager.getInstance().setCarNumber(2);
        System.out.println(String.format("Round 2: available car = %d", CarManager.getInstance().getAvailableNumber()));
        for(int i=0; i<2; i++){
            clients[i] = new Client(i);
            clients[i].start();
        }

        for(int i=0; i<2; i++){
            clients[i].join();
        }

        CarManager.getInstance().setCarNumber(1);
        System.out.println(String.format("Round 3: available car = %d", CarManager.getInstance().getAvailableNumber()));
        for(int i=0; i<2; i++){
            clients[i] = new Client(i);
            clients[i].start();
        }

        for(int i=0; i<2; i++){
            clients[i].join();
        }
    }
}
