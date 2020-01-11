from collections import Counter


def checkHands(player1Hands, player2Hands, deckCards):
    endOfGameFlag = True if len(deckCards) < 3 else False
    result = []
    orderedPlayer1Hands = []
    orderedPlayer2Hands = []
    for x in range(0, 10):
        orderedPlayer1Hands.append(sorted(player1Hands[x], key=lambda card: card.getRank(), reverse=True))
        orderedPlayer2Hands.append(sorted(player2Hands[x], key=lambda card: card.getRank(), reverse=True))
        player1Rank = evaluate(orderedPlayer1Hands[x])
        player2Rank = evaluate(orderedPlayer2Hands[x])
        if list(player1Rank.keys())[0] > list(player2Rank.keys())[0]:
            result.append('player 1 wins with xxx')
        elif list(player1Rank.keys())[0] < list(player2Rank.keys())[0]:
            result.append('player 2 wins with xxx')
        else:
            result.append(compareHandsOfSameRank(player1Rank, player2Rank))


def compareHandsOfSameRank(player1Rank, player2Rank):
    for x in list(player1Rank.values())[0]:
        if list(player1Rank.values())[0][x] > list(player2Rank.values())[0]:
            return 'player 1 wins with xxx'
        elif list(player1Rank.values())[0][x] < list(player2Rank.values())[0]:
            return 'player 2 wins with xxx'
    return 'tie'


def evaluate(hand):
    isFlush = True
    isStraight = True
    ranks = []
    suitType = hand[0].getSuit()
    for card in range(0, 5):
        ranks.append(hand[card].getRank())
        if isFlush:
            if hand[card].getSuit() != suitType:
                isFlush = False
        if isStraight:
            if checkIfNotStraight(card,hand):
                isStraight = False
    count = Counter(ranks).most_common(5)
    # Royal flush 10,Straight flush 9,Four of a kind 8,Full house 7,Flush 6,
    # Straight 5,Three of a kind 4,Two pair 3, Pair 2, High Card 1
    if isFlush and isStraight:
        return {10: []} if hand[0].getRank() == 14 else {9: [hand[0].getRank()]}
    if isFourOfAKind(count):
        return {8: [count[0]]}
    if isFullHouse(count):
        return {7: [count[0][0], count[1][0]]}
    if isFlush:
        return {6: []}
    if isStraight:
        return {5: [hand[0].getRank()]}
    if isThreeOfAKind(count): return {4: [count[0][0], count[1][0], count[2][0], count[3][0]]}
    if isTwoPair(count):
        return {3: [count[0][0], count[1][0], count[2][0]]}
    if isPair(count):
        return {2: [count[0][0], count[1][0], count[2][0], count[3][0]]}
    return highCard(count)


def checkIfNotStraight(card, hand):
    return not ((card != 4 and hand[card].getRank() != hand[card + 1].getRank()) or
                (card == 0 and hand[card].getRank() == 14 and hand[card + 1].getRank() != 5))


def isFourOfAKind(count):
    return count[0][1] == 4


def isFullHouse(count):
    return count[0][1] == 3 and count[1][1] == 2


def isThreeOfAKind(count):
    return count[0][1] == 3


def isTwoPair(count):
    return count[0][1] == 2 and count[1][1] == 2


def isPair(count):
    return count[0][1] == 2


def highCard(count):
    return {1: [count[0][0], count[1][0], count[2][0], count[3][0], count[4][0]]}
