import Cards


class Divide:
    def __init__(self, cards: str):
        self.cards = cards

    def players_cards(self) -> list:
        str2 = self.cards.split(" ", 1)
        players = str2[1].split()
        return players, str2[0]

    def hands(self, play: list) -> str:
        str3 = ""
        for item in play:
            str3 = str3 + item[10:] + " "
        return str3.strip(" ")


class Converter:
    def __init__(self, common_cards: str, custom: list) -> str:
        self.common_cards = common_cards
        self.custom = custom

    def to_player_cards(self):
        set1 = {"2": Cards.Rank.Two, "3": Cards.Rank.Three,
                "4": Cards.Rank.Four, "5": Cards.Rank.Five,
                "6": Cards.Rank.Six, "7": Cards.Rank.Seven,
                "8": Cards.Rank.Eight, "9": Cards.Rank.Nine,
                "1": Cards.Rank.Ten, "J": Cards.Rank.J, "Q": Cards.Rank.Q,
                "K": Cards.Rank.K, "A": Cards.Rank.A}
        set2 = {"h": Cards.Suit.hearts, "d": Cards.Suit.diamonds,
                "c": Cards.Suit.clubs, "s": Cards.Suit.spades}
        common2 = []
        hands_res = []
        for i in range(len(self.common_cards)):
            if self.common_cards[i] != "0":
                if set1.get(self.common_cards[i]) != None:
                    common2.append(set1.get(self.common_cards[i]))
                if set2.get(self.common_cards[i]) != None:
                    common2.append(set2.get(self.common_cards[i]))
        for x in range(len(self.custom)):
            for y in range(len(self.custom[x])):
                if self.custom[x][y] != "0":
                    if set1.get(self.custom[x][y]) != None:
                        hands_res.append(set1.get(self.custom[x][y]))
                    if set2.get(self.custom[x][y]) != None:
                        hands_res.append(set2.get(self.custom[x][y]))
        return common2, hands_res

    def to_str(self, common_to_str: list, hands_to_str: list) -> str:
        set1 = {Cards.Rank.Two: "2", Cards.Rank.Three: "3",
                Cards.Rank.Four: "4", Cards.Rank.Five: "5",
                Cards.Rank.Six: "6", Cards.Rank.Seven: "7",
                Cards.Rank.Eight: "8", Cards.Rank.Nine: "9",
                Cards.Rank.Ten: "10", Cards.Rank.J: "J", Cards.Rank.Q: "Q",
                Cards.Rank.K: "K", Cards.Rank.A: "A"}
        set2 = {Cards.Suit.hearts: "h", Cards.Suit.diamonds: "d",
                Cards.Suit.clubs: "c", Cards.Suit.spades: "s"}
        common2 = ""
        hands_res = ""
        for i in range(len(common_to_str)):
            if set1.get(common_to_str[i]) != None:
                common2 = common2 + set1.get(common_to_str[i])
            if set2.get(common_to_str[i]) != None:
                common2 = common2 + set2.get(common_to_str[i])
        for j in range(len(hands_to_str)):
            if set1.get(hands_to_str[j]) != None:
                hands_res = hands_res + set1.get(hands_to_str[j])
            if set2.get(hands_to_str[j]) != None:
                hands_res = hands_res + set2.get(hands_to_str[j]) + " "
        hands_out = ""
        hands_list = hands_res.strip(" ")
        hands_list = hands_list.split(" ")
        for t in range(len(hands_list)):
            if t % 2 == 0:
                hands_out = hands_out + hands_list[t] + hands_list[t + 1] + " "
                hands_res = hands_out.rstrip(" ")
        return common2, hands_res


str1 = "4cKs4h8s7s Ad4s Ac4d As9s Kh10s Qd3d 10c10h"
qwerty = Divide(str1)
list_player, str_com = qwerty.players_cards()
print(list_player)
print(str_com)
convert = Converter(str_com, list_player)
output_common, output_hands = convert.to_player_cards()
print(output_common, "\n", output_hands)
convert2 = Converter(str_com, list_player)
res_common, res_hands = convert2.to_str(output_common, output_hands)
print(res_common, "\n", res_hands)
