from typing import List, Dict
from app.Cards import Suit, Rank, Card
from app.PlayerCards import PlayerCards


def to_cards(cards_str: str) -> List[Card]:
    j = 0
    output = []
    for i in range(len(cards_str)-1):
        if i == j:
            if cards_str[i] != "1":
                output.append(Card(ranks_dict.get(cards_str[i]),
                                   suits_dict.get(cards_str[i+1])))
                j += 2
            else:
                output.append(Card(ranks_dict.get(cards_str[i] +
                                                  cards_str[i+1]),
                                   suits_dict.get(cards_str[i+2])))
                j += 3
    return output


def to_player_cards(input_string: str) -> List[PlayerCards]:
    string_cards = input_string.split(" ")
    common_cards = to_cards(string_cards[0])
    return [PlayerCards(common_cards, to_cards(string_card)) for string_card in
            string_cards[1:]]


def find_card_str_in_dict(cards_to_str: Card) -> str:
    res = ""
    for key, value in ranks_dict.items():
        if cards_to_str.rank == value:
            res = res + key

    for key, value in suits_dict.items():
        if cards_to_str.suit == value:
            res = res + key
    return res


def to_str(cards_to_str: List[PlayerCards]) -> str:
    output_str = ""

    for i in range(len(cards_to_str[0].common_cards)):
        res = find_card_str_in_dict(cards_to_str[0].common_cards[i])
        output_str = output_str + res

    output_str = output_str + " "
    for i in range(len(cards_to_str)):
        the_first_card = find_card_str_in_dict(cards_to_str[i].custom[0])
        the_second_card = find_card_str_in_dict(cards_to_str[i].custom[1])
        output_str = output_str + the_first_card + the_second_card + " "

    output_str = output_str.rstrip(" ")
    return output_str


ranks_dict: Dict[str, Rank] = {"2": Rank.Two, "3": Rank.Three, "4": Rank.Four,
                               "5": Rank.Five, "6": Rank.Six, "7": Rank.Seven,
                               "8": Rank.Eight, "9": Rank.Nine, "T": Rank.Ten,
                               "J": Rank.J, "Q": Rank.Q, "K": Rank.K,
                               "A": Rank.A}
suits_dict: Dict[str, Suit] = {"h": Suit.hearts, "d": Suit.diamonds,
                               "c": Suit.clubs, "s": Suit.spades}
