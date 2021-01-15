from app.PlayerCards import *
from app.Converter import *


def main():
    play_cards = to_player_cards(input2())
    combination_handlers: List[Handler] = [StraightFlushHandler(),
                                           FourOfKindHandler(),
                                           FullHouseHandler(), FlushHandler(),
                                           StraightHandler(),
                                           ThreeKindHandler(),
                                           TwoPairsHandler(), PairHandler(),
                                           HighCardHandler()]
    all_players_combination = []
    for i in range(len(play_cards)):
        all_players_combination.append(
            [combination_handler.handle(play_cards[i]) for combination_handler
             in combination_handlers if
             combination_handler.handle(play_cards[i])][0])

    all_players_combination = force_definition(all_players_combination)
    print(all_players_combination[0].force_high_card)
    for i in range(len(all_players_combination)-1):
        print(to_str(all_players_combination[i].high_cards), end=" ")
        if (all_players_combination[i].force ==
            all_players_combination[i+1].force) \
                and (all_players_combination[i].force_high_card ==
                     all_players_combination[i+1].force_high_card):
            print("=", end=" ")
    print(to_str(all_players_combination[-1].high_cards))


def input2() -> str:
    res = str(input("input cards  "))
    return res


def force_definition(hands_force: List[Combination]) -> List[Combination]:
    hands_force.sort(key=lambda x: (x.force, x.force_high_card[0],
                                    x.force_high_card[1], x.force_high_card[2],
                                    x.force_high_card[3], x.force_high_card[4]))
    return hands_force


main()
