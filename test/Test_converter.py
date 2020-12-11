import unittest
from app.Converter import *
from app.Cards import Card


class TestCard(unittest.TestCase):
    def setUp(self):
        self.str1 = "Ad4s"
        self.str2 = "4cKs4h8s7s Ad4s Ac4d As9s KhKd 5d6d"
        self.list_player_cards = [PlayerCards([
            Card(Rank.Four, Suit.clubs), Card(Rank.K, Suit.spades),
            Card(Rank.Four,Suit.hearts), Card(Rank.Eight, Suit.spades),
            Card(Rank.Seven, Suit.spades)],[Card(Rank.A, Suit.diamonds),
                                            Card(Rank.Four, Suit.spades)]),
            PlayerCards([Card(Rank.Four, Suit.clubs), Card(Rank.K, Suit.spades),
             Card(Rank.Four, Suit.hearts), Card(Rank.Eight, Suit.spades),
             Card(Rank.Seven, Suit.spades)], [Card(Rank.A, Suit.clubs),
                                              Card(Rank.Four, Suit.diamonds)]),
            PlayerCards([Card(Rank.Four, Suit.clubs), Card(Rank.K, Suit.spades),
             Card(Rank.Four, Suit.hearts), Card(Rank.Eight, Suit.spades),
             Card(Rank.Seven, Suit.spades)], [Card(Rank.A, Suit.spades),
                                              Card(Rank.Nine, Suit.spades)]),
            PlayerCards([Card(Rank.Four, Suit.clubs), Card(Rank.K, Suit.spades),
             Card(Rank.Four, Suit.hearts), Card(Rank.Eight, Suit.spades),
             Card(Rank.Seven, Suit.spades)], [Card(Rank.K, Suit.hearts),
                                                 Card(Rank.K, Suit.diamonds)]),
            PlayerCards([Card(Rank.Four, Suit.clubs), Card(Rank.K, Suit.spades),
             Card(Rank.Four, Suit.hearts), Card(Rank.Eight, Suit.spades),
             Card(Rank.Seven, Suit.spades)], [Card(Rank.Five, Suit.diamonds),
                                              Card(Rank.Six, Suit.diamonds)])]

    # Transfer string to List[Card(Rank, Suit)]
    def test_to_card(self):
        self.assertEqual(to_cards(self.str1), [Card(Rank.A, Suit.diamonds),
                                               Card(Rank.Four, Suit.spades)])

    # Transfer input string to List[PlayerCards]
    def test_to_player_cards(self):
        self.assertEqual(to_player_cards(self.str2), [PlayerCards([
            Card(Rank.Four, Suit.clubs), Card(Rank.K, Suit.spades),
            Card(Rank.Four,Suit.hearts), Card(Rank.Eight, Suit.spades),
            Card(Rank.Seven, Suit.spades)],[Card(Rank.A, Suit.diamonds),
                                            Card(Rank.Four, Suit.spades)]),
            PlayerCards([Card(Rank.Four, Suit.clubs),
                         Card(Rank.K, Suit.spades),
                         Card(Rank.Four, Suit.hearts),
                         Card(Rank.Eight, Suit.spades),
                         Card(Rank.Seven, Suit.spades)],
                        [Card(Rank.A, Suit.clubs),
                         Card(Rank.Four, Suit.diamonds)]),
            PlayerCards([Card(Rank.Four, Suit.clubs),
                         Card(Rank.K, Suit.spades),
                         Card(Rank.Four, Suit.hearts),
                         Card(Rank.Eight, Suit.spades),
                         Card(Rank.Seven, Suit.spades)],
                        [Card(Rank.A, Suit.spades),
                         Card(Rank.Nine, Suit.spades)]),
            PlayerCards([Card(Rank.Four, Suit.clubs),
                         Card(Rank.K, Suit.spades),
                         Card(Rank.Four, Suit.hearts),
                         Card(Rank.Eight, Suit.spades),
                         Card(Rank.Seven, Suit.spades)],
                        [Card(Rank.K, Suit.hearts),
                         Card(Rank.K, Suit.diamonds)]),
            PlayerCards([Card(Rank.Four, Suit.clubs),
                         Card(Rank.K, Suit.spades),
                         Card(Rank.Four, Suit.hearts),
                         Card(Rank.Eight, Suit.spades),
                         Card(Rank.Seven, Suit.spades)],
                        [Card(Rank.Five, Suit.diamonds),
                         Card(Rank.Six, Suit.diamonds)])])

    def test_to_str(self):
        self.assertEqual(to_str(self.list_player_cards),
                         "4cKs4h8s7s Ad4s Ac4d As9s KhKd 5d6d")


if __name__ == "__main__":
    unittest.main()
