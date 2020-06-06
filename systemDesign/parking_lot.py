class User:
    def __init__(self, fn, email):
        self.fn = fn
        self.email = email

    def get_name(self):
        return self.fn

    def get_email(self):
        return self.email


class Vehicle:
    pass


class Car(Vehicle):
    pass


class Bus(Vehicle):
    pass


class Motorcycle(Vehicle):
    pass


class ParkingSpot:

    def __init__(self, number):
        self.number = number
        self.isFull = False
        # self.parking_spot_level=Level(parking_spots)

    def parking_spot(self):
        return self.number

    def print(self):
        print(self.number, self.isFull)


class Level:

    def __init__(self, level):
        self.level = level
        self.parking_spot = []

    def get_level(self):
        return self.level

    def add_parking_spot(self, number):
        self.parking_spot.append(ParkingSpot(number))

    def print(self):
        print("Level Name", self.level)
        for i in self.parking_spot:
            i.print()

    # def add_parking_spot(self):


class ParkingLot:
    def __init__(self):
        self.database = {}
        self.session = {}
        self.levels = []

    def addlevel(self, level):
        self.levels.append(Level(level))

    def getLevel(self, level):
        for j in self.levels:
            if j.get_level() == level:
                return j

    def register(self, fn, email):
        user_name = User(fn, email)
        self.database[email] = user_name
        print("Registered Successfully!")

    def login(self, email):
        if email not in self.session:
            self.session = self.database[email]
            print("Login Successful!!")
            return self.session.get_email()
        else:
            print("Register!!!!")

    def check_user(self):
        if self.session.get_email():
            return "Currently logged in as", self.session.get_email()
        else:
            return "Logged out"

    def logout_user(self):
        del self.session
        print("user logged out!!")

    def print(self):
        for i in self.levels:
            i.print()

    # def book_parking_spot(self):


level = ['A', 'B', 'C']
parking_spots = [1, 2, 3, 4, 5]

myObj = ParkingLot()
for i in level:
    myObj.addlevel(i)
    currentLevel = myObj.getLevel(i)
    print(currentLevel)
    for j in parking_spots:
        currentLevel.add_parking_spot(j)

# myObj.print()

myObj.register("Elsy", "elsyfernandes215@gmail.com")
print(myObj.login("elsyfernandes215@gmail.com"))
print(myObj.check_user())
