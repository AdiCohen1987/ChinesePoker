import Cards
import GameLogic
from const import NUM_OF_HANDS_AND_CARDS
from view import GameView


class Play:
    def __init__(self, deck,view):
        self.deck = Cards.Deck()
        player1Hands = []
        player2Hands = []
        for x in range(NUM_OF_HANDS_AND_CARDS):
            player1Hands.append(Hand())
            player2Hands.append(Hand())
        deck.shuffle()

        self.dealAllCards(deck, player1Hands, player2Hands)

        for item in player2Hands:
            for x in range(0, NUM_OF_HANDS_AND_CARDS):
                print(item.__getitem__(x), end="  ")
            print('\n')
        print('-------------')
        for item in player1Hands:
            for x in range(0, NUM_OF_HANDS_AND_CARDS):
                print(item.__getitem__(x), end="  ")
            print('\n')

        results = self.evaluateHands(player1Hands, player2Hands, deck)

        for item in player2Hands:
            for x in range(0, NUM_OF_HANDS_AND_CARDS):
                print(item.__getitem__(x), end="  ")
            print('\n')
        print('-------------')
        for item in player1Hands:
            for x in range(0, NUM_OF_HANDS_AND_CARDS):
                print(item.__getitem__(x), end="  ")
            print('\n')

        self.convertToView(player1Hands)
        for result in results:
            print(result)

    def dealInitialCards(self, deck, player1Hands, player2Hands):
        for x in range(0, NUM_OF_HANDS_AND_CARDS):
            player1Hands[x].addCard(deck.dealCard())
            player2Hands[x].addCard(deck.dealCard())

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

    def evaluateHands(self, myCardsRows, otherPlayerCardsRows, deckCards):
        player1Hands = self.createColumnsHands(myCardsRows)
        player2Hands = self.createColumnsHands(otherPlayerCardsRows)
        return GameLogic.checkHands(player1Hands, player2Hands, deckCards)

    def evaluateHands(self, my_cards_rows, other_player_cards_rows, deck_cards):
        player1Hands = self.createColumnsHands(my_cards_rows)
        player2Hands = self.createColumnsHands(other_player_cards_rows)
        return GameLogic.checkHands(player1Hands, player2Hands, deck_cards)

    def convertToView(self, playerHands):
        playerCardsForView = []
        for i in range(0, 5):
            for j in range(0, 5):
                hand = []
                hand.append(playerHands)
                if playerHands[i][j] is not None:
                    hand.append(str(playerHands[i][j].rank) + playerHands[i][j].suit)
                else:
                    hand.append('empty')
            playerCardsForView.append(hand)
        print('a')


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


if __name__ == '__main__':
    d = Cards.Deck()
    p1 = []
    p2 = []
    v = GameView(p1, p2)
    p = Play(d,v)
