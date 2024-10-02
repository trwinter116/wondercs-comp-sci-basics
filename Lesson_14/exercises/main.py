# %%
from test_helper import test


def merge(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):          # If xs list is finished,
            result.extend(ys[yi:]) # Add remaining items from ys
            return result          # And we're done.

        if yi >= len(ys):          # Same again, but swap roles
            result.extend(xs[xi:])
            return result

        # Both lists still have items, copy smaller item to result.
        if xs[xi] <= ys[yi]:
            result.append(xs[xi])
            xi += 1
        else:
            result.append(ys[yi])
            yi += 1


xs = [1,3,5,7,9,11,13,15,17,19]
ys = [4,8,12,16,20,24]

test(merge(xs, ys) == [1,3,4,5,7,8,9,11,12,13,15,16,17,19,20,24])

# %%

# Exercise 1
# Write a merge algorithm to return only those items that are present in both lists.

def present_in_both(xs, ys):
    pass

xs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ys = [5, 6, 11, 12, 13, 14, 15, 16, 17, 18]

test(present_in_both(xs, ys) == [5,6])


# %%

# Exercise 2
# Write a function that compares two lists and returns the count of matching items.

def count_matches(xs, ys):
    pass

test(count_matches([42,4,7,11,1,13], [2,5,7,11,13,17]) == 3)
