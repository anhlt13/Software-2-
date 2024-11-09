from car import Car
class Electric_Car(Car):
    def __int__(self, registration_number, maximum_speed, capacity):
        super().__init__(registration_number, maximum_speed)
        self.capacity = capacity

class GasoLineCar(Car):
    def __init__(self, registration_number, maximum_speed, volume_tanks):
        super().__init__(registration_number, maximum_speed)
        self.volume_tanks = volume_tanks


e_car = Electric_Car("ABC-15", 180, 52.5)
e_car.acceleration(120)

gas_car = GasoLineCar("ACD-123", 165, 32.3)
gas_car.acceleration(100)

e_car.drive(3)
gas_car.drive(3)
print(f"The electric car drive {e_car.travelled_distance}")
print(f"The gas car drive {gas_car.travelled_distance}")

