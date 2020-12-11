from typing import List
from Cards import Suit, Rank, Card


def to_player_cards(input_cards: str) -> List[Card] and List[Card]:
    j = 0
    common = []
    custom = []
    for i in range(len(input_cards)-1):
        if i == j:
            if input_cards[i] != " ":
                if input_cards[i] != "1":
                    card1 = Card(set_rank.get(input_cards[i]),
                                 set_suit.get(input_cards[i+1]))
                    if len(common) < 5:
                        common.append(card1)
                        j += 2
                    else:
                        custom.append(card1)
                        j += 2
                else:
                    card1 = Card(set_rank.get(input_cards[i]+input_cards[i+1]),
                                 set_suit.get(input_cards[i+2]))
                    if len(common) < 5:
                        common.append(card1)
                        j += 3
                    else:
                        custom.append(card1)
                        j += 3
            else:
                j += 1

    return common, custom


def to_str(common_to_str: List[Card], custom_to_str: List[Card]) -> str:
    common_res = ""
    hands_res = ""
    res = ""

    for i in range(5):
        for key, value in set_rank.items():
            if common_to_str[i].rank == value:
                common_res = common_res + key
        for key, value in set_suit.items():
            if common_to_str[i].suit == value:
                common_res = common_res + key
    for i in range(len(custom_to_str)):
        for key, value in set_rank.items():
            if custom_to_str[i].rank == value:
                res = res + key + " "
        for key, value in set_suit.items():
            if custom_to_str[i].suit == value:
                res = res + key + " "
    k = 0
    j = 0
    print(res)
    for i in range(len(res)-1):
        if i == j:
            if res[i] != " ":
                hands_res = hands_res + res[i]
                j += 1
            else:
                k += 1
                j += 1
                if k % 4 == 0:
                    hands_res = hands_res + " "
    res = common_res + " " + hands_res
    return res


set_rank = {"2": Rank.Two, "3": Rank.Three, "4": Rank.Four, "5": Rank.Five,
            "6": Rank.Six, "7": Rank.Seven, "8": Rank.Eight, "9": Rank.Nine,
            "10": Rank.Ten, "J": Rank.J, "Q": Rank.Q, "K": Rank.K, "A": Rank.A}
set_suit = {"h": Suit.hearts, "d": Suit.diamonds, "c": Suit.clubs,
            "s": Suit.spades}




