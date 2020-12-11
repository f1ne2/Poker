from Cards import *
from Converter import *
from PlayerCards import *


def main():
    common_cards, custom_cards = to_player_cards(input2())
    result_game = to_str(common_cards, custom_cards)
    z = PlayerCards(x, y)
    force = [0] * int(len(z.custom)/4)
    z2 = z.redefine()
    d = Sort(z.redefine())
    for c in range(len(z2)):
        res = z.is_high_card(z2[c])
        if res:
            force[c] = 1
        res = z.is_pairs(z2[c])
        if res:
            force[c] = 2
        res = z.is_two_pairs(z2[c])
        if res:
            force[c] = 3
        res = z.is_set(z2[c])
        if res:
            force[c] = 4
        res = z.is_straight(z2[c])
        if res:
            force[c] = 5
        res = z.is_flush(z2[c])
        if res:
            force[c] = 6
        res = z.is_full_house(z2[c])
        if res:
            force[c] = 7
        res = z.is_four_of_kind(z2[c])
        if res:
            force[c] = 8
        if force[c] == 5:
            res = z.is_straight_flush(z2[c])
            if res:
                force[c] = 9
    d.quick_sort(force, 0, len(force) - 1)



def input2():
    res = str(input("input cards  "))
    return res


main()

