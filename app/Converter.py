from typing import List, Dict

from app.Cards import Suit, Rank, Card
from app.PlayerCards import PlayerCards


def to_cards(cards_str: str) -> List[Card]:
    j = 0
    output = []
    for i in range(len(cards_str) - 1):
        if i == j:
            if cards_str[i] != "1":
                output.append(Card(ranks_dict.get(cards_str[i]),
                                   suits_dict.get(cards_str[i + 1])))
                j += 2
            else:
                output.append(Card(ranks_dict.get(cards_str[i] +
                                                  cards_str[i + 1]),
                                   suits_dict.get(cards_str[i + 2])))
                j += 3
    for k in range(len(output)):
        print(output[k].rank, output[k].suit)
    return output


def to_player_cards(input_string: str) -> List[PlayerCards]:
    string_cards = input_string.split(" ")
    common_cards = to_cards(string_cards[0])
    return [PlayerCards(common_cards, to_cards(string_card)) for string_card in
            string_cards[1:]]


def to_str(cards_to_str: List[PlayerCards]) -> str:
    res = ""
    for i in range(len(cards_to_str[0].common_cards)):
        for key, value in ranks_dict.items():
            if cards_to_str[i].common_cards[i].rank == value:
                res = res + key
        for key, value in suits_dict.items():
            if cards_to_str[i].common_cards[i].suit == value:
                res = res + key
    res = res + " "
    for i in range(len(cards_to_str)):
        for j in range(len(cards_to_str[0].custom)):
            for key, value in ranks_dict.items():
                if cards_to_str[i].custom[j].rank == value:
                    res = res + key
            for key, value in suits_dict.items():
                if cards_to_str[i].custom[j].suit == value:
                    res = res + key
        res = res + " "
    res = res.rstrip(" ")
    return res


ranks_dict: Dict[str, Rank] = {"2": Rank.Two, "3": Rank.Three, "4": Rank.Four,
                               "5": Rank.Five, "6": Rank.Six, "7": Rank.Seven,
                               "8": Rank.Eight, "9": Rank.Nine, "10": Rank.Ten,
                               "J": Rank.J, "Q": Rank.Q, "K": Rank.K,
                               "A": Rank.A}
suits_dict: Dict[str, Suit] = {"h": Suit.hearts, "d": Suit.diamonds,
                               "c": Suit.clubs, "s": Suit.spades}


