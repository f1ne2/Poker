from random import randint
from enum import Enum


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def compare(self, other):
        return self.rank.value - other.rank.value


class Suit(Enum):
    hearts = "hearts"
    diamonds = "diamonds"
    clubs = "clubs"
    spades = "spades"


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


class CardDesk:
    def __init__(self, arr):
        self.arr = arr

    def random_card(self, m):
        amount = set()
        if m > len(self.arr):
            return
        while len(amount) != m:
            j = randint(0, len(self.arr) - 1)
            amount.add(self.arr[j])
        for item in amount:
            print(item.rank.value, item.suit.value)

    def max_card(self):
        x = 0
        top = 0
        max_arr = []
        for j in range(4):
            for k in range(len(self.arr)):
                if self.arr[k].suit.value == suits[j] and x == 0:
                    top = k
                    x = 1
                if self.arr[k].suit.value == suits[j] and x == 1:
                    res = self.arr[top].compare(self.arr[k])
                    if res < 0:
                        top = k
            if x == 0:
                print("No suit")
            else:
                print(self.arr[top].rank.value, self.arr[top].suit.value)
                max_arr.append(top)
            x = 0
            top = 0
        return max_arr

    def min_card(self):
        x = 0
        bottom = 0
        min_arr = []
        for j in range(4):
            for k in range(len(self.arr)):
                if self.arr[k].suit.value == suits[j] and x == 0:
                    bottom = k
                    x = 1
                if self.arr[k].suit.value == suits[j] and x == 1:
                    res = self.arr[bottom].compare(self.arr[k])
                    if res > 0:
                        bottom = k
            if x == 0:
                print("No suit")
            else:
                print(self.arr[bottom].rank.value, self.arr[bottom].suit.value)
                min_arr.append(bottom)
            x = 0
            bottom = 0
        return min_arr


card1 = Card(Suit.hearts, Rank.Two)
card2 = Card(Suit.diamonds, Rank.King)
card3 = Card(Suit.clubs, Rank.Ace)
card4 = Card(Suit.spades, Rank.Seven)
card5 = Card(Suit.clubs, Rank.Five)
card6 = Card(Suit.diamonds, Rank.Jack)
card7 = Card(Suit.hearts, Rank.Three)
card8 = Card(Suit.spades, Rank.Ten)
suits = ["hearts", "diamonds", "clubs", "spades"]
array = [card1, card2, card3, card4, card5, card6, card7, card8]
n = 2
print("Random cards", "\n", "_________________")
CardResult = CardDesk(array)
CardResult.random_card(n)
result = card3.compare(card2)
print("_________________", "\n", "List of cards")
for i in range(len(array)):
    print(array[i].rank.value, array[i].suit.value)
if result == 0:
    print("cards equal")
if result < 0:
    print("the first card < the second card")
if result > 0:
    print("the first card > the second card")
print("_________________", "\n", "Maxcard")
max_output = CardResult.max_card()
print("_________________", "\n", "Mincard")
min_output = CardResult.min_card()
print(max_output, min_output)
