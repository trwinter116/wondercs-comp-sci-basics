# %%
from test import test

# Write a function, recursive_min, that returns the smallest value in a nested number list.
# Assume there are no empty lists or sublists:


def recursive_min(nums):
    pass


test(recursive_min([2, 9, [1, 13], 8, 6]) == 1)
test(recursive_min([2, [[100, 1], 90], [10, 13], 8, 6]) == 1)
test(recursive_min([2, [[13, -7], 90], [1, 100], 8, 6]) == -7)
test(recursive_min([[[-13, 7], 90], 2, [1, 100], 8, 6]) == -13)

# %%

# Exercise 2
# Write a function which accepts a list, and flattens it using recursive methods.

def flatten(ls):
    pass


test(flatten([2, 9, [2, 1, 13, 2], 8, [2, 6]]) == [2, 9, 2, 1, 13, 2, 8, 2, 6])
test(flatten([[9, [7, 1, 13, 2], 8], [7, 6]]) == [9, 7, 1, 13, 2, 8, 7, 6])
test(flatten([[9, [7, 1, 13, 2], 8], [2, 6]]) == [9, 7, 1, 13, 2, 8, 2, 6])
test(
    flatten([["this", ["a", ["thing"], "a"], "is"], ["a", "easy"]])
    == ["this", "a", "thing", "a", "is", "a", "easy"]
)
test(flatten([]) == [])
