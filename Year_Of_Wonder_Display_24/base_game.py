import itertools


class Card:
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = [
        "narf",
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
    ]

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.ranks[self.rank]} of {self.suits[self.suit]}"

    def cmp(self, other):
        if self.suit > other.suit:
            return 1
        elif self.suit < other.suit:
            return -1
        # Suits are equal, checking rank
        if self.rank > other.rank:
            return 1
        elif self.rank < other.rank:
            return -1
        else:
            return 0

    def __eq__(self, other):
        return self.cmp(other) == 0

    def __le__(self, other):
        return self.cmp(other) <= 0

    def __ge__(self, other):
        return self.cmp(other) >= 0

    def __gt__(self, other):
        return self.cmp(other) > 0

    def __lt__(self, other):
        return self.cmp(other) < 0

    def __ne__(self, other):
        return self.cmp(other) != 0


class Deck:
    def __init__(self):
        self.cards = []
        self.cards.extend(
            Card(suit, rank) for suit, rank in itertools.product(range(4), range(1, 14))
        )

    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s = s + " " * i + str(self.cards[i]) + "\n"
        return s

    def shuffle(self):
        import random

        rng = random.Random()  # Create a random generator
        rng.shuffle(self.cards)

    def remove(self, card):
        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False

    def pop(self):
        return self.cards.pop()

    def is_empty(self):
        return self.cards == []

    def deal(self, hands, num_cards=999):
        num_hands = len(hands)
        for i in range(num_cards):
            if self.is_empty():
                break  # Break if out of cards
            card = self.pop()  # Take the top card
            hand = hands[i % num_hands]  # Whose turn is next?
            hand.add(card)  # Add the card to the hand


class Hand(Deck):
    def __init__(self, name=""):
        self.cards = []
        self.name = name

    def add(self, card):
        self.cards.append(card)

    def __str__(self):
        s = f"Hand {self.name}"
        s += " is empty\n" if self.is_empty() else " contains\n"
        return s + Deck.__str__(self)


class CardGame:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
