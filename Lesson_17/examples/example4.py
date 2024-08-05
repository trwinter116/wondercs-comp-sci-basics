import random

import draw_queens


def main():

    bd = list(range(8))  # Generate the initial permutation
    num_found = 0
    tries = 0
    while num_found < 10:
        random.shuffle(bd)
        tries += 1
        if not has_clashes(bd):
            draw_queens.draw_board(bd)
            tries = 0
            num_found += 1


main()
