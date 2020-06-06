suits = ['D', 'S', 'H', 'C']
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
import random


class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def get_suite(self):
        return self.suit

    def set_suite(self, suit):
        self.suit = suit

    def get_number(self):
        return self.number

    def set_number(self, number):
        self.number = number

    def showObject(self):
        return (self.number, self.suit)


class Deck:
    def __init__(self):
        self.deckOfCards = []

    def make_set(self):
        for i in suits:
            for j in cards:
                self.deckOfCards.append(Card(i, j))

    def showSet(self):
        print(self.deckOfCards)
        for i in self.deckOfCards:
            print(i.showObject())

    def get_dec_of_cards(self):
        return (self.deckOfCards)


class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def get_name(self):
        return self.name

    def add_card(self, card):
        self.cards.append(card)

    def set_name(self, name):
        self.name = name

    def player_name_display(self):
        return "PLAYER IS:-", self.name

    def store_player_name(self):
        self.list_of_player.update({self.name: 0})

    def get_player_list(self):
        return (self.list_of_player)

    def show_all_cards(self):
        print("Name", self.name)
        for card in self.cards:
            print(card.get_number() + card.get_suite())


class Game:
    def __init__(self):
        print("Start Game")
        self.list_of_player = []
        self.deckofCards = Deck()
        self.deckofCards.make_set()
        self.totalCards = self.deckofCards.get_dec_of_cards()

    def add_player(self, name):
        player = Player(name)
        self.list_of_player.append(player)
        return player.player_name_display()

    def pickACard(self, name):
        ranValue = random.choice(self.totalCards)
        return (ranValue.showObject())

    def deal_a_card(self):
        count = 13
        while count > 0:
            for player in self.list_of_player:
                selected_card = random.choice(self.totalCards)
                print(selected_card)
                player.add_card(selected_card)
                self.totalCards.remove(selected_card)
            count -= 1




    def print_cards_of_players(self):
        for player in self.list_of_player:
            player.show_all_cards()
            
    def show_list_of_player(self):
        return self.list_of_player


game = Game()
print(game.add_player("Elsy"))
print(game.add_player("Aaron"))
print(game.add_player("Kooran"))
print(game.add_player("Booran"))

game.deal_a_card()

game.print_cards_of_players()

# print(game.pickAPlayer("Elsy"))
# print(game.pickAPlayer("Aaron"))
# print("Elsy picked",game.pickACard("Elsy"))
# print("Aaron picked",game.pickACard("Aaron"))
