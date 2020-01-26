import unittest

import Cards
from GameLogic import evaluate_hand, check_which_hand_is_better


# Royal flush 10,Straight flush 9,Four of a kind 8,Full house 7,Flush 6,
# Straight 5,Three of a kind 4,Two pair 3, Pair 2, High Card 1
class TestHandsEvaluation(unittest.TestCase):
    def test_royalFlush_Vs_straightFlush(self):
        hand1 = [Cards.Card(14, 'S'), Cards.Card(13, 'S'), Cards.Card(12, 'S'), Cards.Card(11, 'S'),
                 Cards.Card(10, 'S')]
        hand2 = [Cards.Card(13, 'S'), Cards.Card(12, 'S'), Cards.Card(11, 'S'), Cards.Card(10, 'S'), Cards.Card(9, 'S')]
        result = check_which_hand_is_better(evaluate_hand(hand1), evaluate_hand(hand2))
        self.assertEqual(result, "Player: 1 won with: Royal Flush HighestCard: A")

    def test_flush_Vs_flush(self):
        hand1 = [Cards.Card(10, 'S'), Cards.Card(9, 'S'), Cards.Card(8, 'S'), Cards.Card(4, 'S'), Cards.Card(2, 'S')]
        hand2 = [Cards.Card(13, 'H'), Cards.Card(10, 'H'), Cards.Card(8, 'H'), Cards.Card(7, 'H'), Cards.Card(3, 'H')]
        result = check_which_hand_is_better(evaluate_hand(hand1), evaluate_hand(hand2))
        self.assertEqual(result, "Player: 2 won with: Flush HighestCard: K")


if __name__ == '__main__':
    unittest.main()
