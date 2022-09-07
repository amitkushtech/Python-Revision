from site import venv


class Vehicle:
    def __init__(self, max_speed, mileage):
        self.maxS = max_speed
        self.mileage = mileage


car = Vehicle(1200, "40 KM")
print("The speed is: ", car.maxS)
print("The mileage is: ", car.mileage)


class MyVehicle:
    pass


veh = MyVehicle()
print(veh)
