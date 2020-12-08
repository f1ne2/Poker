import unittest
import sys
sys.path.insert(0, "D:/Git/Poker/src")
from Converter import *
from Cards import Rank, Suit, Card
from PlayerCards import *



class TestCard(unittest.TestCase):
    def setUp(self):
        self.str1 = "4cKs4h8s7s Ad4s Ac4d As9s Kh10s Qd3d 10c10h"

    # Divide inputting string to common card string and list[str] of players
    # cards
    def test_divide(self):
        self.assertEqual(divide(self.str1),
                         ("4cKs4h8s7s", ['Ad4s', 'Ac4d', 'As9s', 'Kh10s',
                                         'Qd3d', '10c10h']))

    # Transfer Tuple[Rank, Suit] of cards to string
    def test_to_str(self):
        self.set1 = [Rank.Four, Suit.clubs, Rank.K,
                     Suit.spades, Rank.Four, Suit.hearts,
                     Rank.Eight, Suit.spades, Rank.Seven,
                     Suit.spades]
        self.set2 = [[Rank.Four, Suit.clubs, Rank.K, Suit.spades, Rank.Four,
                      Suit.hearts, Rank.Eight, Suit.spades, Rank.Seven,
                      Suit.spades, Rank.Q, Suit.diamonds, Rank.Three,
                      Suit.diamonds], [Rank.Four, Suit.clubs, Rank.K,
                                       Suit.spades, Rank.Four, Suit.hearts,
                                       Rank.Eight,
                                       Suit.spades, Rank.Seven, Suit.spades,
                                       Rank.K, Suit.hearts,
                                       Rank.Ten, Suit.spades],
                     [Rank.Four, Suit.clubs,
                      Rank.K, Suit.spades, Rank.Four, Suit.hearts, Rank.Eight,
                      Suit.spades, Rank.Seven, Suit.spades, Rank.Ten,
                      Suit.clubs, Rank.Ten, Suit.hearts],
                     [Rank.Four, Suit.clubs,
                      Rank.K, Suit.spades, Rank.Four, Suit.hearts, Rank.Eight,
                      Suit.spades, Rank.Seven, Suit.spades, Rank.A,
                      Suit.diamonds, Rank.Four, Suit.spades], [Rank.Four,
                                        Suit.clubs, Rank.K, Suit.spades,
                                        Rank.Four, Suit.hearts,Rank.Eight,
                                        Suit.spades, Rank.Seven, Suit.spades,
                                        Rank.A, Suit.clubs, Rank.Four,
                                        Suit.diamonds],
                     [Rank.Four, Suit.clubs, Rank.K, Suit.spades, Rank.Four,
                      Suit.hearts,Rank.Eight, Suit.spades, Rank.Seven,
                      Suit.spades, Rank.A, Suit.spades, Rank.Nine, Suit.spades]]
        self.assertEqual(to_str(self.set1, self.set2),
                         ("4cKs4h8s7s", "Qd3d Kh10s 10c10h Ad4s Ac4d As9s"))

    # Converting List[str], str to Tuple[Rank, Suit]
    def test_to_player_cards(self):
        self.list1 = ['Ad4s', 'Ac4d', 'As9s', 'Kh10s', 'Qd3d', '10c10h']
        self.str2 = "4cKs4h8s7s"
        self.assertEqual(to_player_cards(self.str2, self.list1),
                         ([Rank.Four, Suit.clubs, Rank.K,
                           Suit.spades, Rank.Four, Suit.hearts,
                           Rank.Eight, Suit.spades, Rank.Seven,
                           Suit.spades],
                          [Rank.A, Suit.diamonds, Rank.Four, Suit.spades,
                           Rank.A, Suit.clubs,
                           Rank.Four, Suit.diamonds, Rank.A, Suit.spades,
                           Rank.Nine, Suit.spades, Rank.K,
                           Suit.hearts, Rank.Ten, Suit.spades, Rank.Q,
                           Suit.diamonds,
                           Rank.Three, Suit.diamonds, Rank.Ten, Suit.clubs,
                           Rank.Ten, Suit.hearts]))


