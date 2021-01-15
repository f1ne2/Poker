from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional, List
from app.Cards import Card, Rank, Suit
from dataclasses import dataclass


class Combination:
    def __init__(self, force: int, force_high_card: List[int],
                 high_cards: PlayerCards):
        self.force = force
        self.force_high_card = force_high_card
        self.high_cards = high_cards

    def __eq__(self, other):
        return self.force == other.force and \
               self.force_high_card == other.force_high_card and \
               self.high_cards == other.high_cards


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, cards: PlayerCards) -> Optional[Combination]:
        pass


class AbstractHandler(Handler):
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, cards: PlayerCards) -> Optional[Combination]:
        if self._next_handler:
            return self._next_handler.handle(cards)
        return None


class PlayerCards():
    def __init__(self, common_cards: List[Card], custom: List[Card]):
        self.common_cards = common_cards
        self.custom = custom
        self.sum = self.common_cards + self.custom
        self.nums = self.convert_to_nums()
        self.suits = self.convert_to_suit()
        self.hand_num = self.count_rank()
        self.hand_suit = self.count_suit()

    def convert_to_nums(self) -> List[Rank]:
        return [self.sum[i].rank for i in range(len(self.sum))]

    def convert_to_suit(self) -> List[Suit]:
        return [self.sum[i].suit for i in range(len(self.sum))]

    def count_rank(self) -> List[int]:
        return [self.nums.count(cur_sum.rank) for cur_sum in self.sum]

    def count_suit(self) -> List[int]:
        return [self.suits.count(cur_suit.suit) for cur_suit in self.sum]

    def is_straight(self, straight_force: List[int]) -> bool or List[int]:
        chain = 0
        res = []
        if straight_force:
            if straight_force[0] == 14:
                straight_force.append(1)
            for j in range(len(straight_force)-1):
                if straight_force[j]-1 == straight_force[j+1]:
                    chain += 1
                    if chain == 4:
                        for k in range(5):
                            res.append(straight_force[j+1])
                            j -= 1
                        return res
                else:
                    chain = 0
        return False

    def is_flush(self) -> bool or List[int]:
        if self.hand_suit.count(5) > 4 or self.hand_suit.count(6) > 4 or \
                self.hand_suit.count(7) > 4:
            return sorted([self.sum[i].rank.value for i, item in
                           enumerate(self.hand_suit) if item > 4],
                          reverse=True)
        return False


class HighCardHandler(AbstractHandler):
    def is_high_card(self, cards: PlayerCards) -> bool:
        if cards.hand_num.count(1) > 5:
            return True
        return False

    def handle(self, cards: PlayerCards) -> Optional[Combination]:
        if self.is_high_card(cards):
            high_cards = sorted([cards.sum[i].rank.value for i in
                                 range(len(cards.hand_num))],
                                reverse=True)
            return Combination(1, high_cards[0:5], cards)
        return super().handle(cards)


class PairHandler(AbstractHandler):
    def is_pair(self, cards: PlayerCards) -> bool:
        if cards.hand_num.count(2) == 2:
            return True
        return False

    def handle(self, cards: PlayerCards) -> Optional[Combination]:
        if self.is_pair(cards):
            kickers = sorted([cards.sum[i].rank.value for i, item in
                              enumerate(cards.hand_num) if
                              item != 2], reverse=True)
            kickers.insert(0, cards.sum[cards.hand_num.index(2)].rank.value)
            kickers.insert(0, cards.sum[cards.hand_num.index(2)].rank.value)
            return Combination(2, kickers[0:5], cards)
        return super().handle(cards)


