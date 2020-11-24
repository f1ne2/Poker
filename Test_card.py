import unittest
from Card import Rank, Card,  Suit


class TestCard(unittest.TestCase):
    def setUp(self):
        self.card1 = Card(Suit.spades, Rank.Three)
        self.card2 = Card(Suit.diamonds, Rank.Seven)

    def test_compare(self):
        self.assertEqual(self.card1.compare(self.card2), -4)

if __name__ == "__main__":
    unittest.main()