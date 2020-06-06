class deckOfCards:
    def __init__(self):
        self.carNum=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        self.cardTypes=[u"\u1F49C",u"\u2660",u"\u2660",u"\u2660"]

    def createDeckOfCards(self,typeOfCrad):
        displayDeckOfcrads=[]
        if typeOfCrad not in self.cardTypes:
            raise Exception('This card Type doesnt exist')
        else:
            for i in range(0,len(self.carNum)):
                displayDeckOfcrads.append(self.carNum[i])

        return displayDeckOfcrads

    def allCards(self):
        dispalyAllCards=[]
        for i in self.cardTypes:
            for j in self.carNum:
                dispalyAllCards.append(j+i)
        return dispalyAllCards

    def lengthOfCards(self,value):
        print(len(value))



myobj=deckOfCards()
# print(myobj.createDeckOfCards('spade'))
res=(myobj.allCards())
print(res)
myobj.lengthOfCards(res)