class TwoPairsHandler(AbstractHandler):
    def is_two_pairs(self, cards: PlayerCards) -> bool:
        if cards.hand_num.count(2) == 4 or cards.hand_num.count(2) == 6:
            return True
        return False

    def handle(self, cards: PlayerCards) -> Optional[Combination]:
        two_pairs = set()
        kickers = []
        if self.is_two_pairs(cards):
            for i, item in enumerate(cards.hand_num):
                if item == 2:
                    two_pairs.add(cards.sum[i].rank.value)
                else:
                    kickers.append(cards.sum[i].rank.value)

            two_pairs = sorted(list(two_pairs), reverse=True)

            if len(two_pairs) == 3:
                kickers.insert(1, two_pairs[2])
                kickers.insert(2, two_pairs[2])

            kickers = sorted(kickers, reverse=True)
            two_pairs_high = [two_pairs[0], two_pairs[1]]

            for j in range(3):
                two_pairs_high.insert(j+2, kickers[j])
            return Combination(3, two_pairs_high[0:5], cards)
        return super().handle(cards)


class ThreeKindHandler(AbstractHandler):
    def is_three_of_a_kind(self, cards: PlayerCards) -> bool:
        if cards.hand_num.count(3) == 3 or cards.hand_num.count(3) == 6:
            return True
        return False

    def handle(self, cards: PlayerCards) -> Optional[Combination]:
        three_of_a_kind = set()
        kickers = []
        if self.is_three_of_a_kind(cards):
            for i, item in enumerate(cards.hand_num):
                if item == 3:
                    three_of_a_kind.add(cards.sum[i].rank.value)
                else:
                    kickers.append(cards.sum[i].rank.value)

            three_of_a_kind = sorted(list(three_of_a_kind), reverse=True)

            if len(three_of_a_kind) == 2:
                for k in range(3):
                    kickers.insert(k, three_of_a_kind[1])

            kickers = sorted(kickers, reverse=True)
            three_of_a_kind_high = [three_of_a_kind[0], three_of_a_kind[0],
                                    three_of_a_kind[0]]
            three_of_a_kind_high.insert(3, kickers[0])
            three_of_a_kind_high.insert(4, kickers[1])

            return Combination(4, three_of_a_kind_high, cards)
        return super().handle(cards)


class FourOfKindHandler(AbstractHandler):
    def is_four_of_a_kind(self, cards: PlayerCards) -> bool:
        if cards.hand_num.count(4) == 4:
            return True
        return False

    def handle(self, cards: PlayerCards) -> Optional[Combination]:
        if self.is_four_of_a_kind(cards):
            return Combination(8,
                               [cards.sum[cards.hand_num.index(4)].rank.value,
                                0, 0, 0, 0], cards)
        return super().handle(cards)


class StraightHandler(AbstractHandler):
    def handle(self, cards: PlayerCards) -> Optional[Combination]:
        set_straight_force = set()
        for i in range(len(cards.nums)):
            set_straight_force.add(cards.nums[i].value)
            straight_force = sorted(list(set_straight_force), reverse=True)
        if cards.is_straight(straight_force):
            return Combination(5, cards.is_straight(straight_force), cards)
        return super().handle(cards)


class FlushHandler(AbstractHandler):
    def handle(self, cards: PlayerCards) -> Optional[Combination]:
        if cards.is_flush():
            return Combination(6, cards.is_flush(), cards)
        return super().handle(cards)


class FullHouseHandler(AbstractHandler):
    def is_full_house(self, cards: PlayerCards):
        if cards.hand_num.count(2) == 2 and cards.hand_num.count(3) == 3 or \
                cards.hand_num.count(2) == 4 and cards.hand_num.count(3) == 3:
            return True
        return False

    def handle(self, cards: PlayerCards) -> Optional[Combination]:
        if self.is_full_house(cards):
            num_set = [cards.sum[i].rank.value for i, item in
                       enumerate(cards.hand_num) if item == 3]
            num_pair = sorted([cards.sum[i].rank.value for i, item in
                               enumerate(cards.hand_num) if item == 2],
                              reverse=True)
            return Combination(7, [num_set[0], num_pair[0], 0, 0, 0], cards)
        return super().handle(cards)


class StraightFlushHandler(AbstractHandler):
    def handle(self, cards: PlayerCards) -> Optional[Combination]:
        if cards.is_straight(cards.is_flush()):
            return Combination(9, cards.is_straight(cards.is_flush()), cards)
        return super().handle(cards)
