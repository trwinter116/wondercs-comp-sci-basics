import os
import random
import time

from black_jack import BlackJackGame

NAMES = ["Nick", "Danny", "Jonathan", "Caonabo", "Thomas", "Liam", "Daniel", "Khayila","Shemayah"]
DIRECTORY = "./Lesson_24/exercises"

while True:
    for filename in os.listdir(DIRECTORY):
        if os.path.isfile(os.path.join(DIRECTORY, filename)):
            with open(os.path.join(DIRECTORY, filename), 'r') as file:
                print(f"\n{'-'*180}\nReading file: {filename}\n{'-'*180}")

                for line in file:
                    for char in line:
                        print(  char, end='', flush=True)
                        time.sleep(0.085)

                print("\n\n")

        game = BlackJackGame()
        players = random.sample(NAMES, k=3)

        print(f"\n{'-'*180}\nPlaying Game with Players: {*players,}\n{'-'*180}")

        game.play(players)