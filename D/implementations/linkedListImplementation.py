class Node:
    def __init__(self,data):
        self.next=None
        self.data=data


class LinkedList:
    def __init__(self):
        self.head=None

    def insertAtEnd(self,val):
        newNode=Node(val)
        if self.head is None:
            self.head=newNode
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=newNode

    def lengthOfList(self):
        count=0
        current=self.head
        while current is not None:
            current=current.next
            count=count+1
        print("count",count)

    def printList(self):
        element=[]
        current=self.head
        while current is not None:
            element.append(current.data)
            current=current.next
        print(element)

    def insertAtBeginning(self,val):
        newNode=Node(val)
        newNode.next=self.head
        self.head=newNode

    def removeItem(self,val):
        prev=None
        current=self.head
        while current is not None:
            if current.data==val:
                if prev is None:
                    self.head=current.next
                else:
                    prev.next=current.next
            prev=current
            current=current.next

    def removeItemwithIndex(self,index):
        count=1
        current=self.head
        prev=None
        while current is not None:
            if count==index:
                if prev is None:
                    self.head=current.next
                else:
                    prev.next=current.next
            prev=current
            current=current.next
            count=count+1

    def insertAtspecific(self,index,val):
        count=1
        current=self.head
        prev=None
        while current is not None:

            if index==count:
                newNode = Node(val)
                if prev is None:
                    newNode.next = self.head
                    self.head=newNode

                else:
                    prev.next=newNode
                    newNode.next=current
            prev=current
            current=current.next
            count=count+1




# Create a instance

myObj=LinkedList()
myObj.insertAtEnd(5)
myObj.insertAtEnd(6)
myObj.insertAtEnd(8)
myObj.insertAtEnd(20)
myObj.insertAtEnd(21)

myObj.lengthOfList()

myObj.printList()

myObj.insertAtBeginning(7)

myObj.printList()

myObj.removeItem(8)

myObj.printList()

myObj.removeItem(7)

myObj.printList()

myObj.removeItemwithIndex(1)

myObj.printList()

myObj.insertAtspecific(1,10)
myObj.printList()

