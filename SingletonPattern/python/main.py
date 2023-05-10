from CarManagement import *
import threading
import time


def make_task(clientNo):
    def task():
        manager = CarManager()
        car = manager.rentCar()
        print(f"\tClient {clientNo} rent a car: {'No available car' if car is None else car.carNo}")
        if car is not None:
            time.sleep(0.02)
            car.drive(clientNo)
            manager.returnCar(car)

    return task

if __name__ == '__main__':
    clients = [None, None]
    print(f"Round 1: available car = {CarManager().getAvailableNumber()}")
    for i in range(2):
        clients[i] = threading.Thread(target=make_task(i))
        clients[i].start()

    for i in range(2):
        clients[i].join()

    CarManager().carNumber = 2
    print(f"Round 2: available car = {CarManager().getAvailableNumber()}")
    for i in range(2):
        clients[i] = threading.Thread(target=make_task(i))
        clients[i].start()

    for i in range(2):
        clients[i].join()
        
    CarManager().carNumber = 1
    print(f"Round 3: available car = {CarManager().getAvailableNumber()}")
    for i in range(2):
        clients[i] = threading.Thread(target=make_task(i))
        clients[i].start()

    for i in range(2):
        clients[i].join()