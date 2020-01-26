import Cards
import GameLogic

numOfHandsAndCards = 5


class Play:

    def __init__(self, deck):
        self._deck = Cards.Deck()
        player1_hands = []
        player2Hands = []
        for x in range(numOfHandsAndCards):
            player1_hands.append(Hand())
            player2Hands.append(Hand())
        deck.shuffle()

        deal_all_cards(deck, player1_hands, player2Hands)

        for item in player2Hands:
            for x in range(0, numOfHandsAndCards):
                print(item.__getitem__(x), end="  ")
            print('\n')
        print('-------------')
        for item in player1_hands:
            for x in range(0, numOfHandsAndCards):
                print(item.__getitem__(x), end="  ")
            print('\n')

        results = evaluate_hands(player1_hands, player2Hands, deck)

        for item in player2Hands:
            for x in range(0, numOfHandsAndCards):
                print(item.__getitem__(x), end="  ")
            print('\n')
        print('-------------')
        for item in player1_hands:
            for x in range(0, numOfHandsAndCards):
                print(item.__getitem__(x), end="  ")
            print('\n')

        for result in results:
            print(result)


class Hand:

    def __init__(self, cards_list=None):
        self.hand = []
        if cards_list is not None:
            self.create_hand(cards_list)

    def add_card(self, card):
        self.hand.append(card)

    def get_hand(self):
        return self.hand

    def create_hand(self, cards_list):
        for card in cards_list:
            self.hand.append(card)

    def __getitem__(self, x):
        return self.hand[x]


def deal_initial_cards(deck, player_1_hands, player_2_hands):
    for x in range(0, numOfHandsAndCards):
        player_1_hands[x].add_card(deck.deal_card())
        player_2_hands[x].add_card(deck.deal_card())


def deal_all_cards(deck, player_1_hands, player_2_hands):
    for x in range(0, numOfHandsAndCards):
        for y in range(numOfHandsAndCards):
            player_1_hands[x].add_card(deck.deal_card())
            player_2_hands[x].add_card(deck.deal_card())


def create_columns_hands(cards_rows):
    cards_columns = []
    create_hands_list = list(map(list, zip(*cards_rows)))
    for item in create_hands_list:
        cards_columns.append(Hand(item))
    return cards_rows + cards_columns


def evaluate_hands(my_cards_rows, other_player_cards_rows, deck_cards):
    player1_hands = crete_columns_hands(my_cards_rows)
    player2_hands = crete_columns_hands(other_player_cards_rows)
    return GameLogic.check_hands(player1_hands, player2_hands, deck_cards)


def crete_columns_hands(cards_rows):
    cardsColumns = []
    createHandsList = list(map(list, zip(*cards_rows)))
    for item in createHandsList:
        cardsColumns.append(Hand(item))
    return cards_rows + cardsColumns


if __name__ == '__main__':
    d = Cards.Deck()
    p = Play(d)
