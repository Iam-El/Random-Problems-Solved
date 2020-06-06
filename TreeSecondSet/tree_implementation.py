class Node:
    def __init__(self, data=None):
        self.root=None
        self.left = None
        self.right = None
        self.val = data

    # insert tree
    def insertTree(self, value):
        if self.val is None:
            self.val = value
        else:
            if value > self.val:
                if self.right:
                    self.right.insertTree(value)
                else:
                    self.right = Node(value)
            elif value < self.val:
                if self.left:
                    self.left.insertTree(value)
                else:
                    self.left = Node(value)


    # print tree
    def printTree(self):
        print(self.val)
        if self.left:
            self.left.printTree()
        if self.right:
            self.right.printTree()

    # dfs\ depth first search traversal
    def depthFirstSearch(self):
        print(self.val)
        if self.left:
            self.left.depthFirstSearch()
        if self.right:
            self.right.depthFirstSearch()

    def dfsNew(self):
        output = [self]
        print(output)
        while len(output) > 0:
            current = output.pop(0)
            if current.right:
                output.insert(0, current.right)
            if current.left:
                output.insert(0, current.left)
            print(current.val)

    # BFS(breadth first search) # level order traversal
    def breadthFirstSearch(self):
        output = [self]
        while len(output) > 0:
            current = output.pop(0)
            if current.left:
                output.append(current.left)
            if current.right:
                output.append(current.right)
            print(current.val)



    # bfs # level order
    def breadthFirstSearch1(self):
        print(self.val)
        if self.left:
            print(self.left.val)
        if self.right:
            print(self.right.val)

    # Types of depth first search

    # 1) In order traversal

    def inorderTraversal(self):
        if self:
            if self.left:
                self.left.inorderTraversal()
            print(self.val)
            if self.right:
                self.right.inorderTraversal()

    def breadthFirstSearchpreorcder(self):
        cuurent=self
        stack=[]
        while True:
            if cuurent is not None:
                stack.append(cuurent)
                cuurent=cuurent.left
            elif(stack):
                cuurent=stack.pop()
                print(cuurent.val)
                cuurent=cuurent.right
            else:
                break




    # 2) pre order traversal



    # 3) postorder traversal

    def postOrderTraversal(self):
        if self.left:
            self.left.preOrderTraversal()
        if self.right:
            self.right.preOrderTraversal()
        print(self.val)



# Creating object and stuff

    def preOrderTraversal(self,root,string):
        print(self)
        # if root == None:
        #     string=string+"None"
        #     return string
        # else:
        #     stri




        # if self.right:
        #     self.right.preOrderTraversal()

    def pre(self):
        print(self.val)
        if self.left:
            self.left.inorderTraversal()
        if self.right:
            self.right.inorderTraversal()

nodeObj = Node()
nodeObj.insertTree(10)
nodeObj.insertTree(5)
nodeObj.insertTree(11)
nodeObj.insertTree(8)
nodeObj.insertTree(1)
nodeObj.insertTree(3)
nodeObj.insertTree(20)

# nodeObj.preOrderTraversal()
# nodeObj.breadthFirstSearch1()

# nodeObj.insertTree(27)
# nodeObj.insertTree(14)
# nodeObj.insertTree(35)
# nodeObj.insertTree(10)
# nodeObj.insertTree(19)
# nodeObj.insertTree(31)
# nodeObj.insertTree(42)


nodeObj.pre()


# nodeObj.insertTree(3)
# nodeObj.insertTree(9)
# nodeObj.insertTree(20)
# nodeObj.insertTree(15)
# nodeObj.insertTree(7)
# nodeObj.insertTree(31)
# nodeObj.insertTree(42)

# nodeObj.preOrderTraversal()



