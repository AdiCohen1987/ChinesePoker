def checkHands(player1Hands, player2Hands, deckCards):
    for x in range(0, 10):
        flowOfChecks(player1Hands[x])


def sortByRank(hand):
    for i in hand:
        'a'



def flowOfChecks(hand):
    orderedByRankHand = sorted(hand, key = lambda x: x.getRank(), reverse =True)
    orderedBySuitHand = sorted(hand, key = lambda x: x.getSuit(), reverse =True)

    isRoyal(orderedByRankHand)


def isRoyal(hand):
    sortedHand = sorted(hand, reverse=True)
    flag = True
    h = 10
    Cursuit = sortedHand[0].suit
    Currank = 14
    total_point = h * 13 ** 5 + self.point(sortedHand)
    for card in sortedHand:
        if card.suit != Cursuit or card.rank != Currank:
            flag = False
            break
        else:
            Currank -= 1
    if flag:
        print('Royal Flush')
        self.tlist.append(total_point)
    else:
        self.isStraightFlush(sortedHand)
