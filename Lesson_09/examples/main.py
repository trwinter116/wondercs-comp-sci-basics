# %%
from test_helper import test


def find(strng, ch):
    """
    Find and return the index of ch in strng.
    Return -1 if ch does not occur in strng.
    """
    ix = 0
    while ix < len(strng):
        if strng[ix] == ch:
            return ix
        ix += 1
    return -1


test(find("Compsci", "p") == 3)
test(find("Compsci", "C") == 0)
test(find("Compsci", "i") == 6)
test(find("Compsci", "x") == -1)


# %%


def find2(strng, ch, start):
    ix = start
    while ix < len(strng):
        if strng[ix] == ch:
            return ix
        ix += 1
    return -1


test(find2("banana", "a", 2) == 3)


# %%


def find(strng, ch, start=0, end=None):
    ix = start
    if end is None:
        end = len(strng)
    while ix < end:
        if strng[ix] == ch:
            return ix
        ix += 1
    return -1


ss = "Python strings have some interesting methods."
test(find(ss, "s") == 7)
test(find(ss, "s", 7) == 7)
test(find(ss, "s", 8) == 13)
test(find(ss, "s", 8, 13) == -1)
test(find(ss, ".") == len(ss) - 1)

# %%

"banana".find("nan")

# %%

"banana".find("na", 3)

# %%

ss = "Well I never did said Alice"
wds = ss.split()
wds

# %%

punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"


def remove_punctuation(s):
    s_sans_punct = ""
    for letter in s:
        if letter not in punctuation:
            s_sans_punct += letter
    return s_sans_punct


# %%

import string


def remove_punctuation(s):
    s_without_punct = ""
    for letter in s:
        if letter not in string.punctuation:
            s_without_punct += letter
    return s_without_punct


test(
    remove_punctuation('"Well, I never did!", said Alice.')
    == "Well I never did said Alice"
)
test(remove_punctuation("Are you very, very, sure?") == "Are you very very sure")

# %%

my_story = """
Pythons are constrictors, which means that they will 'squeeze' the life
out of their prey. They coil themselves around their prey and with
each breath the creature takes the snake will squeeze a little tighter
until they stop breathing completely. Once the heart stops the prey
is swallowed whole. The entire animal is digested in the snake's
stomach except for fur or feathers. What do you think happens to the fur,
feathers, beaks, and eggshells? The 'extra stuff' gets passed out as ---
you guessed it --- snake POOP! """

wds = remove_punctuation(my_story).split()
wds

# %%
"His name is {0}".format("Arthur")

# %%
name = "Alice"
age = "10"
"I am {1} and I am {0} years old.".format(age, name)

# %%
f"I am {name} and I am {age} years old."

# %%
n1 = 4
n2 = 5
"2**10 = {0} and {1} * {2} = {3:f}".format(2**10, n1, n2, n1 * n2)

# %%
f"2**10 = {2**10} and {n1} * {n2} = {n1 * n2:f}"
# %%
f"Pi to three decimal places is {3.1415926:.3f}"

# %%
f"|||{'Paris':<15}|||{'Whitney':^15}|||{'Hilton':>15}|||Born in 1981|||"

# %%
integer = 123456
f"The decimal value {integer} converts to hex value {integer:x}"

# %%

letter = """
Dear {0} {2}.
    {0}, I have an interesting money-making proposition for you!
    If you deposit $10 million into my bank account, I can
    double your money ...
"""

print(letter.format("Paris", "Whitney", "Hilton"))
print(letter.format("Bill", "Henry", "Gates"))

# %%
print("i\ti**2\ti**3\ti**5\ti**10\ti**20")
for i in range(1, 11):
    print(i, "\t", i**2, "\t", i**3, "\t", i**5, "\t",
                                            i**10, "\t", i**20)

# %%
layout = "{0:>4}{1:>6}{2:>6}{3:>8}{4:>13}{5:>24}"

print(layout.format("i", "i**2", "i**3", "i**5", "i**10", "i**20"))
for i in range(1, 11):
    print(layout.format(i, i**2, i**3, i**5, i**10, i**20))

# %%
