class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.parking_spots = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.parking_spots[carType-1] >= 1:
            self.parking_spots[carType-1] -= 1
            return True
        return False


"""
Your ParkingSystem object will be instantiated and called as such:
obj = ParkingSystem(big, medium, small)
param_1 = obj.addCar(carType)

Input
["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
[[1, 1, 0], [1], [2], [3], [1]]
Output
[null, true, true, false, false]
"""
