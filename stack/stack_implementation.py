class stack:
    def __init__(self):
        self.items=[]

    def insertStack(self,val):
        self.items.append(val)

    def displayStack(self):
        print(self.items)

    def removeStack(self):
        self.items.pop()


stackObj=stack()

#insert
stackObj.insertStack(1)
stackObj.insertStack(2)
stackObj.insertStack(3)

#display
stackObj.displayStack()

#remove
stackObj.removeStack()


#display
stackObj.displayStack()


