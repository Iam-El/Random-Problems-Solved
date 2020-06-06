class Queue:
    def __init__(self):
        self.items=[]

    def insertIntoQueue(self,val):
        self.items.insert(0,val)


    def display(self):
        print(self.items)

    def popelement(self):
        self.items.pop()


    def toelemenet(self):
        print(self.items[-1])




myObj=Queue()
myObj.insertIntoQueue(1)
myObj.insertIntoQueue(2)
myObj.insertIntoQueue(3)
myObj.insertIntoQueue(4)
myObj.insertIntoQueue(5)

myObj.display()

myObj.popelement()

myObj.display()

myObj.toelemenet()





