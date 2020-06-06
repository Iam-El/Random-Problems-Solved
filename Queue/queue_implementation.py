#queue data structure
#first in First out

class Queue:
    def __init__(self):
        self.items=[]

    def queueInsert(self,val):
        self.items.insert(0,val)

    def displayQueue(self):
        print(self.items)

    def removeElements(self):
        self.items.pop()




# create Queue object
queueObj=Queue()


# insert items into Queue
queueObj.queueInsert(4)
queueObj.queueInsert(2)
queueObj.queueInsert(3)


# display the Queue
queueObj.displayQueue()


# remove the items from queue
queueObj.removeElements()

# display the Queue
queueObj.displayQueue()

