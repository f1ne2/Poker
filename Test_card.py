import unittest
from Card_2 import Rank, Card,  Suit, CardDesk


class TestCard(unittest.TestCase):
    def setUp(self):
        self.card1 = Card(Suit.spades, Rank.Three)
        self.card2 = Card(Suit.diamonds, Rank.Seven)

    def test_compare(self):
        self.assertEqual(self.card1.compare(self.card2), -4)


class TestCardDesk(unittest.TestCase):
    def setUp(self):
        self.card1 = Card(Suit.spades, Rank.Three)
        self.card2 = Card(Suit.diamonds, Rank.Seven)
        self.card3 = Card(Suit.clubs, Rank.Eight)
        self.card4 = Card(Suit.hearts, Rank.Ten)
        self.card5 = Card(Suit.clubs, Rank.Queen)
        self.card6 = Card(Suit.diamonds, Rank.Jack)
        self.card7 = Card(Suit.clubs, Rank.King)
        self.card8 = Card(Suit.spades, Rank.Ten)
        self.array = [self.card1, self.card2, self.card3, self.card4,
                      self.card5, self.card6, self.card7, self.card8]
        self.cardResult = CardDesk(self.array)
    def test_max_card(self):
        self.assertEqual(self.cardResult.max_card(), [3, 5, 6, 7])

    def test_min_card(self):
        self.assertEqual(self.cardResult.min_card(), [3, 1, 2, 0])

if __name__ == "__main__":
    unittest.main()