import Cards
import GameLogic
from const import NUM_OF_HANDS_AND_CARDS


class Play:
    def __init__(self, deck):
        self.deck = Cards.Deck()
        player1Hands = []
        player2Hands = []
        for x in range(NUM_OF_HANDS_AND_CARDS):
            player1Hands.append(Hand())
            player2Hands.append(Hand())
        deck.shuffle()

        deal_all_cards(deck, player1Hands, player2Hands)

        for item in player2Hands:
            for x in range(0, NUM_OF_HANDS_AND_CARDS):
                print(item.__getitem__(x), end="  ")
            print('\n')
        print('-------------')
        for item in player1Hands:
            for x in range(0, NUM_OF_HANDS_AND_CARDS):
                print(item.__getitem__(x), end="  ")
            print('\n')

        results = evaluate_hands(player1Hands, player2Hands, deck)

        for item in player2Hands:
            for x in range(0, NUM_OF_HANDS_AND_CARDS):
                print(item.__getitem__(x), end="  ")
            print('\n')
        print('-------------')
        for item in player1Hands:
            for x in range(0, NUM_OF_HANDS_AND_CARDS):
                print(item.__getitem__(x), end="  ")
            print('\n')

        for result in results:
            print(result)

    def evaluate_hands(self, my_cards_rows, other_player_cards_rows, deck_cards):
        player1Hands = create_columns_hands(my_cards_rows)
        player2Hands = create_columns_hands(other_player_cards_rows)
        return GameLogic.checkHands(player1Hands, player2Hands, deck_cards)


class Hand:
    def __init__(self, cardsList=None):
        self.hand = []
        if cardsList is not None:
            self.create_hand(cardsList)

    def add_card(self, card):
        self.hand.append(card)

    def get_hand(self):
        return self.hand

    def create_hand(self, cardsList):
        for card in cardsList:
            self.hand.append(card)

    def __getitem__(self, x):
        return self.hand[x]


def deal_initial_cards(deck, player1Hands, player2Hands):
    for x in range(0, NUM_OF_HANDS_AND_CARDS):
        player1Hands[x].add_card(deck.dealCard())
        player2Hands[x].add_card(deck.dealCard())


def deal_all_cards(deck, player1Hands, player2Hands):
    for x in range(0, NUM_OF_HANDS_AND_CARDS):
        for y in range(NUM_OF_HANDS_AND_CARDS):
            player1Hands[x].add_card(deck.dealCard())
            player2Hands[x].add_card(deck.dealCard())


def create_columns_hands(cardsRows):
    cardsColumns = []
    createHandsList = list(map(list, zip(*cardsRows)))
    for item in createHandsList:
        cardsColumns.append(Hand(item))
    return cardsRows + cardsColumns


def evaluate_hands(myCardsRows, otherPlayerCardsRows, deckCards):
    player1Hands = create_columns_hands(myCardsRows)
    player2Hands = create_columns_hands(otherPlayerCardsRows)
    return GameLogic.checkHands(player1Hands, player2Hands, deckCards)



if __name__ == '__main__':
    d = Cards.Deck()
    p = Play(d)
