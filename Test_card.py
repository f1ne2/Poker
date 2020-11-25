import unittest
from Card import Converter


class TestCard(unittest.TestCase):
    def setUp(self):
        str1 = "4cKs4h8s7s Ad4s Ac4d As9s Kh10s Qd3d 10c10h"
        self.str1 = Converter(str1)

    def test_players_card(self):
        self.assertEqual(self.str1.players_cards(), ['4cKs4h8s7sAd4s', '4cKs4h8s7sAc4d', '4cKs4h8s7sAs9s', '4cKs4h8s7sKh10s', '4cKs4h8s7sQd3d', '4cKs4h8s7s10c10h'])

    def test_hands(self):
        self.list1 = ['4cKs4h8s7sAd4s', '4cKs4h8s7sAc4d', '4cKs4h8s7sAs9s', '4cKs4h8s7sKh10s', '4cKs4h8s7sQd3d', '4cKs4h8s7s10c10h']
        self.result = Converter(self.str1)
        self.assertEqual(self.result.hands(self.list1), ['4cKs4h8s7sAd4s', '4cKs4h8s7sAc4d', '4cKs4h8s7sAs9s', '4cKs4h8s7sKh10s', '4cKs4h8s7sQd3d', '4cKs4h8s7s10c10h'])


if __name__ == "__main__":
    unittest.main()
