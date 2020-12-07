from Cards import Rank, Suit, Card
from typing import Tuple
from Converter import *

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

    def is_straight_flush(self, h):
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


class Sort:
    def __init__(self, custom2: Tuple[Rank,Suit]):
        self.custom2 = custom2

    def partition(self, arr, low, high):
        pivot = arr[high]
        j = low - 1
        for i in range(low, high):
            if arr[i] <= pivot:
                j += 1
                arr[j], arr[i] = arr[i], arr[j]
                self.custom2[j], self.custom2[i] = self.custom2[i], self.custom2[j]
        arr[j + 1], arr[high] = arr[high], arr[j + 1]
        self.custom2[j+1], self.custom2[high] = self.custom2[high], self.custom2[j+1]
        return j+1

    def quick_sort(self, arr, low, high):
        if low < high:
            pivotal = Sort.partition(self, arr, low, high)
            Sort.quick_sort(self, arr, low, pivotal - 1)
            Sort.quick_sort(self, arr, pivotal + 1, high)













