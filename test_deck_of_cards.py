import unittest
from deck_of_cards import Card, Deck


class CardTests(unittest.TestCase):
    def setUp(self):
        self.cards = Card("Hearts", "A")

    def test_init(self):
        """cards should have a suit and value"""
        self.assertEqual(self.cards.suit, "Hearts")
        self.assertEqual(self.cards.value, "A")

    def test_repr(self):
        """repr should return a string {self.value} of {self.suit} """
        self.assertEqual(repr(self.cards), "A of Hearts")


class DeckTests(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_init(self):
        self.assertTrue(isinstance(self.deck.cards, list))
        self.assertEqual(self.deck.cards, 52)

    def test_count(self):
        self.assertEqual(self.deck.count(), 52)
        self.deck.cards.pop()
        self.assertEqual(self.deck.count(), 51)

    def test_repr(self):
        self.assertEqual(repr(self.deck), "Deck of 52 cards")

    def test_deal_if_empty(self):
        self.deck._deal(self.deck.count())
        with self.assertRaises(ValueError):
            self.deck._deal(1)

    def test_deal_sufficient_cards(self):
        cards = self.deck._deal(10)
        self.assertEqual(len(cards), 10)
        self.assertEqual(self.deck.count(), 42)

    def test_deal_insufficient_cards(self):
        cards = self.deck._deal(100)
        self.assertEqual(len(cards), 52)
        self.assertEqual(self.deck.count(), 0)

    def test_deal_card(self):
        card = self.deck.cards[-1]
        deal_card = self.deck.deal_card()
        self.assertEqual(card, deal_card)
        self.assertEqual(self.deck.count(), 51)

    def test_deal_hand(self):
        cards = self.deck.deal_hand(20)
        self.assertEqual(len(cards), 20)
        self.assertEqual(self.deck.count(), 32)

    def test_shuffle_full_deck(self):
        cards = self.deck.cards[:]
        self.deck.shuffle()
        self.assertNotEqual(cards, self.deck.cards)
        self.assertEqual(self.deck.count(), 52)

    def test_shuffle_not_full_deck(self):
        self.deck._deal(1)
        with self.assertRaises(ValueError):
            self.deck.shuffle()
