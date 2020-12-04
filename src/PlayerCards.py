from enum import Enum
from Cards import Rank, Suit, Card
from typing import Tuple
from Converter import *


class Force(Enum):
    High_card = 1
    Pair = 2
    Two_pairs = 3
    Set = 4
    Straight = 5
    Flush = 6
    Full_house = 7
    Four_of_a_kind = 8
    Straight_flush = 9


class PlayerCards:
    def __init__(self, common_cards: Tuple[Rank, Suit], custom: Tuple[Rank,
                                                                      Suit]):
        self.common_cards = common_cards
        self.custom = custom
        self.custom2 = [[0] * 14 for i in range(int(len(self.custom)/4))]
        self.force_collection = [0] * int(len(self.custom)/4)
        for f in range(int(len(self.custom)/4)):
            for m in range(len(self.common_cards)):
                self.custom2[f][m] = self.common_cards[m]
        n = 0
        for f in range(int(len(self.custom)/4)):
            for m in range(10, len(self.custom2[f])):
                self.custom2[f][m] = self.custom[n]
                n += 1

    def pairs(self):
        k = 0
        a = 0
        b = 0
        a1 = 0
        b1 = 0
        for i in range(len(self.custom2)):
            for x in range(0, len(self.custom2[i]), 2):
                for y in range(0, len(self.custom2[i]), 2):
                    if x != y:
                        if self.custom2[i][x] == self.custom2[i][y]:
                            k += 1
                            if k == 1:
                                a, b = x, y
                if k == 0 and self.force_collection[i] < 1:
                    self.force_collection[i] = Force.High_card.value
                if k == 1 and self.force_collection[i] == 2:
                    if a != b1 and b != a1:
                        self.force_collection[i] = Force.Two_pairs.value
                if k == 1 and self.force_collection[i] < 2:
                    a1 = a
                    b1 = b
                    self.force_collection[i] = Force.Pair.value
                if k == 2 and self.force_collection[i] < 4:
                    self.force_collection[i] = Force.Set.value
                if k == 3 and self.force_collection[i] < 8:
                    self.force_collection[i] = Force.Four_of_a_kind.value
                k = 0
            a = 0
            b = 0
            a1 = 0
            b1 = 0
        return self.force_collection