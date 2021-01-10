from app.Converter import *


class PlayerCards:
    def __init__(self, common_cards: List[Card], custom: List[Card]):
        self.common_cards = common_cards
        self.custom = custom
        self.sum = self.common_cards + self.custom
        self.nums = self.convert_to_nums()
        self.hand_num = self.count_rank()
        self.suits = self.convert_to_suit()
        self.hand_suit = self.count_suit()
        self.force = {}

    def force_hand(self) -> None:
        self.is_high_card()
        self.is_pair()
        self.is_two_pairs()
        self.is_three_of_a_kind()
        self.is_straight(straight=None)
        self.is_flush()
        self.is_full_house()
        self.is_four_of_kind()
        self.is_straight_flush()
        self.is_royal_flush()

    def convert_to_nums(self) -> List[Rank]:
        nums = []
        for i in range(len(self.sum)):
            nums.append(self.sum[i].rank)
        return nums

    def convert_to_suit(self) -> List[Suit]:
        suits = []
        for i in range(len(self.sum)):
            suits.append(self.sum[i].suit)
        return suits

    def count_rank(self) -> List[int]:
        repeated = []
        for i in range(len(self.sum)):
            repeated.append(self.nums.count(self.sum[i].rank))
        return repeated

    def count_suit(self) -> List[int]:
        repeated = []
        for i in range(len(self.sum)):
            repeated.append(self.suits.count(self.sum[i].suit))
        return repeated

    def is_high_card(self) -> None:
        high_cards = []

        if self.hand_num.count(1) > 5:
            for i, item in enumerate(self.hand_num):
                high_cards.append(self.sum[i].rank.value)

            high_cards = sorted(high_cards, reverse=True)
            self.force = [1, high_cards[0:5], self.common_cards, self.custom]

    def is_pair(self) -> None:
        kickers = []

        if self.hand_num.count(2) == 2:
            for i, item in enumerate(self.hand_num):
                if item != 2:
                    kickers.append(self.sum[i].rank.value)

            kickers = sorted(kickers, reverse=True)
            kickers.insert(0, self.sum[self.hand_num.index(2)].rank.value)
            self.force = [2, kickers[0:5], self.common_cards, self.custom]

    def is_two_pairs(self) -> None:
        two_pairs = set()
        kickers = []

        if self.hand_num.count(2) == 4 or self.hand_num.count(2) == 6:
            for i, item in enumerate(self.hand_num):
                if item == 2:
                    two_pairs.add(self.sum[i].rank.value)
                else:
                    kickers.append(self.sum[i].rank.value)

            two_pairs = list(two_pairs)
            two_pairs = sorted(two_pairs, reverse=True)

            if len(two_pairs) == 3:
                kickers.insert(1, two_pairs[2])
                kickers.insert(2, two_pairs[2])

            kickers = sorted(kickers, reverse=True)
            two_pairs_high = [two_pairs[0], two_pairs[1]]

            for j in range(3):
                two_pairs_high.insert(j+2, kickers[j])
            self.force = [3, two_pairs_high[0:5], self.common_cards,
                          self.custom]

    def is_three_of_a_kind(self) -> None:
        three_of_a_kind = set()
        kickers = []

        if self.hand_num.count(3) == 3 or self.hand_num.count(3) == 6:
            for i, item in enumerate(self.hand_num):
                if item == 3:
                    three_of_a_kind.add(self.sum[i].rank.value)
                else:
                    kickers.append(self.sum[i].rank.value)

            three_of_a_kind = list(three_of_a_kind)
            three_of_a_kind = sorted(three_of_a_kind, reverse=True)

            if len(three_of_a_kind) == 2:
                for k in range(3):
                    kickers.insert(k, three_of_a_kind[1])

            kickers = sorted(kickers, reverse=True)
            three_of_a_kind_high = [three_of_a_kind[0]]

            for j in range(4):
                three_of_a_kind_high.insert(j+1, kickers[j])
            self.force = [4, three_of_a_kind_high[0:5], self.common_cards,
                          self.custom]

    def is_straight(self, straight) -> List[int]:
        eq = 0
        set_straight_force = set()
        res = []

        if straight is not None:
            straight_force = straight
        else:
            for i in range(len(self.nums)):
                set_straight_force.add(self.nums[i].value)
            straight_force = list(set_straight_force)
            straight_force.reverse()
        for j in range(len(straight_force)-1):
            if straight_force[j]-1 == straight_force[j+1]:
                eq += 1
                if eq == 4:
                    for k in range(5):
                        res.append(straight_force[j+1])
                        j -= 1
                    self.force = [5, res, self.common_cards, self.custom]
                    return [5, res]
            else:
                eq = 0

    def is_flush(self) -> None:
        flush_force = []

        if self.hand_suit.count(5) > 4 or self.hand_suit.count(6) > 4 or \
                self.hand_suit.count(7) > 4:
            for i, item in enumerate(self.hand_suit):
                if item > 4:
                    flush_force.append(self.sum[i].rank.value)

            flush_force = sorted(flush_force, reverse=True)
            self.force = [6, flush_force, self.common_cards, self.custom]

    def is_full_house(self) -> None:
        num_set = []
        num_pair = []

        if self.hand_num.count(2) == 2 and self.hand_num.count(3) == 3 or \
                self.hand_num.count(2) == 4 and self.hand_num.count(3) == 3:
            for i, item in enumerate(self.hand_num):
                if item == 3:
                    num_set.append(self.sum[i].rank.value)
                if item == 2:
                    num_pair.append(self.sum[i].rank.value)

            num_pair = sorted(num_pair, reverse=True)
            self.force = [7, [num_set[0], num_pair[0], 0, 0, 0],
                          self.common_cards, self.custom]

    def is_four_of_kind(self) -> None:
        if self.hand_num.count(4) == 4:
            for i, item in enumerate(self.hand_num):
                if item == 4:
                    self.force = [8, [self.sum[i].rank.value, 0, 0, 0, 0],
                                  self.common_cards, self.custom]

    def is_straight_flush(self) -> None:
        if self.force[0] == 6:
            straight_flush_force = self.is_straight(self.force[1])
            try:
                if straight_flush_force[0] == 5:
                    self.force = [9, straight_flush_force[1],
                                  self.common_cards, self.custom]
            except:
                pass

    def is_royal_flush(self) -> None:
        if self.force[0] == 9:
            if self.force[1][0] == 10 and self.force[1][4] == 14:
                self.force = [10, [0, 0, 0, 0, 0], self.common_cards,
                              self.custom]
