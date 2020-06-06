import sys

class MinStack:

    def __init__(self):
        self.s = []
        self.minx=[]

    def push(self, x):
        print("value of x" ,x)
        self.s.append(x)
        if not self.minx:
            self.minx.append(x)
        else:
            if x < self.minx[0]:
                self.minx.append(x)
            else:
                self.minx.insert(0,x)
        print("x",x)
        print("sorted",self.minx.sort())


    def display(self):
        print(self.minx)


    def pop(self):
        poppedval=self.s.pop()
        print(poppedval)
        if  poppedval in self.minx:
            self.minx.remove(poppedval)

    def getMin(self):
        pop=self.minx.pop(0)
        print(pop)



a=MinStack()
a.push(-2)
a.push(0)
a.push(-1)
a.display()
a.getMin()
a.pop()
a.display()
a.getMin()

# a.pop()
# a.display()
# a.getMin()




