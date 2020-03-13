from collections import Counter

# Royal flush 10,Straight flush 9,Four of a kind 8,Full house 7,Flush 6,
# Straight 5,Three of a kind 4,Two pair 3, Pair 2, High Card 1
# value_when_true if condition else value_when_false
from const import RANKS_NAMES, HANDS_RANK


def checkHands(player1_hands, player2_hands, deck_cards):
    end_of_game_flag = True if len(deck_cards) < 3 else False
    result = []
    for hand in range(len(player1_hands)):
        orderedPlayer1Hand = sorted(player1_hands[hand], key=lambda card: card.get_rank(), reverse=True)
        orderedPlayer2Hand = sorted(player2_hands[hand], key=lambda card: card.get_rank(), reverse=True)
        player1Rank = evaluateHand(orderedPlayer1Hand)
        player2Rank = evaluateHand(orderedPlayer2Hand)
        result.append(checkWhichHandIsBetter(player1Rank, player2Rank))
    return result


def whichPlayerWonCurrentHandString(key, player, card):
    if card in RANKS_NAMES:
        card = RANKS_NAMES.get(card)

    return 'Player: ' + player + ' won with: ' + HANDS_RANK.get(key) + ' HighestCard: ' + str(card)


def checkWhichHandIsBetter(player1_rank, player2_rank):
    if list(player1_rank.keys())[0] > list(player2_rank.keys())[0]:
        return whichPlayerWonCurrentHandString(list(player1_rank.keys())[0], '1',
                                               list(player1_rank.values())[0][0])
    elif list(player1_rank.keys())[0] < list(player2_rank.keys())[0]:
        return whichPlayerWonCurrentHandString(list(player2_rank.keys())[0], '2',
                                               list(player2_rank.values())[0][0])
    else:
        return compareHandsOfSameRank(player1_rank, player2_rank)


def compareHandsOfSameRank(player1_rank, player2_rank):
    for card in range(len(list(player1_rank.values())[0])):
        if list(player1_rank.values())[0][card] > list(player2_rank.values())[0][card]:
            return whichPlayerWonCurrentHandString(list(player1_rank.keys())[0], '1',
                                                   list(player1_rank.values())[0][0])
        elif list(player1_rank.values())[0][card] < list(player2_rank.values())[0][card]:
            return whichPlayerWonCurrentHandString(list(player2_rank.keys())[0], '2',
                                                   list(player2_rank.values())[0][0])
    return 'tie'


def evaluateHand(hand):
    is_flush = True
    is_straight = True
    collection_of_ranks_in_hand = []
    suit_type = hand[0].get_suit()
    for card in range(len(hand)):
        collection_of_ranks_in_hand.append(hand[card].get_rank())
        if is_flush and hand[card].get_suit() != suit_type:
            is_flush = False
        if is_straight and not isCurrentCardFollowsNextCard(card, hand):
            is_straight = False
    count_the_amount_of_each_rank_in_hand = Counter(collection_of_ranks_in_hand).most_common(5)
    # Royal flush 10,Straight flush 9,Four of a kind 8,Full house 7,Flush 6,
    # Straight 5,Three of a kind 4,Two pair 3, Pair 2, High Card 1
    if is_flush and is_straight:
        return {10: [count_the_amount_of_each_rank_in_hand[0][0]]} if hand[0].get_rank() == 14 else {
            9: [count_the_amount_of_each_rank_in_hand[0][0]]}
    if isFourOfAKind(count_the_amount_of_each_rank_in_hand):
        return {8: [count_the_amount_of_each_rank_in_hand[0][0], count_the_amount_of_each_rank_in_hand[1][0]]}
    if is_full_house(count_the_amount_of_each_rank_in_hand):
        return {7: [count_the_amount_of_each_rank_in_hand[0][0], count_the_amount_of_each_rank_in_hand[1][0]]}
    if is_flush:
        return {6: [count_the_amount_of_each_rank_in_hand[0][0], count_the_amount_of_each_rank_in_hand[1][0],
                    count_the_amount_of_each_rank_in_hand[2][0], count_the_amount_of_each_rank_in_hand[3][0],
                    count_the_amount_of_each_rank_in_hand[4][0]]}
    if is_straight:
        if hand[1].get_rank() == 5:
            return {5: [hand[1].get_rank()]}
        else:
            return {5: [hand[0].get_rank()]}
    if is_three_of_a_kind(count_the_amount_of_each_rank_in_hand):
        return {4: [count_the_amount_of_each_rank_in_hand[0][0], count_the_amount_of_each_rank_in_hand[1][0],
                    count_the_amount_of_each_rank_in_hand[2][0]]}
    if is_two_pair(count_the_amount_of_each_rank_in_hand):
        return {3: [count_the_amount_of_each_rank_in_hand[0][0], count_the_amount_of_each_rank_in_hand[1][0],
                    count_the_amount_of_each_rank_in_hand[2][0]]}
    if is_pair(count_the_amount_of_each_rank_in_hand):
        return {2: [count_the_amount_of_each_rank_in_hand[0][0], count_the_amount_of_each_rank_in_hand[1][0],
                    count_the_amount_of_each_rank_in_hand[2][0], count_the_amount_of_each_rank_in_hand[3][0]]}
    return high_card(count_the_amount_of_each_rank_in_hand)


def isCurrentCardFollowsNextCard(card, hand):
    return ((card == 4) or (card != 4 and hand[card].get_rank() == hand[card + 1].get_rank() + 1) or
            (card == 0 and hand[card].get_rank() == 14 and hand[card + 1].get_rank() == 5))


def isFourOfAKind(count):
    return count[0][1] == 4


def is_full_house(count):
    return count[0][1] == 3 and count[1][1] == 2


def is_three_of_a_kind(count):
    return count[0][1] == 3


def is_two_pair(count):
    return count[0][1] == 2 and count[1][1] == 2


def is_pair(count):
    return count[0][1] == 2


def high_card(count):
    return {1: [count[0][0], count[1][0], count[2][0], count[3][0], count[4][0]]}
