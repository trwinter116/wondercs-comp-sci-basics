# %%
from test_helper import test


class Card:
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["narf", "Ace", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.ranks[self.rank]} of {self.suits[self.suit]}"

    def cmp(self, other):
        if self.suit < other.suit:
            return -1
        if self.suit > other.suit:
            return 1
        # Suits are the same, check ranks
        if self.rank < other.rank:
            return -1
        if self.rank > other.rank:
            return 1
        # Ranks are the same, its the same card
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

# %%
# Exercise 1
# Currently if you compare an Ace, it will rank lower than 2. For most card games however,
# an Ace ranks higher than a king. Modify the cmp class method so that Ace ranks higher than a king
ace = Card(1, 1)
king = Card(1, 13)
test(ace > king)
test(ace >= king)
