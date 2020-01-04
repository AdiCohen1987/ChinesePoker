from collections import Counter


def checkHands(player1Hands, player2Hands, deckCards):
    endOfGameFlag = True if len(deckCards) < 3 else False
    for x in range(0, 10):
        flowOfChecks(player1Hands[x])


def flowOfChecks(hand):
    orderedByRankHand = sorted(hand, key=lambda x: x.getRank(), reverse=True)
    #orderedBySuitHand = sorted(hand, key=lambda x: x.getSuit(), reverse=True)
    isFullHand = True if len(hand.getHand()) == 5 else False
    evaluate(orderedByRankHand, isFullHand)


def evaluate(hand, isFullHand):
    if isFullHand:
        isStraight = True
        isFlush = True
        ranks = [hand[4].getRank()]
        for card in range(0, 4):
            if hand[card].getSuit() != hand[card + 1].getSuit():
                isFlush = False
            if hand[card].getRank() != hand[card + 1].getRank() - 1:
                isStraight = False
            ranks.append(hand[card].getRank())
        count = Counter(ranks).most_common(2)
        print('a')
    else:
        print('need to add')
        # need to add a prediction model
