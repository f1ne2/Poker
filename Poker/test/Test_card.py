import unittest
import sys
sys.path.insert(0, "D:/Git/Poker/src")
from Converter import *
from Cards import Rank, Suit
class TestCard(unittest.TestCase):
    def setUp(self):
        self.str1 = "4cKs4h8s7s Ad4s Ac4d As9s Kh10s Qd3d 10c10h"

    def test_divide(self):
        self.assertEqual(divide(self.str1), (['Ad4s', 'Ac4d', 'As9s', 'Kh10s', 'Qd3d', '10c10h'], "4cKs4h8s7s"))

    def test_to_str(self):
        self.set1 = [Rank.Four, Suit.clubs, Rank.K,
        Suit.spades, Rank.Four, Suit.hearts,
        Rank.Eight, Suit.spades, Rank.Seven,
        Suit.spades]
        self.set2 = [Rank.A, Suit.diamonds, Rank.Four, Suit.spades, Rank.A, Suit.clubs,
        Rank.Four, Suit.diamonds, Rank.A, Suit.spades, Rank.Nine, Suit.spades, Rank.K,
        Suit.hearts, Rank.Ten, Suit.spades, Rank.Q, Suit.diamonds,
        Rank.Three, Suit.diamonds, Rank.Ten, Suit.clubs, Rank.Ten, Suit.hearts]
        self.assertEqual(to_str(self.set1, self.set2), ("4cKs4h8s7s", "Ad4s Ac4d As9s Kh10s Qd3d 10c10h"))

    def test_to_player_cards(self):
        self.list1 = ['Ad4s', 'Ac4d', 'As9s', 'Kh10s', 'Qd3d', '10c10h']
        self.str2 = "4cKs4h8s7s"
        self.assertEqual(to_player_cards(self.str2, self.list1), ([Rank.Four, Suit.clubs, Rank.K,
        Suit.spades, Rank.Four, Suit.hearts,
        Rank.Eight, Suit.spades, Rank.Seven,
        Suit.spades], [Rank.A, Suit.diamonds, Rank.Four, Suit.spades, Rank.A, Suit.clubs,
        Rank.Four, Suit.diamonds, Rank.A, Suit.spades, Rank.Nine, Suit.spades, Rank.K,
        Suit.hearts, Rank.Ten, Suit.spades, Rank.Q, Suit.diamonds,
        Rank.Three, Suit.diamonds, Rank.Ten, Suit.clubs, Rank.Ten, Suit.hearts]))


if __name__ == "__main__":
    unittest.main()
