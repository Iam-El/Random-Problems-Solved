class Node:
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.val = value

    def insert(self, value):
        if self.val is None:
            self.val = value
        else:
            if self.val > value:
                if self.left:
                    self.left.insert(value)
                else:
                    self.left = Node(value)
            elif self.val < value:
                if self.right:
                    self.right.insert(value)
                else:
                    self.right = Node(value)

    def print(self):
        output = [self]
        while len(output) > 0:
            current = output.pop(0)
            if current.left:
                output.append(current.left)
            if current.right:
                output.append(current.right)
            print(current.val)

    def printTree(self):
        print(self.val)
        if self.left:
            self.left.printTree()
        if self.right:
            self.right.printTree()



    def bfs(node):
        output = [node]
        while len(output) > 0:
            current = output.pop(0)
            if current.left:
                output.append(current.left)
            if current.right:
                output.append(current.right)
            print(current.val)


    def dfs(node):
        queue=[node]
        while len(queue)>0:
            current=queue.pop(0)
            if current.right:
                queue.insert(0,current.right)
            if current.left:
                queue.insert(0,current.left)

            print(current.val)


obj = Node()
obj.insert(10)
obj.insert(5)
obj.insert(11)
obj.insert(8)
obj.insert(1)
obj.insert(3)
obj.insert(20)

#
obj.dfs()


