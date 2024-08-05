# %%
from test import test

# %%

# Exercise 1
# Write a program that reads a string and returns a dictionary of the letters of the alphabet
# in alphabetical order which occur in the string together with the number of times each
# letter occurs. Case should be ignored.


def letter_count(sentence):
    letter_counts = {}
    for char in sentence:
        if char.isalpha():
            char = char.lower()
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1
    return dict(sorted(letter_counts.items()))


test(letter_count("ThiS is String with Upper and lower case Letters")["a"] == 2)

# %%
