from typing import List

from Cards import Suit, Rank, Card


def to_player_cards(input_cards: str) -> List[Card]:
    cards2 = []
    i = 0

    while i < len(input_cards) - 1:
        if input_cards[i] != " ":
            if input_cards[i] != "1":
                card1 = Card(set1.get(input_cards[i]),
                             set1.get(input_cards[i+1]))
                cards2.append(card1)
                i += 2
            else:
                card1 = Card(set1.get(input_cards[i]+input_cards[i+1]),
                             set1.get(input_cards[i+2]))
                cards2.append(card1)
                i += 3
        else:
            i += 1
    # Converting to 7 PlayerCards
    seven_cards = [[0] * 7 for k in range(len(cards2)-11)]
    t = 5
    for j in range(len(seven_cards)):
        seven_cards[j][0:5] = cards2[0:5]
        seven_cards[j][5:7] = cards2[t:t+2]
        t += 2

    return seven_cards


def to_str(cards_to_str: List[Card]) -> str:
    common_res = ""
    hands_res = ""
    res = ""

    for i in range(5):
        for key, value in set1.items():
            if cards_to_str[0][i].rank == value or \
                    cards_to_str[0][i].suit == value:
                common_res = common_res + key

    for i in range(len(cards_to_str)):
        for j in range(-2, 0):
            for key, value in set1.items():
                if cards_to_str[i][j].rank == value or \
                        cards_to_str[i][j].suit == value:
                    res = res + key + " "
    i = 0
    j = 0
    while i < len(res)-1:
        if res[i] != " ":
            hands_res = hands_res + res[i]
            i += 1
        else:
            j += 1
            i += 1
            if j % 4 == 0:
                hands_res = hands_res + " "
    res = common_res + " " + hands_res
    return res


set1 = {"2": Rank.Two, "3": Rank.Three, "4": Rank.Four, "5": Rank.Five,
        "6": Rank.Six, "7": Rank.Seven, "8": Rank.Eight, "9": Rank.Nine,
        "10": Rank.Ten, "J": Rank.J, "Q": Rank.Q, "K": Rank.K, "A": Rank.A,
        "h": Suit.hearts, "d": Suit.diamonds, "c": Suit.clubs, "s": Suit.spades
        }





