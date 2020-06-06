import random

cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suites = ['D', 'S', 'H', 'C']


class Card:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value


class Player:
    def __init__(self, index, name):
        self.index = index
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_index(self):
        return self.index

    def set_index(self, index):
        self.index = index


class Suite:
    def __init__(self, suite):
        self.suite = suite
        self.cardsList = []

        for i in cards:
            self.cardsList.append(Card(i))

    def get_suite(self):
        return self.suite

    def get_card_list(self):
        return self.cardsList

    def get_card(self):
        card = random.choice(self.cardsList)
        self.cardsList.remove(card)
        return card.get_value() + self.suite

    def is_empty(self):
        return len(self.cardsList) == 0


class Deck:
    def __init__(self):
        self.suites = []
        for suite in suites:
            self.suites.append(Suite(suite))

    def get_card(self):
        suite = random.choice(self.suites)
        print(suite.get_card())



deck=Deck()


# card = Card(1)
#
# print(card.get_value())
# card.set_value(10)
# print(card.get_value())
#
# suite = Suite("Diamond")
# print(suite.get_suite())
# print(suite.get_card())
#
# for i in suite.get_card_list():
#     print(i.get_value())