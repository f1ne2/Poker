from Cards import *
from Converter import *
from PlayerCards import *


def main():
    i, j = divide(input2())
    x, y = to_player_cards(i, j)
    i, j = to_str(x, y)
    z = PlayerCards(x, y)
    f = z.pairs()
    print(f)


def input2():
    res = str(input("input cards  "))
    return res

main()

