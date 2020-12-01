import Cards
from Cards import Suit, Rank, Card
from typing import List, Tuple


def divide(str_cards: str) -> Tuple[List[str], str]:
    str2 = str_cards.split(" ", 1)
    players = str2[1].split()
    return players, str2[0]


def to_player_cards(common_cards: str, custom: List[str]) -> Tuple[Rank, Suit]:
    common2 = []
    hands_res = []
    for i in range(len(common_cards)):
        if common_cards[i] != "0":
            if set1.get(common_cards[i]) is not None:
                common2.append(set1.get(common_cards[i]))
            if set2.get(common_cards[i]) is not None:
                common2.append(set2.get(common_cards[i]))
    for x in range(len(custom)):
        for y in range(len(custom[x])):
            if custom[x][y] != "0":
                if set1.get(custom[x][y]) is not None:
                    hands_res.append(set1.get(custom[x][y]))
                if set2.get(custom[x][y]) is not None:
                    hands_res.append(set2.get(custom[x][y]))
    return common2, hands_res


def to_str(common_to_str: Tuple[Rank, Suit],
           hands_to_str: Tuple[Rank, Suit]) -> Tuple[str, List[str]]:
    common2 = ""
    hands_res = ""
    for i in range(len(common_to_str)):
        if set3.get(common_to_str[i]) is not None:
            common2 = common2 + set3.get(common_to_str[i])
        if set4.get(common_to_str[i]) is not None:
            common2 = common2 + set4.get(common_to_str[i])
    for j in range(len(hands_to_str)):
        if set3.get(hands_to_str[j]) is not None:
            hands_res = hands_res + set3.get(hands_to_str[j])
        if set4.get(hands_to_str[j]) is not None:
            hands_res = hands_res + set4.get(hands_to_str[j]) + " "
    hands_out = ""
    hands_list = hands_res.strip(" ")
    hands_list = hands_list.split(" ")
    for t in range(len(hands_list)-1):
        if t % 2 == 0:
            hands_out = hands_out + hands_list[t] + hands_list[t + 1] + " "
            hands_res = hands_out.strip(" ")
    return common2, hands_res


set1 = {"2": Cards.Rank.Two, "3": Cards.Rank.Three,
        "4": Cards.Rank.Four, "5": Cards.Rank.Five,
        "6": Cards.Rank.Six, "7": Cards.Rank.Seven,
        "8": Cards.Rank.Eight, "9": Cards.Rank.Nine,
        "1": Cards.Rank.Ten, "J": Cards.Rank.J, "Q": Cards.Rank.Q,
        "K": Cards.Rank.K, "A": Cards.Rank.A}
set2 = {"h": Cards.Suit.hearts, "d": Cards.Suit.diamonds,
        "c": Cards.Suit.clubs, "s": Cards.Suit.spades}
set3 = {Cards.Rank.Two: "2", Cards.Rank.Three: "3",
        Cards.Rank.Four: "4", Cards.Rank.Five: "5",
        Cards.Rank.Six: "6", Cards.Rank.Seven: "7",
        Cards.Rank.Eight: "8", Cards.Rank.Nine: "9",
        Cards.Rank.Ten: "10", Cards.Rank.J: "J", Cards.Rank.Q: "Q",
        Cards.Rank.K: "K", Cards.Rank.A: "A"}
set4 = {Cards.Suit.hearts: "h", Cards.Suit.diamonds: "d",
        Cards.Suit.clubs: "c", Cards.Suit.spades: "s"}
