import unittest

import Cards
import Game
from GameLogic import evaluateHand


# Royal flush 10,Straight flush 9,Four of a kind 8,Full house 7,Flush 6,
# Straight 5,Three of a kind 4,Two pair 3, Pair 2, High Card 1
class TestHandsEvaluation(unittest.TestCase):
    def test_royalFlush(self):
        hand = Game.Hand()
        hand.addCard(Cards.Card(14, 'S'))
        hand.addCard(Cards.Card(13, 'S'))
        hand.addCard(Cards.Card(12, 'S'))
        hand.addCard(Cards.Card(11, 'S'))
        hand.addCard(Cards.Card(10, 'S'))
        self.assertEqual(evaluateHand(hand), {10: []})

    def test_straightFlush(self):
        hand = Game.Hand()
        hand.addCard(Cards.Card(13, 'S'))
        hand.addCard(Cards.Card(12, 'S'))
        hand.addCard(Cards.Card(11, 'S'))
        hand.addCard(Cards.Card(10, 'S'))
        hand.addCard(Cards.Card(9, 'S'))
        self.assertEqual(evaluateHand(hand), {9: [13]})

    def test_fourOfAKind(self):
        hand = Game.Hand()
        hand.addCard(Cards.Card(12, 'S'))
        hand.addCard(Cards.Card(12, 'D'))
        hand.addCard(Cards.Card(12, 'H'))
        hand.addCard(Cards.Card(12, 'C'))
        hand.addCard(Cards.Card(9, 'S'))
        self.assertEqual(evaluateHand(hand), {8: [12, 9]})

    def test_fullHouse(self):
        hand = Game.Hand()
        hand.addCard(Cards.Card(11, 'S'))
        hand.addCard(Cards.Card(11, 'D'))
        hand.addCard(Cards.Card(11, 'H'))
        hand.addCard(Cards.Card(5, 'C'))
        hand.addCard(Cards.Card(5, 'S'))
        self.assertEqual(evaluateHand(hand), {7: [11, 5]})

    def test_fullHouse(self):
        hand = Game.Hand()
        hand.addCard(Cards.Card(11, 'S'))
        hand.addCard(Cards.Card(11, 'D'))
        hand.addCard(Cards.Card(11, 'H'))
        hand.addCard(Cards.Card(5, 'C'))
        hand.addCard(Cards.Card(5, 'S'))
        self.assertEqual(evaluateHand(hand), {7: [11, 5]})

    def test_flush(self):
        hand = Game.Hand()
        hand.addCard(Cards.Card(13, 'S'))
        hand.addCard(Cards.Card(11, 'S'))
        hand.addCard(Cards.Card(10, 'S'))
        hand.addCard(Cards.Card(7, 'S'))
        hand.addCard(Cards.Card(4, 'S'))
        self.assertEqual(evaluateHand(hand), {6: [13, 11, 10, 7, 4]})

    def test_straight(self):
        hand = Game.Hand()
        hand.addCard(Cards.Card(14, 'S'))
        hand.addCard(Cards.Card(5, 'S'))
        hand.addCard(Cards.Card(4, 'S'))
        hand.addCard(Cards.Card(3, 'C'))
        hand.addCard(Cards.Card(2, 'S'))
        self.assertEqual(evaluateHand(hand), {5: [5]})

    def test_threeOfAKind(self):
        hand = Game.Hand()
        hand.addCard(Cards.Card(14, 'S'))
        hand.addCard(Cards.Card(5, 'H'))
        hand.addCard(Cards.Card(5, 'S'))
        hand.addCard(Cards.Card(5, 'C'))
        hand.addCard(Cards.Card(2, 'S'))
        self.assertEqual(evaluateHand(hand), {4: [5, 14, 2]})

    def test_twoPairs(self):
        hand = Game.Hand()
        hand.addCard(Cards.Card(10, 'S'))
        hand.addCard(Cards.Card(9, 'H'))
        hand.addCard(Cards.Card(9, 'S'))
        hand.addCard(Cards.Card(8, 'C'))
        hand.addCard(Cards.Card(8, 'S'))
        self.assertEqual(evaluateHand(hand), {3: [9, 8, 10]})

    def test_pair(self):
        hand = Game.Hand()
        hand.addCard(Cards.Card(10, 'S'))
        hand.addCard(Cards.Card(9, 'H'))
        hand.addCard(Cards.Card(7, 'S'))
        hand.addCard(Cards.Card(4, 'C'))
        hand.addCard(Cards.Card(4, 'S'))
        self.assertEqual(evaluateHand(hand), {2: [4, 10, 9, 7]})

    def test_highCard(self):
        hand = Game.Hand()
        hand.addCard(Cards.Card(12, 'S'))
        hand.addCard(Cards.Card(9, 'H'))
        hand.addCard(Cards.Card(7, 'S'))
        hand.addCard(Cards.Card(5, 'C'))
        hand.addCard(Cards.Card(4, 'S'))
        self.assertEqual(evaluateHand(hand), {1: [12, 9, 7, 5, 4]})


if __name__ == '__main__':
    unittest.main()
