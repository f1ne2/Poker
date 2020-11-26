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
    Jack = 11
    Queen = 12
    King = 13
    Ace = 14


class Card:
    def __init__(self, suit: Suit, rank: Rank):
        self.suit = suit
        self.rank = rank

    def compare(self, other: Rank):
        return self.rank.value - other.rank.value

