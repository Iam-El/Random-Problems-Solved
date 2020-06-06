level = ['1', '2', '3']
parking_spot = ['A', 'B', 'C']


class Vehicle:
    def __init__(self, name, licence_plate, type):
        self.name = name
        self.licence_plate = licence_plate
        self.color = type

    def get_name(self):
        return self.get_name

    def get_licence_plate(self):
        return self.licence_plate

    def get_type(self):
        return self.get_type


class Car(Vehicle):
    def __init__(self, name, licence_plate, type):
        super().__init__(name, licence_plate, type)


class Motorcycle(Vehicle):
    def __init__(self, name, licence_plate, type):
        super().__init__(name, licence_plate, type)


class Spot:
    def __init__(self, name, level, isVailable=True):
        self.name = name
        self.level = level
        self.isVailable = isVailable

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def check_availabe(self):
        return self.isVailable

    def set_available(self, isVailable):
        self.isVailable = isVailable


class ParkingSpots:
    def __init__(self):
        self.parking_spots = []
        self.user_spot=[]

    def merge_spots(self):
        for i in level:
            for j in parking_spot:
                self.parking_spots.append(Spot(i, j))

    def available_spots(self):
        for i in self.parking_spots:
            print("Available slots are " + i.get_name(), i.get_level(), i.check_availabe())

    def add_level(self,spot,level):
        self.user_spot.append(Spot(spot, level))

    def display_level(self):
        self.user_spot.get_level()

    def provide_parking_spots(self):
        return self.parking_spots

    def book_spot(self, level, spot):
        for i in self.parking_spots:
            if i.get_level() == level and i.get_name() == spot and i.check_availabe() == True:
                i.set_available(False)
                return i
            elif i.get_level() == level and i.get_name() == spot and i.check_availabe() == False:
                return False


class ParkingLot:

    def __init__(self):
        self.parking_spots = ParkingSpots()
        self.booked_spots = {}

    def check_available_spots(self):
        self.parking_spots.merge_spots()

    def book_spot(self, name, licence_plate, type, level, spot):
        vehicle_car = Car(name, licence_plate, type)
        # self.check_available_spots()
        value = self.parking_spots.book_spot(level, spot)
        if value != False:
            self.booked_spots[licence_plate] = {'name': vehicle_car, 'booked_spot': ParkingSpots()}
            print("slot is booked !!")
            print("check other available slots are:-")

            print(self.booked_spots[licence_plate]['name'].get_licence_plate())
            print(self.booked_spots[licence_plate]['booked_spot'].add_level(spot, level))
            self.parking_spots.available_spots()
        else:
            print("Slot is not available")


myObj = ParkingLot()
myObj.check_available_spots()
myObj.book_spot("Murano", "LP1", "Car", "B", "1")
# myObj.book_spot("Murano", "LP2", "Car", "B", "1")
