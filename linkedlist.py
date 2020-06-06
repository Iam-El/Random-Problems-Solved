class Node(object):

    def __init__(self, data, n=None):
        self.data = data
        self.next_node = n


class Linkelist:
    def __init__(self):
        self.head = None

    def insert(self,newnode):
        if self.head is None:
            self.head=newnode
        else:
            self.head



#    firstnode.data=1 firstnode.next_node=None

firstnode = Node('1')
print(firstnode.data)
Linkelist.insert(firstnode)
