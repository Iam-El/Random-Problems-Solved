suits = ['D', 'S', 'H', 'C']
numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

import random


class Card:
    def __init__(self, suit, numbers):
        self.numbers = numbers
        self.suit = suit

    def get_number(self):
        return self.numbers

    def get_suit(self):
        return self.suit

    def get_card(self):
        return self.suit+''+self.numbers

class Deck:
    def __init__(self):
        self.deck = []

    def add_card_number(self):
        for i in suits:
            for j in numbers:
                self.deck.append(Card(i, j))

    def display_deck(self):
        print("Deck:-")
        for i in self.deck:
            print(i.get_number(), i.get_suit())

    def count_cards(self):
        return len(self.deck)

    def len(self):
        return len(self.deck)

    def deal(self):
        randomNumber = random.choice(self.deck)
        self.deck.remove(randomNumber)
        return randomNumber


class Player:

    def __init__(self, name):
        self.name = name
        self.card = []

    def get_player_name(self):
        return self.name

    def add_card(self, value):
        self.card.append(value)

    def show_all_cards(self):
        print("player name",self.name)
        for i in self.card:
            print(i.get_card())


class Game:

    def __init__(self):
        self.database = {}
        self.listOfPlayers = []
        self.playerCapacity = 4
        self.deck_of_cards = Deck()

    def add_player(self, name):
        self.player = Player(name)
        if len(self.listOfPlayers) < self.playerCapacity:
            self.listOfPlayers.append(self.player)
        else:
            print("maximum limit for the players is reached")

    def display_player(self):
        for i in self.listOfPlayers:
            print(i.get_player_name())

    def make_card_set(self):
        print(self.deck_of_cards.add_card_number())

    def print_set(self):
        print(self.deck_of_cards.display_deck())

    def generate_random_number(self):
        return self.deck_of_cards.deal()

    def deal_a_card(self):
        count = 13
        self.make_card_set()
        while count > 0:
            for player in self.listOfPlayers:
                value = self.generate_random_number()
                player.add_card(value)
            count = count - 1

    def display_cards(self):
        for player in self.listOfPlayers:
            player.show_all_cards()


# myObj = Deck()
# myObj.add_card_number()
# myObj.display_deck()

myObj = Game()
myObj.add_player("Elsy")
myObj.add_player("Aaron")
myObj.add_player("Kooran")
myObj.add_player("Booran")
myObj.add_player("d")
myObj.display_player()
myObj.make_card_set()
# myObj.print_set()
myObj.deal_a_card()
myObj.display_cards()

