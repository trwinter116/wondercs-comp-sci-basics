# %%
from test_helper import test

ss = "Hello, World!"
tt = ss.upper()
tt
# %%
fruit = "banana"
m = fruit[1]
m

# %%
m = fruit[0]
m

# %%
list(enumerate(fruit))

# %%
len(fruit)

# %%
# For example, in Robert McCloskey’s book Make Way for Ducklings, the names of the ducklings
# are Jack, Kack, Lack, Mack, Nack, Ouack, Pack, and Quack. This loop outputs these names
# in order:

prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
    print(letter + suffix)


# %%
s = "Pirates of the Caribbean"
s[:7]

# %%
s[11:14]

# %%
s[15:24]

# %%
# An error is expected here.
s[0] = "p"

# %%
"p" in "apple"

# %%
"i" in "apple"

# %%
"ap" in "apple"

# %%
"pa" in "apple"

# %%
"x" not in "apple"


# %%
def remove_vowels(s):
    vowels = "aeiouAEIOU"
    s_sans_vowels = ""
    for x in s:
        if x not in vowels:
            s_sans_vowels += x
    return s_sans_vowels


test(remove_vowels("compsci") == "cmpsc")
test(remove_vowels("aAbEefIijOopUus") == "bfjps")


# %%
def count_a(text):
    count = 0
    for c in text:
        if c == "a":
            count += 1
    return(count)

test(count_a("banana") == 3)

# %%
