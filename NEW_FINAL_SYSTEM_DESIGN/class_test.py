class OurArray:
    def __init__(self):
        self.array = []
        self.count = 0

    def print(self):
        print(self.count)

    def add(self):
        self.count += 1


a = OurArray()
b = OurArray()

a.add()
a.add()

b.add()

a.print()
b.print()