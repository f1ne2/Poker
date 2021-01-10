import unittest
from app.Converter import *


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


if __name__ == "__main__":
    unittest.main()