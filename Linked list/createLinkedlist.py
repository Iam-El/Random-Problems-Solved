class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    # Inserting at the End of the Linked List
    def insertatEnd(self, newdata):  # self.head should be node not none for this function
        # newnode=Node(newdata)
        # cur=self.head
        # while cur.next is not None:
        #     cur.next=newnode
        #     cur = cur.next
        # print(cur.next.data)

        if self.head is None:
            self.head = Node(newdata)
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(newdata)

        return self.head

    # insert one by one
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.head is None:
            self.head = NewNode
            return
        laste = self.head
        while (laste.next):
            laste = laste.next
        laste.next = NewNode

    # display the elemets of linked list
    def disply(self):
        elements = []
        cur = self.head
        while cur is not None:
            elements.append(cur.data)
            cur = cur.next
        print(elements)

    # print the elements of the linked list
    def listprint(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next

    # find the length of linked list

    def lengthLinkedlist(self):
        count = 0
        cur = self.head
        while cur is not None:
            count = count + 1
            cur = cur.next
        print(count)

    # delete an item from linked list

    def removeAnItem(self, removedata):
        cur = self.head
        prev = None
        if cur is None:
            raise ValueError("Data not in list")
        while cur is not None:
            if cur.data == removedata:
                if prev is None:
                    self.head = cur.next
                    return
                else:
                    prev.next = cur.next
                    cur = cur.next
            else:
                prev = cur
                cur = cur.next

    # insert at the begining of the list

    # def insertatBeginning(self,newdata):
    #     newnode=Node(newdata)
    #     newnode.next=self.head
    #     self.head=newnode  # why is this . insnt it self.head.next??

    def insertBeginning(self, newdata):

        if self.head is None:
            self.head = Node(newdata)
        else:
            newnode = Node(newdata)
            newnode.next = self.head
            self.head = newnode

    # def search(self, itemtosearch):
    #     print('here')
    #     cur = self.head
    #     found = False
    #     if cur is None:
    #         raise ValueError("Data not in list")
    #     while cur is not None:
    #         if cur.data == itemtosearch:
    #             Found = True
    #             cur = cur.next
    #         else:
    #             cur = cur.next
    #             Found = False
    #     if Found:
    #         print(True)
    #     else:
    #         print(False)
    #

    # def search(self, itemtosearch):
    #     print("item to search",itemtosearch)
    #     current=self.head
    #     while current is not None:
    #         if itemtosearch==

    # insert a node at specific position at linked list

    def insertAtSpecificPosition(self, data, position):  ##  another solution in hackerank
        newnode = Node(data)
        pos = 0
        prev = None
        cur = self.head
        while cur is not None:
            pos = pos + 1
            if pos == position:
                prev = cur
                cur = cur.next
                prev.next = newnode
                newnode.next = cur
                break
            else:
                cur = cur.next

    1 - 1 - 2 - 20 - 5

    #
    def insertAtSpecificPosition(self, data, position):  ##  another solution in hackerank
        prev = None
        current = self.head
        length = 1
        while current is not None:
            if prev == None:
                prev = current
                current = current.next
            if length == position:
                newNode = Node(data)
                newNode.next = prev
                prev = current
                current = current.next
                return newNode.data

            length = length + 1

    # def reverseLinkedList(self,):


# inert newnode in between nodes(Inserting in between two Data Nodes)

# delete at a specfic position

# reverse a linked list


# insert to linked list

list = Linkedlist()

list.insertatEnd(1)
list.insertatEnd(2)
list.insertatEnd(5)
list.insertatEnd(20)

print("done insering")

# display the linked list
list.disply()

print("done displaying")

# find the length of the linked list

list.lengthLinkedlist()

print("done displaying the length")

# delete an item from linked list
print("tesring deletekmkmkmkmkmkmk")

list.disply()
list.removeAnItem(5)
list.disply()
#
# #print after deleteing
#
# list.disply()

# insert at the beginning of the list

list2 = Linkedlist()
list2.insertBeginning(10)
list2.insertBeginning(11)
list2.insertBeginning(12)
list2.disply()

# print the linked list

list.disply()

# search an item in linked list
#
# list.search(20)

# inserting a data and node speciac position

print(list.insertAtSpecificPosition(8, 2))
print("sidddhdyydyydydd")
list.disply()
