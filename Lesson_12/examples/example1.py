# %%
import random

rng = random.Random()

dice_throw = rng.randrange(1, 7)
dice_throw

# %%
delay_in_seconds = rng.random() * 5.0
delay_in_seconds

# %%
r_odd = rng.randrange(1, 100, 2)
r_odd

# %%
cards = list(range(52))
rng.shuffle(cards)
cards

# %%
drng = random.Random(123)
dice_throw = drng.randrange(1, 7)
dice_throw

#%%
dice_throw = drng.randrange(1, 7)
dice_throw

# %%
def make_random_ints_no_dups(num, lower_bound, upper_bound):
    """
    Generate a list containing num random ints between
    lower_bound and upper_bound. upper_bound is an open bound.
    The result list cannot contain duplicates.
    """
    result = []
    rng = random.Random()
    for _ in range(num):
        while True:
            candidate = rng.randrange(lower_bound, upper_bound)
            if candidate not in result:
                break
        result.append(candidate)
    return result


make_random_ints_no_dups(5, 1, 10000000)

# %%
