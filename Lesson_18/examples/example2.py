# %%
from test import test

#print(sum([1,2 ,3 ,4]))
print(sum([2, 9, [1, 13], 8, 6]))


# %%
def r_sum(nested_num_list):
    tot = 0
    for element in nested_num_list:
        if isinstance(element, list):
            tot += r_sum(element)
        else:
            tot += element
    return tot


test(r_sum([2, 9, [1, 13], 8, 6]) == 39)
test(r_sum([2, [[100, 7], 90], [1, 13], 8, 6]) == 227)

# %%
