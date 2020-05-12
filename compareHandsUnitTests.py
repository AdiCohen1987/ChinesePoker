import unittest

import cards
from gameLogic import evaluateHand, checkWhichHandIsBetter


# Royal flush 10,Straight flush 9,Four of a kind 8,Full house 7,Flush 6,
# Straight 5,Three of a kind 4,Two pair 3, Pair 2, High Card 1
class TestHandsEvaluation(unittest.TestCase):
    def test_royalFlush_Vs_straightFlush(self):
        hand1 = [cards.Card(14, 'S'), cards.Card(13, 'S'), cards.Card(12, 'S'), cards.Card(11, 'S'),
                 cards.Card(10, 'S')]
        hand2 = [cards.Card(13, 'S'), cards.Card(12, 'S'), cards.Card(11, 'S'), cards.Card(10, 'S'), cards.Card(9, 'S')]
        result = checkWhichHandIsBetter(evaluateHand(hand1), evaluateHand(hand2))
        self.assertEqual(result, "Player: 1 won with: Royal Flush HighestCard: A")

    def test_flush_Vs_flush(self):
        hand1 = [cards.Card(10, 'S'), cards.Card(9, 'S'), cards.Card(8, 'S'), cards.Card(4, 'S'), cards.Card(2, 'S')]
        hand2 = [cards.Card(13, 'H'), cards.Card(10, 'H'), cards.Card(8, 'H'), cards.Card(7, 'H'), cards.Card(3, 'H')]
        result = checkWhichHandIsBetter(evaluateHand(hand1), evaluateHand(hand2))
        self.assertEqual(result, "Player: 2 won with: Flush HighestCard: K")


if __name__ == '__main__':
    unittest.main()
