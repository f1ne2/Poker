from typing import List, Dict
from app.Cards import Suit, Rank, Card
from app.PlayerCards import PlayerCards


def to_cards(cards_str: str) -> List[Card]:
    return [Card(ranks_dict.get(cards_str[i]), suits_dict.get(cards_str[i+1]))
            for i in range(0, len(cards_str)-1, 2)]


def to_player_cards(input_string: str) -> List[PlayerCards]:
    common_cards = to_cards(input_string.split(" ")[0])
    return [PlayerCards(common_cards, to_cards(string_card)) for string_card in
            input_string.split(" ")[1:]]


def find_card_str_in_dict(cards_to_str: Card) -> str:
    res = ""
    for key, value in ranks_dict.items():
        if cards_to_str.rank == value:
            res = res + key

    for key, value in suits_dict.items():
        if cards_to_str.suit == value:
            res = res + key
    return res


def to_str(cards_to_str: PlayerCards) -> str:
    the_first_card = find_card_str_in_dict(cards_to_str.custom[0])
    the_second_card = find_card_str_in_dict(cards_to_str.custom[1])
    return the_first_card + the_second_card


ranks_dict: Dict[str, Rank] = {"2": Rank.Two, "3": Rank.Three, "4": Rank.Four,
                               "5": Rank.Five, "6": Rank.Six, "7": Rank.Seven,
                               "8": Rank.Eight, "9": Rank.Nine, "T": Rank.Ten,
                               "J": Rank.J, "Q": Rank.Q, "K": Rank.K,
                               "A": Rank.A}
suits_dict: Dict[str, Suit] = {"h": Suit.hearts, "d": Suit.diamonds,
                               "c": Suit.clubs, "s": Suit.spades}
