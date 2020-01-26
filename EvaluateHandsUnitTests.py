import unittest

import Cards
import Game
from GameLogic import evaluate_hand


# Royal flush 10,Straight flush 9,Four of a kind 8,Full house 7,Flush 6,
# Straight 5,Three of a kind 4,Two pair 3, Pair 2, High Card 1
class TestHandsEvaluation(unittest.TestCase):
    def test_royalFlush(self):
        hand = Game.Hand()
        hand.add_card(Cards.Card(14, 'S'))
        hand.add_card(Cards.Card(13, 'S'))
        hand.add_card(Cards.Card(12, 'S'))
        hand.add_card(Cards.Card(11, 'S'))
        hand.add_card(Cards.Card(10, 'S'))
        self.assertEqual(evaluate_hand(hand), {10: []})

    def test_straightFlush(self):
        hand = Game.Hand()
        hand.add_card(Cards.Card(13, 'S'))
        hand.add_card(Cards.Card(12, 'S'))
        hand.add_card(Cards.Card(11, 'S'))
        hand.add_card(Cards.Card(10, 'S'))
        hand.add_card(Cards.Card(9, 'S'))
        self.assertEqual(evaluate_hand(hand), {9: [13]})

    def test_fourOfAKind(self):
        hand = Game.Hand()
        hand.add_card(Cards.Card(12, 'S'))
        hand.add_card(Cards.Card(12, 'D'))
        hand.add_card(Cards.Card(12, 'H'))
        hand.add_card(Cards.Card(12, 'C'))
        hand.add_card(Cards.Card(9, 'S'))
        self.assertEqual(evaluate_hand(hand), {8: [12, 9]})

    def test_fullHouse(self):
        hand = Game.Hand()
        hand.add_card(Cards.Card(11, 'S'))
        hand.add_card(Cards.Card(11, 'D'))
        hand.add_card(Cards.Card(11, 'H'))
        hand.add_card(Cards.Card(5, 'C'))
        hand.add_card(Cards.Card(5, 'S'))
        self.assertEqual(evaluate_hand(hand), {7: [11, 5]})

    def test_fullHouse(self):
        hand = Game.Hand()
        hand.add_card(Cards.Card(11, 'S'))
        hand.add_card(Cards.Card(11, 'D'))
        hand.add_card(Cards.Card(11, 'H'))
        hand.add_card(Cards.Card(5, 'C'))
        hand.add_card(Cards.Card(5, 'S'))
        self.assertEqual(evaluate_hand(hand), {7: [11, 5]})

    def test_flush(self):
        hand = Game.Hand()
        hand.add_card(Cards.Card(13, 'S'))
        hand.add_card(Cards.Card(11, 'S'))
        hand.add_card(Cards.Card(10, 'S'))
        hand.add_card(Cards.Card(7, 'S'))
        hand.add_card(Cards.Card(4, 'S'))
        self.assertEqual(evaluate_hand(hand), {6: [13, 11, 10, 7, 4]})

    def test_straight(self):
        hand = Game.Hand()
        hand.add_card(Cards.Card(14, 'S'))
        hand.add_card(Cards.Card(5, 'S'))
        hand.add_card(Cards.Card(4, 'S'))
        hand.add_card(Cards.Card(3, 'C'))
        hand.add_card(Cards.Card(2, 'S'))
        self.assertEqual(evaluate_hand(hand), {5: [5]})

    def test_threeOfAKind(self):
        hand = Game.Hand()
        hand.add_card(Cards.Card(14, 'S'))
        hand.add_card(Cards.Card(5, 'H'))
        hand.add_card(Cards.Card(5, 'S'))
        hand.add_card(Cards.Card(5, 'C'))
        hand.add_card(Cards.Card(2, 'S'))
        self.assertEqual(evaluate_hand(hand), {4: [5, 14, 2]})

    def test_twoPairs(self):
        hand = Game.Hand()
        hand.add_card(Cards.Card(10, 'S'))
        hand.add_card(Cards.Card(9, 'H'))
        hand.add_card(Cards.Card(9, 'S'))
        hand.add_card(Cards.Card(8, 'C'))
        hand.add_card(Cards.Card(8, 'S'))
        self.assertEqual(evaluate_hand(hand), {3: [9, 8, 10]})

    def test_pair(self):
        hand = Game.Hand()
        hand.add_card(Cards.Card(10, 'S'))
        hand.add_card(Cards.Card(9, 'H'))
        hand.add_card(Cards.Card(7, 'S'))
        hand.add_card(Cards.Card(4, 'C'))
        hand.add_card(Cards.Card(4, 'S'))
        self.assertEqual(evaluate_hand(hand), {2: [4, 10, 9, 7]})

    def test_highCard(self):
        hand = Game.Hand()
        hand.add_card(Cards.Card(12, 'S'))
        hand.add_card(Cards.Card(9, 'H'))
        hand.add_card(Cards.Card(7, 'S'))
        hand.add_card(Cards.Card(5, 'C'))
        hand.add_card(Cards.Card(4, 'S'))
        self.assertEqual(evaluate_hand(hand), {1: [12, 9, 7, 5, 4]})


if __name__ == '__main__':
    unittest.main()
