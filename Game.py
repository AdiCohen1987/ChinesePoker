import Cards

numOfHandsAndCards = 5


def dealInitialCards(deck, player1Hands, player2Hands):
    for x in range(0, numOfHandsAndCards):
        player1Hands[x].add_card(deck.dealCard())
        player2Hands[x].add_card(deck.dealCard())


class Play:
    def __init__(self, deck):
        self.deck = Cards.Deck()
        player1Hands = []
        player2Hands = []
        for x in range(numOfHandsAndCards):
            player1Hands.append(Hand())
            player2Hands.append(Hand())
        deck.shuffle()
        dealInitialCards(deck, player1Hands, player2Hands)
        for item in player1Hands:
            print(item.__getitem__(0),end="  ")
        print()
        for item in player2Hands:
            print(item.__getitem__(0), end="  ")


class Hand:
    def __init__(self):
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def __getitem__(self, x):
        return self.hand[x]


if __name__ == '__main__':
    d = Cards.Deck()
    p = Play(d)
