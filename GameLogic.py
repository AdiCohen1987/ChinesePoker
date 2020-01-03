def evaluate(self, myCards, otherPlayerCards, deckCards):
    for hand in myCards:
        sortedHand = sorted(hand, reverse=True)
        isRoyalFlush(sortedHand)


def isRoyalFlush():
    pass