class TestPlayerCards(unittest.TestCase):
    def setUp(self):
        self.set1 = [Rank.Four, Suit.clubs, Rank.K,
                     Suit.spades, Rank.Four, Suit.hearts,
                     Rank.Eight, Suit.spades, Rank.Seven,
                     Suit.spades]
        self.set2 = [Rank.A, Suit.diamonds, Rank.Four, Suit.spades, Rank.A,
                     Suit.clubs, Rank.Four, Suit.diamonds, Rank.A, Suit.spades,
                     Rank.Nine, Suit.spades, Rank.K, Suit.hearts, Rank.Ten,
                     Suit.spades, Rank.Q, Suit.diamonds, Rank.Three,
                     Suit.diamonds, Rank.Ten, Suit.clubs, Rank.Ten, Suit.hearts]
        self.set3 = [Rank.Four, Suit.clubs, Rank.K, Suit.spades, Rank.Four,
                           Suit.hearts, Rank.Eight, Suit.spades, Rank.Seven,
                           Suit.spades, Rank.A, Suit.diamonds, Rank.Four,
                           Suit.spades]
        self.set4 = [Rank.Four, Suit.clubs, Rank.K, Suit.spades, Rank.Four,
                     Suit.hearts, Rank.Eight, Suit.spades, Rank.Seven,
                     Suit.spades, Rank.Ten, Suit.clubs, Rank.Ten, Suit.hearts]

    # Converting Tuple[Rank, Suit] of five common cards and Tuple[Rank, Suit]
    # of two player"s cards to Tuple[Rank, Suit] of seven cards
    def test_redefine(self):
        self.assertEqual(PlayerCards(self.set1, self.set2).redefine(),
                         [[Rank.Four, Suit.clubs, Rank.K, Suit.spades,
                           Rank.Four, Suit.hearts, Rank.Eight, Suit.spades,
                           Rank.Seven, Suit.spades, Rank.A, Suit.diamonds,
                           Rank.Four, Suit.spades], [Rank.Four, Suit.clubs,
                                    Rank.K, Suit.spades, Rank.Four,
                                    Suit.hearts, Rank.Eight, Suit.spades,
                                    Rank.Seven, Suit.spades, Rank.A,
                                    Suit.clubs, Rank.Four, Suit.diamonds],
                          [Rank.Four, Suit.clubs, Rank.K, Suit.spades,
                           Rank.Four, Suit.hearts, Rank.Eight, Suit.spades,
                           Rank.Seven, Suit.spades, Rank.A, Suit.spades,
                           Rank.Nine, Suit.spades], [Rank.Four, Suit.clubs,
                                    Rank.K, Suit.spades, Rank.Four,
                                    Suit.hearts, Rank.Eight, Suit.spades,
                                    Rank.Seven, Suit.spades, Rank.K,
                                    Suit.hearts, Rank.Ten, Suit.spades],
                          [Rank.Four, Suit.clubs, Rank.K, Suit.spades,
                           Rank.Four, Suit.hearts, Rank.Eight, Suit.spades,
                           Rank.Seven, Suit.spades, Rank.Q, Suit.diamonds,
                           Rank.Three, Suit.diamonds], [Rank.Four, Suit.clubs,
                                    Rank.K, Suit.spades, Rank.Four,
                                    Suit.hearts, Rank.Eight, Suit.spades,
                                    Rank.Seven, Suit.spades, Rank.Ten,
                                    Suit.clubs, Rank.Ten, Suit.hearts]])
    # Finding the pairs combination in Tuple[Rank, Suit]

    def test_is_pairs(self):
        self.assertEqual(PlayerCards(self.set1, self.set2).is_pairs(self.set3),
                         False)

    # Finding the two pairs combination in Tuple[Rank, Suit]
    def test_is_two_pairs(self):
        self.assertEqual(
            PlayerCards(self.set1, self.set2).is_two_pairs(self.set4), True)

    # Finding the set combination in Tuple[Rank, Suit]
    def test_is_set(self):
        self.assertEqual(PlayerCards(self.set1, self.set2).is_set(self.set3),
                         True)

    # Finding the four of kind combination in Tuple[Rank, Suit]
    def test_is_four_of_kind(self):
        self.assertEqual(PlayerCards(self.set1, self.set2).is_four_of_kind
                         (self.set3), False)

    # Finding the high card combination in Tuple[Rank, Suit]
    def test_high_card(self):
        self.assertEqual(PlayerCards(self.set1, self.set2).is_high_card
                         (self.set3), False)

    # Finding the full house combination in Tuple[Rank, Suit]
    def test_full_house(self):
        self.assertEqual(PlayerCards(self.set1, self.set2).is_full_house
                         (self.set4), False)

    # Finding the flush combination in Tuple[Rank, Suit]
    def test_is_flush(self):
        self.assertEqual(PlayerCards(self.set1, self.set2).is_flush
                         (self.set3), False)

    # Finding the straight combination in Tuple[Rank, Suit]
    def test_is_straight(self):
        self.assertEqual(PlayerCards(self.set1, self.set2).is_straight
                         (self.set3), False)

    # Finding the straight flush combination in Tuple[Rank, Suit]
    def test_is_straight_flush(self):
        self.assertEqual(PlayerCards(self.set1, self.set2).is_straight_flush
                         (self.set3), False)


