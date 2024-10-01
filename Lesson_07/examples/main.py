# %%
def sum_to(n):
    s = 0
    v = 1
    while v <= n:
        s += v
        v += 1
    return s


print(sum_to(10))


# %%

# An interesting question was first posed by a German mathematician called Lothar Collatz:
# the Collatz conjecture (also known as the 3n + 1 conjecture), is that this sequence
# terminates for all positive values of n. So far, no one has been able to prove it or
# disprove it! (A conjecture is a statement that might be true, but nobody knows for sure.)

def collatz(n):
    iterations = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        iterations += 1
    return iterations


print(collatz(17))


# %%
def print_first_evens(numbers):
    for item in numbers:
        if item % 2 == 0:
            print(item)
            break

    print("Done!")


print_first_evens([1, 3, 5, 8, 9, 10])


# %%
def print_all_evens(numbers):
    for item in numbers:
        if item % 2 != 0:
            continue
        print(item)

    print("Done!")


print_all_evens([12, 26, 4, 7, 18, 39])
