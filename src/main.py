from Cards import *
from Converter import *
from PlayerCards import *


def main():
    i, j = divide(input2())
    x, y = to_player_cards(i, j)
    i, j = to_str(x, y)
    z = PlayerCards(x, y)
    z2 = z.redefine()
    for c in range(len(z2)):
        res = z.is_high_card(z2[c])
        res = z.is_pairs(z2[c])
        res = z.is_two_pairs(z2[c])
        res = z.is_set(z2[c])
        res = z.is_four_of_kind(z2[c])
        res = z.is_full_house(z2[c])
        res = z.is_straight(z2[c])
        res = z.is_flush(z2[c])
        res2 = z.is_straight_flush(z2[c], res)
        res = z.is_straight(z2[c])
        print(res)





def input2():
    res = str(input("input cards  "))
    return res

main()

