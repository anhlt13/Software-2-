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

class Race:
    def __init__(self,name, distance, car_list):
        self.name = name
        self.distance = distance
        self.car_list = car_list

    def hour_passes(self):
        for car in self.car_list:
            car.acceleration(random.randint(-10,15))
            car.drive(1.)

    def print_status(self):
         print(self.name +":")
         print(
             f"\t{"Register Number":<14}\t|\t{"Max Speed":<12}\t|\t{"Current Speed":<16}|{" travelled_distance ":<15}|")
         print("--------------------------------------------------------------------------------")
         for car in car_list:
             print(
                 f"|\t\t{car.registration_number: <10}\t|\t\t{car.maximum_speed:<8}\t|\t\t{car.current_speed:<11}\t|\t\t{car.travelled_distance:<11}\t|")
         print("---------------------------------------------------------------------------------")


    def race_finished(self):
        for car in self.car_list:
            if car.travelled_distance >=  self.distance:
                return True
            return False
car_list=[]
for i in range (10):
    car_list.append(Car("Car ABC-"+str(i+1), random.randint(100,200)))

race = Race("Grand Demolition Derby", 8000, car_list)
hours = 0
while not race.race_finished():
    race.hour_passes()
    hours +=1
    if hours % 10 == 0:
        print(f"the result after {hours}")
        race.print_status()

race.print_status()
print(f"Race finished after {hours} hours")
