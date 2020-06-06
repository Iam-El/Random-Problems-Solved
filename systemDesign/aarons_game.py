import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def showCard(self):
        print("Card Is", self.suit, "value is", self.value)

    def showRemovedCard(self):
        print(self.suit, self.value)

    def getCard(self):
        return str(self.suit)+str(self.value)


class Deck:
    def __init__(self):
        self.suitCards = []

    def builtCards(self):
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
        print("PLAYER", self.name)

    def getPlayerName(self):
        return self.name

    # def playerName(self):
    #     value = Deck.drawCard()
    #     print("PLAYER", self.name, "picked", value.showCard())


class Players:
    def __init__(self):
        self.playerList = []

    def addPlayer(self, name):
        player = Player(name)
        self.playerList.append(player)

    def printPlayers(self):
        print("The current players in the game are")
        for player in self.playerList:
            player.playerName()


class Game:
    def __init__(self):
        self.deck = None
        self.players = None


    def startGame(self):
        self.deck = Deck()
        self.deck.builtCards()
        self.players = Players()

    def addPlayer(self, name):
        self.players.addPlayer(name)

    def drawCardForEachPlayer(self):
        for player in self.players.playerList:
            card = self.deck.drawCard()
            print(player.getPlayerName(), "drew", card.getCard())

    def currentPlayers(self):
        self.players.printPlayers()


game = Game()
game.startGame()
game.addPlayer("Aaron")
game.addPlayer("Elsy")
game.currentPlayers()
game.drawCardForEachPlayer()