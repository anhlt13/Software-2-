class Elevator:


    def __init__(self,  bottom_floor:int, top_floor:int):
        self.current_floor = bottom_floor
        self.top_floor = top_floor
    def floor_up(self):
        self.current_floor +=1
        print(f"Elevator is in {self.current_floor} floor")
    def floor_down(self):
        self.current_floor -=1
        print(f"Elevator is in {self.current_floor} floor")
    def go_to_floor(self,target_floor):
        while self.current_floor != target_floor:
            if self.current_floor < target_floor:
                self.floor_up()
            else:
                self.floor_down()

class Building:
    def __init__(self, bottom_floor: int, top_floor: int, num_elevator: int):
        self.current_floor = bottom_floor
        self.top_floor = top_floor
        self.elevator_list = []
        for i in range(num_elevator):
            self.elevator_list.append(Elevator(self.current_floor, self.top_floor))

    def run_elevator(self, id_elevator, destination):
        print("---------------------------------------------------------------------------------------------")
        print(f"choose the elevator number {id_elevator} to go to the floor {destination} ")
        selected_ele = self.elevator_list[id_elevator - 1]
        selected_ele.go_to_floor(destination)

    def fire_alarm(self):
        for elevator in self.elevator_list:
            while elevator.current_floor > self.current_floor:
                elevator.floor_down()
# test building
building = Building(1,10,3)

#test elevator runs:
building.run_elevator(1,3)

print("---------------------------------------------------------------------------------------------")
#test fire_alarm
print(f"the building has a fire")
building.fire_alarm()

