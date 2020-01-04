import random


class Card:
    RANKS = {2: '2',
             3: "3",
             4: "4",
             5: "5",
             6: "6",
             7: "7",
             8: "8",
             9: "9",
             10: "10",
             11: "J",
             12: "Q",
             13: "K",
             14: "A"}
    SUITS = ('S', 'D', 'H', 'C')

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return Card.RANKS[self.rank] + "" + self.suit

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit



class Deck:
    def __init__(self):
        self.deck = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                card = Card(rank, suit)
                self.deck.append(card)
                #print(Card.__str__(card))

    def shuffle(self):
        random.shuffle(self.deck)

    def __len__(self):
        return len(self.deck)

    def dealCard(self):
        if len(self) == 0:
            return None
        else:
            return self.deck.pop(0)



