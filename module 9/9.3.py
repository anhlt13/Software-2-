class Car:
    def __init__(self, registration_number, maximum_speed, current_speed = 0, travelled_distance = 0):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def acceleration(self,change_of_speed: float):
        self.current_speed += change_of_speed
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, number_of_hours: float):
         self.travelled_distance = (number_of_hours * self.current_speed) + self.travelled_distance
    def print_drive(self):
        print(f"the total travelled distance: {self.travelled_distance}")

new_car = Car("ABC-123", 142, 60, 2000)
new_car.drive(1.5)
new_car.print_drive()



