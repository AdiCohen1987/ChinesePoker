import cards
import gameLogic
from const import NUM_OF_HANDS_AND_CARDS


class Play:
    player1Hands = []
    player2Hands = []
    deck = None

    def __init__(self):
        self.deck = cards.Deck()
        for x in range(NUM_OF_HANDS_AND_CARDS):
            self.player1Hands.append(Hand())
            self.player2Hands.append(Hand())
        self.deck.shuffle()
        self.dealInitialCards()
        self.convertToView(self.player1Hands)
        self.convertToView(self.player2Hands)

        # for result in results:
        #     print(result)

    def __getPlayer1Hands__(self):
        return self.player1Hands

    def __getPlayer2Hands__(self):
        return self.player2Hands

    def __setPlayer1Hands__(self, newHand):
        self.player1Hands = newHand

    def __setPlayer2Hands__(self, newHand):
        self.player1Hands = newHand

    def __getDeck__(self):
        return self.deck

    def dealInitialCards(self):
        for x in range(0, NUM_OF_HANDS_AND_CARDS):
            self.player1Hands[x].addCard(self.deck.dealCard())
            self.player2Hands[x].addCard(self.deck.dealCard())

    def dealAllCards(self, deck, player1Hands, player2Hands):
        for x in range(0, NUM_OF_HANDS_AND_CARDS):
            for y in range(NUM_OF_HANDS_AND_CARDS):
                player1Hands[x].addCard(deck.dealCard())
                player2Hands[x].addCard(deck.dealCard())

    def createColumnsHands(self, cardsRows):
        cardsColumns = []
        createHandsList = list(map(list, zip(*cardsRows)))
        for item in createHandsList:
            cardsColumns.append(Hand(item))
        return cardsRows + cardsColumns

    def evaluateHands(self, player1, player2, deckCards):
        player1Hands = self.createColumnsHands(player1)
        player2Hands = self.createColumnsHands(player2)
        return gameLogic.checkHands(player1Hands, player2Hands, deckCards)

    def convertToView(self, playerHands):
        playerCardsForView = []
        for i in range(0, 5):
            for j in range(0, 5):
                hand = [playerHands]
                try:
                    hand.append(str(playerHands[i][j].rank) + playerHands[i][j].suit)
                except IndexError:
                    pass
            playerCardsForView.append(hand)


class Hand:
    def __init__(self, cardsList=None):
        self.hand = []
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
