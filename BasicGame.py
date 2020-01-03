import collections

import Cards


def deal(deck):
    hand1 = Hand()
    hand2 = Hand()
    for x in range(2, 6):
        hand1.add_card(deck.dealCard())
        hand2.add_card(deck.dealCard())


class Play:
    def __init__(self, deck):
        self.deck = Cards.Deck()
        deck.shuffle()
        deal(deck)


class Hand:
    def __init__(self):
        self.hand = collections.deque(maxlen=5)

    def add_card(self, card):
        self.hand.append(card)


if __name__ == '__main__':
    d = Cards.Deck()
    p = Play(d)
