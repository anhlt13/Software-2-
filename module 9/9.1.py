class Car:
    def __init__(self, registration_number, maximum_speed, current_speed = 0 , travelled_distance = 0):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed

if __name__ == "__main__":
    new_car = Car("ABC-123", 142)
    print(f"the properties of the new car is: {new_car.registration_number}, {new_car.maximum_speed}")