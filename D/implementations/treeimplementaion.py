class Node:

    def __init__(self,data=None):
        self.right=None
        self.left=None
        self.val=data


    def insertTree(self,val):
        if self.val is None:
            self.val=val
        else:
            if val>self.val:
                if self.right:
                    self.right.insertTree(val)
                else:
                    self.right=Node(val)
                if self.left:
                    self.left.insertTree(val)
                else:
                    self.left=Node(val)

    def depthFirstSearch(self):
        output=[self]
        while len(output)>0:
            current=output.pop()
            if current.right:
                output.insert(0,current.right)
            if current.left:
                output.insert(0,current.left)
            print(current.val)

    def breadthFirstSearch(self):
        output=[self]
        while len(output)>0:
            current=output.pop()
            if current.right:
                output.append(current.right)
            if current.left:
                output.append(current.left)
            print(current.val)

    def inorderTraversal(self):
        if self.left:
            self.left.inorderTraversal()
        print(self.val)
        if self.right:
            self.right.inorderTraversal()

    def inOrderIterative(self):





nodeObj=Node()
nodeObj.insertTree(10)
nodeObj.insertTree(5)
nodeObj.insertTree(11)
nodeObj.insertTree(8)
nodeObj.insertTree(1)
nodeObj.insertTree(3)
nodeObj.insertTree(20)

nodeObj.depthFirstSearch()

print("------------------------")

nodeObj.breadthFirstSearch()

print("In order Traversal recursive")

nodeObj.inorderTraversal()

print("In order Traversal iterative")




