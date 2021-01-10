from app.Converter import *


def main():
    sum_force = []
    str_list = []

    play_cards = to_player_cards(input2())

    for i in range(len(play_cards)):
        play_cards[i].__init__(play_cards[i].common_cards,
                               play_cards[i].custom)
        play_cards[i].force_hand()
        sum_force.append(play_cards[i].force)
    hands_force = force_definition(sum_force)

    for j in range(len(hands_force)):
        player = PlayerCards(hands_force[j][2], hands_force[j][3])
        str_list.append(player)
    res_list_str = (to_str(str_list)).split(" ")[1:]

    for k in range(len(hands_force)-1):
        if hands_force[k][1] == hands_force[k+1][1]:
            print(res_list_str[k], "=", end=" ")
        else:
            print(res_list_str[k], end=" ")
    print(res_list_str[-1], end="")


def input2() -> str:
    res = str(input("input cards  "))
    return res


def force_definition(hands_force: List[int]) -> List[int] and \
                                                List[PlayerCards]:
    hands_force.sort(key=lambda x: (x[0], x[1][0], x[1][1], x[1][2], x[1][3],
                                    x[1][4]))
    return hands_force


main()
