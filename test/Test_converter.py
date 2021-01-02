import unittest
from app.Converter import *
from app.Cards import Card


class TestCard(unittest.TestCase):
    def setUp(self):
        self.str1 = "Ad4s"
        self.str2 = "4cKs4h8s7s Ad4s Ac4d As9s KhKd 5d6d"
        self.list_player_cards = [PlayerCards([
            Card(Rank.Four, Suit.clubs), Card(Rank.K, Suit.spades),
            Card(Rank.Four, Suit.hearts), Card(Rank.Eight, Suit.spades),
            Card(Rank.Seven, Suit.spades)], [Card(Rank.A, Suit.diamonds),
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
                         Card(Rank.Six, Suit.diamonds)])]

    # Transfer string to List[Card(Rank, Suit)]
    def test_to_card(self):
        self.Card1 = Card(Rank.A, Suit.diamonds)
        self.Card2 = Card(Rank.Four, Suit.spades)
        self.list1 = to_cards(self.str1)
        self.assertEqual(self.list1[0].rank, self.Card1.rank)
        self.assertEqual(self.list1[0].suit, self.Card1.suit)
        self.assertEqual(self.list1[1].rank, self.Card2.rank)
        self.assertEqual(self.list1[1].suit, self.Card2.suit)

    # Transfer input string to List[PlayerCards]
    def test_to_player_cards(self):
        self.common_card1 = Card(Rank.Four, Suit.clubs)
        self.common_card2 = Card(Rank.K, Suit.spades)
        self.common_card3 = Card(Rank.Four, Suit.hearts)
        self.common_card4 = Card(Rank.Eight, Suit.spades)
        self.common_card5 = Card(Rank.Seven, Suit.spades)
        self.list_common = [self.common_card1, self.common_card2,
                            self.common_card3, self.common_card4,
                            self.common_card5]
        self.player1_card1 = Card(Rank.A, Suit.diamonds)
        self.player1_card2 = Card(Rank.Four, Suit.spades)
        self.player2_card1 = Card(Rank.A, Suit.clubs)
        self.player2_card2 = Card(Rank.Four, Suit.diamonds)
        self.player3_card1 = Card(Rank.A, Suit.spades)
        self.player3_card2 = Card(Rank.Nine, Suit.spades)
        self.player4_card1 = Card(Rank.K, Suit.hearts)
        self.player4_card2 = Card(Rank.K, Suit.diamonds)
        self.player5_card1 = Card(Rank.Five, Suit.diamonds)
        self.player5_card2 = Card(Rank.Six, Suit.diamonds)
        self.cards_of_players = [[self.player1_card1, self.player1_card2],
                                 [self.player2_card1, self.player2_card2],
                                 [self.player3_card1, self.player3_card2],
                                 [self.player4_card1, self.player4_card2],
                                 [self.player5_card1, self.player5_card2]]
        self.list1 = to_player_cards(self.str2)

        for i in range(len(self.list1[0].common_cards)):
            self.assertEqual(self.list1[0].common_cards[i].rank,
                             self.list_common[i].rank)
            self.assertEqual(self.list1[0].common_cards[i].suit,
                             self.list_common[i].suit)
            self.assertEqual(self.list1[i].custom[0].rank,
                             self.cards_of_players[i][0].rank)
            self.assertEqual(self.list1[i].custom[0].suit,
                             self.cards_of_players[i][0].suit)
            self.assertEqual(self.list1[i].custom[1].rank,
                             self.cards_of_players[i][1].rank)
            self.assertEqual(self.list1[i].custom[1].suit,
                             self.cards_of_players[i][1].suit)

#     finding Card in dictionary and return its key
    def test_find_card_str_in_dict(self):
        self.Card1 = Card(Rank.A, Suit.diamonds)
        self.assertEqual(find_card_str_in_dict(self.Card1), "Ad")

    def test_to_str(self):
        self.assertEqual(to_str(self.list_player_cards),
                         "4cKs4h8s7s Ad4s Ac4d As9s KhKd 5d6d")


if __name__ == "__main__":
    unittest.main()
