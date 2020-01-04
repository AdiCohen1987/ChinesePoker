def checkHands(player1Hands, player2Hands, deckCards):
    for x in range(0, 10):
        flowOfChecks(player1Hands[x])


def flowOfChecks(hand):
    orderedByRankHand = sorted(hand, key=lambda x: x.getRank(), reverse=True)
    orderedBySuitHand = sorted(hand, key=lambda x: x.getSuit(), reverse=True)

    isRoyal(orderedByRankHand)


def isRoyal(hand):
    'a'
