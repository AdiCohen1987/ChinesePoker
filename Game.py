import Cards
import GameLogic

numOfHandsAndCards = 5


class Play:
    def __init__(self, deck):
        self.deck = Cards.Deck()
        player1Hands = []
        player2Hands = []
        for x in range(numOfHandsAndCards):
            player1Hands.append(Hand())
            player2Hands.append(Hand())
        deck.shuffle()
        # dealInitialCards(deck, player1Hands, player2Hands)
        # for item in player1Hands:
        #     print(item.__getitem__(0),end="  ")
        # print()
        # for item in player2Hands:
        #     print(item.__getitem__(0), end="  ")
        dealAllCards(deck, player1Hands, player2Hands)
        for item in player2Hands:
            for x in range(0, numOfHandsAndCards):
                print(item.__getitem__(x), end="  ")
            print('\n')
        print('-------------')
        for item in player1Hands:
            for x in range(0, numOfHandsAndCards):
                print(item.__getitem__(x), end="  ")
            print('\n')

        evaluateHands(player1Hands, player2Hands, deck)
        print('\n')


class Hand:
    def __init__(self, cardsList=None):
        self.hand = []
        self.score = 0
        self.hasWon = False
        if cardsList is not None:
            self.createHand(cardsList)

    def addCard(self, card):
        self.hand.append(card)

    def getHand(self):
        return self.hand

    def createHand(self, cardsList):
        for card in cardsList:
            self.hand.append(card)

    def __getitem__(self, x):
        return self.hand[x]


def dealInitialCards(deck, player1Hands, player2Hands):
    for x in range(0, numOfHandsAndCards):
        player1Hands[x].addCard(deck.dealCard())
        player2Hands[x].addCard(deck.dealCard())


def dealAllCards(deck, player1Hands, player2Hands):
    for x in range(0, numOfHandsAndCards):
        for y in range(numOfHandsAndCards):
            player1Hands[x].addCard(deck.dealCard())
            player2Hands[x].addCard(deck.dealCard())


def createColumnsHands(cardsRows):
    cardsColumns = []
    createHandsList = list(map(list, zip(*cardsRows)))
    for item in createHandsList:
        cardsColumns.append(Hand(item))
    return cardsRows + cardsColumns


def evaluateHands(myCardsRows, otherPlayerCardsRows, deckCards):
    player1Hands = createColumnsHands(myCardsRows)
    player2Hands = createColumnsHands(otherPlayerCardsRows)
    GameLogic.checkHands(player1Hands, player2Hands, deckCards)


def createColumnsHands(cardsRows):
    cardsColumns = []
    createHandsList = list(map(list, zip(*cardsRows)))
    for item in createHandsList:
        cardsColumns.append(Hand(item))
    return cardsRows + cardsColumns


if __name__ == '__main__':
    d = Cards.Deck()
    p = Play(d)
