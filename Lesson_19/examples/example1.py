# %%
print(55/0)

# %%
a = []
print(a[5])

# %%
tup = ("a", "b", "d", "d")
tup[2] = "c"

# %%
filename = input("Enter a file name: ")
try:
    f = open(filename, "r")
except Exception:
    print("There is no file named", filename)


# %%
def recursion_depth(number):
    print("Recursion depth number", number)
    recursion_depth(number + 1)


recursion_depth(0)


# %%
def recursion_depth(number):
    print("Recursion depth number", number)
    try:
        if number == 100:
            recursion_depth(f"{number}stringy")
        else:
            recursion_depth(number + 1)
    except RecursionError:
        print("I cannot go any deeper into this wormhole.")
    except TypeError:
        print("Don't add those things together")


recursion_depth(0)

# %%
def get_age():
    age = int(input("Please enter your age: "))

    if age < 0:
        raise ValueError(f"{age} is not a valid age.")

    return age

# %%
get_age()

# %%
