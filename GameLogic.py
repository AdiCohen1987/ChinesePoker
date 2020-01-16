from collections import Counter

HANDS_RANK = {1: 'High Card', 2: 'Pair', 3: 'Two Pairs', 4: 'Three Of A Kind', 5: 'Straight', 6: 'Flush',
              7: 'Full House', 8: 'Four Of A Kind', 9: 'Straight Flush', 10: 'Royal Flush'}
RANKS_NAMES = {14: 'A', 13: 'K', 12: 'Q', 11: 'J'}


# Royal flush 10,Straight flush 9,Four of a kind 8,Full house 7,Flush 6,
# Straight 5,Three of a kind 4,Two pair 3, Pair 2, High Card 1
# value_when_true if condition else value_when_false
def checkHands(player1Hands, player2Hands, deckCards):
    endOfGameFlag = True if len(deckCards) < 3 else False
    result = []
    for hand in range(len(player1Hands)):
        orderedPlayer1Hand = sorted(player1Hands[hand], key=lambda card: card.getRank(), reverse=True)
        orderedPlayer2Hand = sorted(player2Hands[hand], key=lambda card: card.getRank(), reverse=True)
        player1Rank = evaluateHand(orderedPlayer1Hand)
        player2Rank = evaluateHand(orderedPlayer2Hand)
        result.append(checkWhichHandIsBetter(player1Rank, player2Rank))
    return result


def whichPlayerWonCurrentHandString(key, player, card):
    if card in RANKS_NAMES:
        card = RANKS_NAMES.get(card)

    return 'Player: ' + player + ' won with: ' + HANDS_RANK.get(key) + ' HighestCard: ' + str(card)


def checkWhichHandIsBetter(player1Rank, player2Rank):
    if list(player1Rank.keys())[0] > list(player2Rank.keys())[0]:
        return whichPlayerWonCurrentHandString(list(player1Rank.keys())[0], '1', list(player1Rank.values())[0][0])
    elif list(player1Rank.keys())[0] < list(player2Rank.keys())[0]:
        return whichPlayerWonCurrentHandString(list(player2Rank.keys())[0], '2', list(player2Rank.values())[0][0])
    else:
        return compareHandsOfSameRank(player1Rank, player2Rank)


def compareHandsOfSameRank(player1Rank, player2Rank):
    for card in range(len(list(player1Rank.values())[0])):
        if list(player1Rank.values())[0][card] > list(player2Rank.values())[0][card]:
            return whichPlayerWonCurrentHandString(list(player1Rank.keys())[0], '1', list(player1Rank.values())[0][0])
        elif list(player1Rank.values())[0][card] < list(player2Rank.values())[0][card]:
            return whichPlayerWonCurrentHandString(list(player2Rank.keys())[0], '2', list(player2Rank.values())[0][0])
    return 'tie'


def evaluateHand(hand):
    isFlush = True
    isStraight = True
    collectionOfRanksInHand = []
    suitType = hand[0].getSuit()
    for card in range(len(hand)):
        collectionOfRanksInHand.append(hand[card].getRank())
        if isFlush and hand[card].getSuit() != suitType:
            isFlush = False
        if isStraight and not isCurrentCardFollowsNextCard(card, hand):
            isStraight = False
    countTheAmountOfEachRankInHand = Counter(collectionOfRanksInHand).most_common(5)
    # Royal flush 10,Straight flush 9,Four of a kind 8,Full house 7,Flush 6,
    # Straight 5,Three of a kind 4,Two pair 3, Pair 2, High Card 1
    if isFlush and isStraight:
        return {10: [countTheAmountOfEachRankInHand[0][0]]} if hand[0].getRank() == 14 else {
            9: [countTheAmountOfEachRankInHand[0][0]]}
    if isFourOfAKind(countTheAmountOfEachRankInHand):
        return {8: [countTheAmountOfEachRankInHand[0][0], countTheAmountOfEachRankInHand[1][0]]}
    if isFullHouse(countTheAmountOfEachRankInHand):
        return {7: [countTheAmountOfEachRankInHand[0][0], countTheAmountOfEachRankInHand[1][0]]}
    if isFlush:
        return {6: [countTheAmountOfEachRankInHand[0][0], countTheAmountOfEachRankInHand[1][0],
                    countTheAmountOfEachRankInHand[2][0], countTheAmountOfEachRankInHand[3][0],
                    countTheAmountOfEachRankInHand[4][0]]}
    if isStraight:
        if hand[1].getRank() == 5:
            return {5: [hand[1].getRank()]}
        else:
            return {5: [hand[0].getRank()]}
    if isThreeOfAKind(countTheAmountOfEachRankInHand):
        return {4: [countTheAmountOfEachRankInHand[0][0], countTheAmountOfEachRankInHand[1][0],
                    countTheAmountOfEachRankInHand[2][0]]}
    if isTwoPair(countTheAmountOfEachRankInHand):
        return {3: [countTheAmountOfEachRankInHand[0][0], countTheAmountOfEachRankInHand[1][0],
                    countTheAmountOfEachRankInHand[2][0]]}
    if isPair(countTheAmountOfEachRankInHand):
        return {2: [countTheAmountOfEachRankInHand[0][0], countTheAmountOfEachRankInHand[1][0],
                    countTheAmountOfEachRankInHand[2][0], countTheAmountOfEachRankInHand[3][0]]}
    return highCard(countTheAmountOfEachRankInHand)


def isCurrentCardFollowsNextCard(card, hand):
    return ((card == 4) or (card != 4 and hand[card].getRank() == hand[card + 1].getRank() + 1) or
            (card == 0 and hand[card].getRank() == 14 and hand[card + 1].getRank() == 5))


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
