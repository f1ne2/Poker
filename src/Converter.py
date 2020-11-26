class Converter:
    def __init__(self, cards: str) -> str:
        self.cards = cards

    def players_cards(self) -> list:
        str2 = self.cards.split(" ", 1)
        players = str2[1].split()
        pl = ""
        for i in range(len(players)):
            pl = pl + str2[0] + players[i] + " "
        res = pl.split()
        return res

    def hands(self, play: list) -> str:
        str3 = ""
        for item in play:
            str3 = str3 + item[10:] + " "
        return str3.strip(" ")



