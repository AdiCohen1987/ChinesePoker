import GameLogic
from Game import numOfHandsAndCards, Hand


# TODO:
#       check usage of this methods,
#       If they're being used once, then this file is useless and class Utilities should be moved back to Game.

# but class of all this functions together is still better in my opinion.

class Utilities:
    @staticmethod
    def dealInitialCards(deck, player1_hands, player2_hands):
        for x in range(0, numOfHandsAndCards):
            player1_hands[x].addCard(deck.dealCard())
            player2_hands[x].addCard(deck.dealCard())

    @staticmethod
    def dealAllCards(deck, player1_hands, player2_hands):
        for x in range(0, numOfHandsAndCards):
            for y in range(numOfHandsAndCards):
                player1_hands[x].addCard(deck.dealCard())
                player2_hands[x].addCard(deck.dealCard())

    @staticmethod
    def create_columns_hands(cards_rows):
        cardsColumns = []
        createHandsList = list(map(list, zip(*cards_rows)))
        for item in createHandsList:
            cardsColumns.append(Hand(item))
        return cards_rows + cardsColumns

    @staticmethod
    def evaluate_hands(my_cards_rows, other_player_cards_rows, deck_cards):
        player1_hands = my_cards_rows.create_columns_hands(my_cards_rows)
        player2_hands = my_cards_rows.create_columns_hands(other_player_cards_rows)
        return GameLogic.check_hands(player1_hands, player2_hands, deck_cards)
