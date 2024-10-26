import random
class Car:
    def __init__(self, registration_number, maximum_speed, current_speed = 0, travelled_distance = 0):
        self.registration_number =  registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def drive(self, number_of_hours: float):
         self.travelled_distance = (number_of_hours * self.current_speed) + self.travelled_distance
    def acceleration(self,change_of_speed: float):
        self.current_speed += change_of_speed
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0

car_list=[]
for i in range (10):
    car_list.append(Car("Car ABC-"+str(i+1), random.randint(100,200)))

travelled_distance = 0
while travelled_distance < 10000:
    for car in car_list:
        car.acceleration(random.randint(-10,25))
        car.drive(1.)
        travelled_distance = max(car.travelled_distance, travelled_distance)
for car in car_list:
    print(f"{car.registration_number:6s}: {car.maximum_speed}, {car.travelled_distance}")