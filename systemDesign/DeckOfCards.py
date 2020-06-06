import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def showCard(self):
        print("Card Is", self.suit, "value is", self.value)

    def showRemovedCard(self):
        print(self.suit, self.value)


class Deck:
    def __init__(self):
        self.suitCards = []

    def bultCards(self):
        s = ['Diamond', 'hears', 'spades', 'clubs']
        for i in s:
            for j in range(1, 14):
                value = Card(i, j)
                self.suitCards.append(value)

    def showCards(self):
        for c in self.suitCards:
            c.showCard()

    def drawCard(self):
        print("jbjbj")
        a = self.suitCards.pop()
        return a


class Player:
    def __init__(self, name):
        self.name = name

    def playerName(self):
        value = Deck.drawCard()
        print("PLAYER", self.name, "picked", value.showCard())


class Players:
    def __init__(self):
        self.playerList = []

    def addPlayer(self, name):
        player = Player(name)
        self.playerList.append(player)


class Game:
    def __init__(self):
        self.cards = None
        self.players = None


    def startGame(self):
        self.cards = Deck()
        self.players = Players()

