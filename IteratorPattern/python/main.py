from Garage import *

if __name__ == '__main__':
    garage = Garage()
    garage.addVehicle(Motorcycle("Harley", "014X-X54A"))
    garage.addVehicle(Car("Toyota Corolla Altis", "0XS7-7LE5"))
    garage.addVehicle(Car("Nissan GT-R", "1S7W-8A1S"))

    for vehicle in garage:
        print(str(vehicle))
