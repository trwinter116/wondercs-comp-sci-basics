import time

import base_game


class BlackJackHand(base_game.Hand):
    def get_score(self):
        total = 0
        self.cards.sort(reverse=True)
        for card in self.cards:
            if card.rank == 1:
                total += 1 if total > 10 else 11
            elif card.rank > 9:
                total += 10
            else:
                total += card.rank

        return total

    def is_bust(self):
        return self.get_score() > 21

    def __str__(self):
        s = f"Hand {self.name}"
        if self.is_empty():
            s += " is empty\n"
        elif self.is_bust():
            s += " is bust!\n"
        else:
            s += f" is {self.get_score()}\n"

        return s + base_game.Hand.__str__(self)


class BlackJackGame(base_game.CardGame):
    def play(self, names):
        # Make a hand for each player
        self.hands = []
        self.hands.extend(BlackJackHand(name) for name in names)
        # Make a hand for the dealer
        self.hands.append(BlackJackHand("Dealer"))

        # Deal the cards
        self.deck.deal(self.hands, len(self.hands) * 2)
        self.print_str_slowly("---------- Cards have been dealt ----------")
        self.print_hands()

        # Play a turn for each playr.
        for i in range(len(self.hands)):
            self.play_one_turn(i)

        # End the game.
        self.print_str_slowly("---------- Game is Over. Winner is: ----------")
        self.get_winner()

    def play_one_turn(self, i):
        while self.hands[i].get_score() < 16:
            self.hands[i].add(self.deck.pop())

    def print_hands(self):
        for i in self.hands:
            s = str(i)
            self.print_str_slowly(s)

    def get_winner(self):
        best_hand_total = 0
        winners = []
        for hand in self.hands:
            if hand.is_bust():
                continue
            if hand.get_score() > best_hand_total:
                best_hand_total = hand.get_score()
                winners = [hand]
            elif hand.get_score() == best_hand_total:
                if hand.name == "Dealer":
                    winners = [hand]
                else:
                    winners.append(hand)
            else:
                continue

        for i in winners:
            s = str(i)
            self.print_str_slowly(s)

    def print_str_slowly(self, s: str):
        for c in s:
            print(  c, end='', flush=True)
            time.sleep(0.085)
        print()