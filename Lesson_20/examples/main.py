# %%
eng2sp = {}
eng2sp["one"] = "uno"
eng2sp["two"] = "dos"

eng2sp
# %%
eng2sp["one"]

# %%
eng2sp = {"one": "uno", "two": "dos"}

eng2sp
# %%
inventory = {"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}
inventory
# %%
del inventory["pears"]
inventory
# %%
inventory["pears"] = 0
inventory

# %%
# * IMPORTANT FOR Exercises
inventory["bananas"] += 200
inventory
# %%
len(inventory)
# %%
for k in eng2sp.keys():
    print("Got key", k, "which maps to value", eng2sp[k])

eng2sp.keys()
# %%
eng2sp.values()
# %%
eng2sp.items()
# %%
for k, v in eng2sp.items():
    print("Got", k, "that maps to", v)
# %%
"one" in eng2sp
# %%
"six" in eng2sp
# %%
"dos" in eng2sp
# %%

# * Discuss Memoization


def r_fib(n):
    if n <= 1:
        return n
    else:
        return r_fib(n - 1) + r_fib(n - 2)


# %%
r_fib(20)

# %%
r_fib(30)

# %%
r_fib(35)

# %%
already_known = {0: 0, 1: 1}


def fib(n):
    if n not in already_known:
        new_value = fib(n - 1) + fib(n - 2)
        already_known[n] = new_value
    return already_known[n]


# %%
fib(100)
# %%
