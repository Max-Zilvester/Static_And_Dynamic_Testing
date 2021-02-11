import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.value = 0
        self.card = Card("ace", 1)
        self.card1 = Card("diamond", 2)
        self.card2 = Card("spade", 3)
        self.cards = [self.card, self.card1, self.card2]
        self.CardGame = CardGame(self.card, 1)

    def test_check_for_ace__TRUE(self):
        self.assertEqual(True, self.CardGame.check_for_ace(self.card))

    def test_check_for_ace__FALSE(self):
        self.assertEqual(False, self.CardGame.check_for_ace(self.card2))

    def test_check_highest_card(self):
        self.assertEqual(self.card2, self.CardGame.highest_card(self.card1, self.card2))

    def test_check_cards_total(self):
        self.assertEqual("You have a total of 6", self.CardGame.cards_total(self.cards))

