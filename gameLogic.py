from collections import Counter

# Royal flush 10,Straight flush 9,Four of a kind 8,Full house 7,Flush 6,
# Straight 5,Three of a kind 4,Two pair 3, Pair 2, High Card 1
# value_when_true if condition else value_when_false
from const import RANKS_NAMES, HANDS_RANK


def checkHands(player1HandsList, player2HandsList, deckCards):
    result = []
    for hand in range(len(player1HandsList)):
        orderedPlayer1Hand = sorted(player1HandsList[hand], key=lambda card: card.getRank(), reverse=True)
        orderedPlayer2Hand = sorted(player2HandsList[hand], key=lambda card: card.getRank(), reverse=True)
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
    suit_type = hand[0].getSuit()
    for card in range(len(hand)):
        collectionOfRanksInHand.append(hand[card].getRank())
        if isFlush and hand[card].getSuit() != suit_type:
            isFlush = False
        if isStraight and not isCurrentCardFollowsNextCard(card, hand):
            isStraight = False
    countAmountOfEachRankInHand = Counter(collectionOfRanksInHand).most_common(5)
    # Royal flush 10,Straight flush 9,Four of a kind 8,Full house 7,Flush 6,
    # Straight 5,Three of a kind 4,Two pair 3, Pair 2, High Card 1
    if isFlush and isStraight:
        return {10: [countAmountOfEachRankInHand[0][0]]} if hand[0].getRank() == 14 else {
            9: [countAmountOfEachRankInHand[0][0]]}
    if isFourOfAKind(countAmountOfEachRankInHand):
        return {8: [countAmountOfEachRankInHand[0][0], countAmountOfEachRankInHand[1][0]]}
    if isFullHouse(countAmountOfEachRankInHand):
        return {7: [countAmountOfEachRankInHand[0][0], countAmountOfEachRankInHand[1][0]]}
    if isFlush:
        return {6: [countAmountOfEachRankInHand[0][0], countAmountOfEachRankInHand[1][0],
                    countAmountOfEachRankInHand[2][0], countAmountOfEachRankInHand[3][0],
                    countAmountOfEachRankInHand[4][0]]}
    if isStraight:
        if hand[1].getRank() == 5:
            return {5: [hand[1].getRank()]}
        else:
            return {5: [hand[0].getRank()]}
    if isThreeOfAKind(countAmountOfEachRankInHand):
        return {4: [countAmountOfEachRankInHand[0][0], countAmountOfEachRankInHand[1][0],
                    countAmountOfEachRankInHand[2][0]]}
    if isTwoPair(countAmountOfEachRankInHand):
        return {3: [countAmountOfEachRankInHand[0][0], countAmountOfEachRankInHand[1][0],
                    countAmountOfEachRankInHand[2][0]]}
    if isPair(countAmountOfEachRankInHand):
        return {2: [countAmountOfEachRankInHand[0][0], countAmountOfEachRankInHand[1][0],
                    countAmountOfEachRankInHand[2][0], countAmountOfEachRankInHand[3][0]]}
    return highCard(countAmountOfEachRankInHand)


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
