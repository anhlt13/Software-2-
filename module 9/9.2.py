from sympy.physics.units import acceleration


class Car:
    def __init__(self, registration_number, maximum_speed, current_speed = 0, travelled_distance = 0):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed

    def acceleration(self,change_of_speed: float):
        self.current_speed += change_of_speed
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0


    def print_speed(self):
        print(f"The current speed of the car is: {self.current_speed}")

new_car = Car("ABC-123", 142)
new_car.acceleration(30)
new_car.acceleration(70)
new_car.acceleration(50)
new_car.print_speed()
