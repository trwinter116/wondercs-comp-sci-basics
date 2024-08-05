# %%
import time


def do_my_sum(xs):
    s = 0
    for v in xs:
        s += v
    return s


sz = 10000000  # Lets have 10 million elements in the list
testdata = range(sz)

t0 = time.process_time()
my_result = do_my_sum(testdata)
t1 = time.process_time()
print("my_result    = {0} (time taken = {1:.4f} seconds)".format(my_result, t1 - t0))

t2 = time.process_time()
their_result = sum(testdata)
t3 = time.process_time()
print("their_result = {0} (time taken = {1:.4f} seconds)".format(their_result, t3 - t2))

# %%
