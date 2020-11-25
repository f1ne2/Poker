from enum import Enum


class Suit(Enum):
    hearts = "h"
    diamonds = "d"
    clubs = "c"
    spades = "s"


class Rank(Enum):
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    J = 11
    Q = 12
    K = 13
    A = 14


class Card:
    def __init__(self, suit: Suit, rank: Rank):
        self.suit = suit
        self.rank = rank

    def compare(self, other: Rank):
        return self.rank.value - other.rank.value


class Converter:
    def __init__(self, cards: str):
        self.cards = cards

    def players_cards(self):
        cards_ = self.cards.split(" ", 1)
        table = cards_[0]
        players = cards_[1].split()
        return table, players

    def hands(self, hands_: list):
        return " ".join(hands_)

str1 = "4cKs4h8s7s Ad4s Ac4d As9s Kh10s Qd3d 10c10h"
cards_input = Converter(str1)
table_cards, players_card = cards_input.players_cards()
hands_output = Converter(str1)
str_hands = hands_output.hands(players_card)