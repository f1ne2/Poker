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
        self.force_collection = [0] * int(len(self.custom)/4)

    def redefine(self):
        n = 0
        self.custom2 = [[0] * 14 for i in range(int(len(self.custom) / 4))]
        for f in range(int(len(self.custom)/4)):
            for m in range(len(self.custom2[f])):
                if m < len(self.common_cards):
                    self.custom2[f][m] = self.common_cards[m]
                else:
                    self.custom2[f][m] = self.custom[n]
                    n += 1
        return self.custom2

    def is_pairs(self, h):
        repeated = []
        for i in range(0, len(h), 2):
            repeated.append(h.count(h[i]))
        if repeated.count(2) == 2:
            return True
        return False

    def is_two_pairs(self, h):
        repeated = []
        for i in range(0, len(h), 2):
            repeated.append(h.count(h[i]))
        if repeated.count(2) == 4 or repeated.count(2) == 6 or repeated.count(2) == 8:
            return True
        return False

    def is_set(self, h):
        repeated = []
        for i in range(0, len(h), 2):
            repeated.append(h.count(h[i]))
        if repeated.count(3) == 3 or repeated.count(3) == 6:
            return True
        return False

    def is_four_of_kind(self, h):
        repeated = []
        for i in range(0, len(h), 2):
            repeated.append(h.count(h[i]))
        if repeated.count(4) == 4:
            return True
        return False

    def is_high_card(self, h):
        repeated = []
        for i in range(0, len(h), 2):
            repeated.append(h.count(h[i]))
        if repeated.count(1) > 5:
            return True
        return False

    def is_full_house(self, h):
        repeated = []
        for i in range(0, len(h), 2):
            repeated.append(h.count(h[i]))
        if repeated.count(2) == 2 and repeated.count(3) == 3 \
                or repeated.count(2) == 4 and repeated.count(3) == 3:
            return True
        return False

    def is_flush(self, h):
        repeated = []
        for i in range(1, len(h), 2):
            repeated.append(h.count(h[i]))
        if repeated.count(5) > 4:
            return True
        return False

    def is_straight(self, h):
        rank = []
        eq = 0
        for i in range(0, len(h), 2):
            rank.append(h[i].value)
        rank.sort()
        for j in range(len(rank)-1):
            if rank[j]+1 == rank[j+1]:
                eq += 1
        if eq == 4:
            return True
        return False

    def is_straight_flush(self, h, flush):
        if flush:
            rank = []
            eq = 0
            for i in range(0, len(h), 2):
                rank.append(h[i].value)
            rank.sort()
            for j in range(len(rank) - 1):
                if rank[j] + 1 == rank[j + 1]:
                    eq += 1
            if eq == 4:
                return True
            return False












