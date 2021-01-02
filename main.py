from app.Converter import *


def main():
    play_cards = to_player_cards(input2())

    # for i in range(len(play_cards)):
    #     print(play_cards[i].custom[0].rank, play_cards[i].custom[0].suit)
    #     print(play_cards[i].custom[1].rank, play_cards[i].custom[1].suit)
    #     for j in range(len(play_cards[i].common_cards)):
    #         print(play_cards[i].common_cards[j].rank,
    #               play_cards[i].common_cards[j].suit)
    # for i in range(len(play_cards)):
    #     force = PlayerCards(play_cards[i].common_cards, play_cards[i].custom)
    #     print(play_cards[i].common_cards, play_cards[i].custom)


def input2():
    res = str(input("input cards  "))
    return res


main()

