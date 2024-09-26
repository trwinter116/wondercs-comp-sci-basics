# %%
from test_helper import test


def r_max(nxs):
    largest = None
    first_time = True
    for e in nxs:
        if isinstance(e, list):
            val = r_max(e)
        else:
            val = e

        if first_time or val > largest:
            largest = val
            first_time = False

    return largest


test(r_max([2, 9, [1, 13], 8, 6]) == 13)
test(r_max([2, [[100, 7], 90], [1, 13], 8, 6]) == 100)
test(r_max([[[13, 7], 90], 2, [1, 100], 8, 6]) == 100)
test(r_max(["joe", ["sam", "ben"]]) == "sam")
