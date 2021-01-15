import unittest
from app.PlayerCards import *


class TestCard(unittest.TestCase):
    def setUp(self):
        self.list_player_cards = PlayerCards([
            Card(Rank.Four, Suit.clubs), Card(Rank.K, Suit.spades),
            Card(Rank.Four, Suit.hearts), Card(Rank.Eight, Suit.spades),
            Card(Rank.Seven, Suit.spades)], [Card(Rank.A, Suit.diamonds),
                                             Card(Rank.Four, Suit.spades)])
        self.common = [Card(Rank.Four, Suit.clubs), Card(Rank.K, Suit.spades),
                       Card(Rank.Four, Suit.hearts),
                       Card(Rank.Eight, Suit.spades),
                       Card(Rank.Seven, Suit.spades)]
        self.custom = [Card(Rank.A, Suit.diamonds),
                       Card(Rank.Four, Suit.spades)]
        self.sum = self.common + self.custom
        self.nums = self.list_player_cards.convert_to_nums()

    def test_convert_to_nums(self):
        self.assertEqual(self.nums, [Rank.Four, Rank.K, Rank.Four, Rank.Eight,
                                     Rank.Seven, Rank.A, Rank.Four])

    def test_convert_to_suit(self):
        self.suits = self.list_player_cards.convert_to_suit()
        self.assertEqual(self.suits, [Suit.clubs, Suit.spades, Suit.hearts,
                                      Suit.spades, Suit.spades, Suit.diamonds,
                                      Suit.spades])

    def test_count_rank(self):
        self.assertEqual(self.list_player_cards.count_rank(),
                         [3, 1, 3, 1, 1, 1, 3])

    def test_count_suit(self):
        self.assertEqual(self.list_player_cards.count_suit(),
                         [1, 4, 1, 4, 4, 1, 4])

    def test_is_straight(self):
        self.list_straight = [14, 13, 12, 11, 10, 6, 3]
        self.list_no_straight = [14, 10, 8, 6, 5, 3, 2]
        self.assertEqual(self.list_player_cards.is_straight
                         (self.list_straight), [10, 11, 12, 13, 14])
        self.assertEqual(self.list_player_cards.is_straight
                         (self.list_no_straight), False)

    def test_is_flush(self):
        self.assertEqual(self.list_player_cards.is_flush(), False)
        self.list_player_cards_second = PlayerCards([
            Card(Rank.Four, Suit.clubs), Card(Rank.K, Suit.spades),
            Card(Rank.Four, Suit.hearts), Card(Rank.Eight, Suit.spades),
            Card(Rank.Seven, Suit.spades)], [Card(Rank.A, Suit.spades),
                                             Card(Rank.Four, Suit.spades)])
        self.assertEqual(self.list_player_cards_second.is_flush(),
                         [14, 13, 8, 7, 4])


class TestHighCardHandler(unittest.TestCase):
    def setUp(self):
        self.High_card = HighCardHandler()
        self.list_player_cards = PlayerCards([
            Card(Rank.Four, Suit.clubs), Card(Rank.K, Suit.spades),
            Card(Rank.Four, Suit.hearts), Card(Rank.Eight, Suit.spades),
            Card(Rank.Seven, Suit.spades)], [Card(Rank.A, Suit.diamonds),
                                             Card(Rank.Four, Suit.spades)])

    def test_is_high_card(self):
        self.assertEqual(self.High_card.is_high_card(self.list_player_cards),
                         False)

    def test_handle(self):
        self.assertEqual(self.High_card.handle(self.list_player_cards), None)


class TestPairHandler(unittest.TestCase):
    def setUp(self):
        self.pair = PairHandler()
        self.list_player_cards = PlayerCards([
            Card(Rank.Four, Suit.clubs), Card(Rank.K, Suit.spades),
            Card(Rank.Four, Suit.hearts), Card(Rank.Eight, Suit.spades),
            Card(Rank.Seven, Suit.spades)], [Card(Rank.A, Suit.diamonds),
                                             Card(Rank.Four, Suit.spades)])

    def test_is_pair(self):
        self.assertEqual(self.pair.is_pair(self.list_player_cards), False)

    def test_handle(self):
        self.assertEqual(self.pair.handle(self.list_player_cards), None)


class TestTwoPairsHandler(unittest.TestCase):
    def setUp(self):
        self.two_pairs = TwoPairsHandler()
        self.list_player_cards = PlayerCards([
            Card(Rank.Four, Suit.clubs), Card(Rank.K, Suit.spades),
            Card(Rank.Four, Suit.hearts), Card(Rank.Eight, Suit.spades),
            Card(Rank.Seven, Suit.spades)], [Card(Rank.A, Suit.diamonds),
                                             Card(Rank.Four, Suit.spades)])

    def test_is_two_pair(self):
        self.assertEqual(self.two_pairs.is_two_pairs(self.list_player_cards),
                         False)

    def test_handle(self):
        self.assertEqual(self.two_pairs.handle(self.list_player_cards), None)


class TestThreeKindHandler(unittest.TestCase):
    def setUp(self):
        self.three_kind = ThreeKindHandler()
        self.list_player_cards = PlayerCards([
            Card(Rank.Four, Suit.clubs), Card(Rank.K, Suit.spades),
            Card(Rank.Four, Suit.hearts), Card(Rank.Eight, Suit.spades),
            Card(Rank.Seven, Suit.spades)], [Card(Rank.A, Suit.diamonds),
                                             Card(Rank.Four, Suit.spades)])

    def test_is_three_of_a_kind(self):
        self.assertEqual(self.three_kind.is_three_of_a_kind
                         (self.list_player_cards), True)

    def test_handle(self):
        self.assertEqual(self.three_kind.handle(self.list_player_cards),
                         Combination(4, [4, 4, 4, 14, 13],
                                     self.list_player_cards))


if __name__ == "__main__":
    unittest.main()
