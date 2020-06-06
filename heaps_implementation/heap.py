class heap:
    def __init__(self):
        self.items=[]


    def insert(self,key):
        index=len(self.items)
        print(index)
        self.items.append(key)

        while(index!=0):
            p=(index-1)//2
            if self.items[p]>self.items[index]:
                self.items[p],self.items[index]=self.items[index],self.items[p]
            index=p
        print(self.items)




myObj=heap()
print(myObj)
myObj.insert(5)
myObj.insert(3)
myObj.insert(-3)
myObj.insert(10)
myObj.insert(8)