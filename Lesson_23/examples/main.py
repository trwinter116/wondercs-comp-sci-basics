# %%
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


# %%
card1 = Card(1, 11)
print(card1)

# %%
card2 = Card(1, 3)
print(card2)

# %%
card1.suits[1] = "Diamonds"
print(card1)

# %%
print(card2)

# %%
# Write comparison logic
# __eq__, __le__, __ge__, __gt__, __lt__, __ne__

card1 = Card(1, 11)
card2 = Card(1, 3)
card3 = Card(1, 11)
card1 < card2

# %%
card1 == card3

# %%


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


# %%
red_deck = Deck()
blue_deck = Deck()

# %%
print(red_deck)

# %%
blue_deck.shuffle()
print(blue_deck)
# %%


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


# %%
deck = Deck()
deck.shuffle()
hand = Hand("Frank")
deck.deal([hand], 5)
print(hand)

# %%


class CardGame:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()


class OldMaidHand(Hand):
    def remove_matches(self):
        count = 0
        original_cards = self.cards[:]
        for card in original_cards:
            match = Card(3 - card.suit, card.rank)
            if match in self.cards:
                self.cards.remove(card)
                self.cards.remove(match)
                print("Hand {0}: {1} matches {2}".format(self.name, card, match))
                count += 1
        return count


class OldMaidGame(CardGame):
    def play(self, names):
        # Remove Queen of Clubs
        self.deck.remove(Card(0, 12))

        # Make a hand for each player
        self.hands = []
        for name in names:
            self.hands.append(OldMaidHand(name))

        # Deal the cards
        self.deck.deal(self.hands)
        print("---------- Cards have been dealt")
        self.print_hands()

        # Remove initial matches
        matches = self.remove_all_matches()
        print("---------- Matches discarded, play begins")
        self.print_hands()

        # Play until all 50 cards are matched
        turn = 0
        num_hands = len(self.hands)
        while matches < 25:
            matches += self.play_one_turn(turn)
            turn = (turn + 1) % num_hands

        print("---------- Game is Over")
        self.print_hands()

    def remove_all_matches(self):
        count = 0
        for hand in self.hands:
            count += hand.remove_matches()
        return count

    def play_one_turn(self, i):
        if self.hands[i].is_empty():
            return 0
        neighbor = self.find_neighbor(i)
        picked_card = self.hands[neighbor].pop()
        self.hands[i].add(picked_card)
        print("Hand", self.hands[i].name, "picked", picked_card)
        count = self.hands[i].remove_matches()
        self.hands[i].shuffle()
        return count

    def find_neighbor(self, i):
        num_hands = len(self.hands)
        for next in range(1, num_hands):
            neighbor = (i + next) % num_hands
            if not self.hands[neighbor].is_empty():
                return neighbor

    def print_hands(self):
        for i in self.hands:
            print(i)


# %%
game = OldMaidGame()
game.play(["Allen", "Jeff", "Chris"])

# %%
