class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.parking = [0]
        self.parking.append(big) #1
        self.parking.append(medium) #2
        self.parking.append(small) #3

    def addCar(self, carType: int) -> bool:
        if self.parking[carType] == 0:
            return False
        self.parking[carType] -= 1
        return True
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)