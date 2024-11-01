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

#test elevator
print(f"Exercise 10.1")
h = Elevator(1,9)
print("---------------------------------------------------------------------------------------------")
print(f"Going to the 4th floor")
h.go_to_floor(4)
print("---------------------------------------------------------------------------------------------")
print(f"going to the bottom floor")
h.go_to_floor(1)