class TesSort(unittest.TestCase):
    def setUp(self):
        self.arr = [4, 4, 6, 3, 2, 3]
        self.set1 = [[Rank.Four, Suit.clubs, Rank.K, Suit.spades, Rank.Four,
          Suit.hearts, Rank.Eight, Suit.spades, Rank.Seven,
          Suit.spades, Rank.A, Suit.diamonds, Rank.Four,
          Suit.spades], [Rank.Four, Suit.clubs, Rank.K,
                         Suit.spades, Rank.Four, Suit.hearts,
                         Rank.Eight, Suit.spades, Rank.Seven,
                         Suit.spades, Rank.A, Suit.clubs,
                         Rank.Four, Suit.diamonds], [Rank.Four,
                                                     Suit.clubs, Rank.K,
                                                     Suit.spades, Rank.Four,
                                                     Suit.hearts, Rank.Eight,
                                                     Suit.spades, Rank.Seven,
                                                     Suit.spades, Rank.A,
                                                     Suit.spades, Rank.Nine,
                                                     Suit.spades],
         [Rank.Four, Suit.clubs, Rank.K,
          Suit.spades, Rank.Four, Suit.hearts,
          Rank.Eight, Suit.spades, Rank.Seven,
          Suit.spades, Rank.K, Suit.hearts,
          Rank.Ten, Suit.spades], [Rank.Four,
                                   Suit.clubs, Rank.K, Suit.spades, Rank.Four,
                                   Suit.hearts, Rank.Eight, Suit.spades,
                                   Rank.Seven,
                                   Suit.spades, Rank.Q, Suit.diamonds,
                                   Rank.Three,
                                   Suit.diamonds],
         [Rank.Four, Suit.clubs, Rank.K,
          Suit.spades, Rank.Four, Suit.hearts,
          Rank.Eight, Suit.spades, Rank.Seven,
          Suit.spades, Rank.Ten, Suit.clubs,
          Rank.Ten, Suit.hearts]]

    # Sorting array of force hands.  Sorting Tuple[Rank, Suit]
    def test_partition(self):
        self.assertEqual(Sort(self.set1).partition(self.arr, 0, 5), 2)


if __name__ == "__main__":
    unittest.main()
