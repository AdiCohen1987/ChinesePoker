import Cards
import GameLogic
from utils import Utilities

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

        results = evaluateHands(player1Hands, player2Hands, deck)

        for item in player2Hands:
            for x in range(0, numOfHandsAndCards):
                print(item.__getitem__(x), end="  ")
            print('\n')
        print('-------------')
        for item in player1Hands:
            for x in range(0, numOfHandsAndCards):
                print(item.__getitem__(x), end="  ")
            print('\n')

        for result in results:
            print(result)


class Hand:
    def __init__(self, cards_list=None):
        self.hand = []
        if cards_list is not None:
            self.createHand(cards_list)

    def addCard(self, card):
        self.hand.append(card)

    def getHand(self):
        return self.hand

    def createHand(self, cards_list):
        for card in cards_list:
            self.hand.append(card)

    def __getitem__(self, x):
        return self.hand[x]

    @property
    def runner(self):
        return Utilities.dealInitialCards, Utilities.dealAllCards, Utilities.create_columns_hands \
            , Utilities.evaluate_hands


if __name__ == '__main__':
    d = Cards.Deck()
    p = Play(d)
