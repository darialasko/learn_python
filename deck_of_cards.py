from random import shuffle


class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):
        name_suit = ["Hearts", "Diamonds", "Clubs", "Spades"]
        name_value = ["A", "2", "3", "4", "5", "6",
                      "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(suit, value)
                      for suit in name_suit for value in name_value]
        # for suit in name_suit:
        #    for value in name_value:
        #        card = Card(suit, value)
        #        self.cards.append(card)

    def count(self):
        return len(self.cards)

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def _deal(self, number):
        count = self.count()
        actual = min([count, number])
        if count == 0:
            raise ValueError("All cards have been dealt")
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        return self._deal(hand_size)

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)

    def __iter__(self):
        return iter(self.cards)


my_deck = Deck()
for card in my_deck:
    print(card)
