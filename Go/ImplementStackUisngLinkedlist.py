
# stack is first in Last out
# /LIFO-Last in first out


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class stack:
    def __init__(self):
        self.head=None

    def stackPush(self,data):
        if self.head is None:
            self.head=Node(data)
        else:
            newNode=Node(data)
            newNode.next=self.head
            self.head=newNode


    def display(self):
        firstNode=self.head
        while firstNode is not None:
            print(firstNode.data ,"->",end=" ")
            firstNode=firstNode.next


    def stackPop(self):
        popNode=self.head
        nextNode=self.head.next
        self.head=nextNode
        popNode.next=None
        print("\n")
        print(popNode.data)



myobj=stack()

myobj.stackPush(12)
myobj.stackPush(10)
myobj.stackPush(5)

myobj.display()

myobj.stackPop()

myobj.display()


