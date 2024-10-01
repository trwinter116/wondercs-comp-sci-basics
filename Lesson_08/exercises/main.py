# %%
from test_helper import test

# Exercise 1
# Execute the below cells, thinking about what you expect the output to be and if the output
# is different, think about why.
"Python"[1]

# %%
"Strings are sequences of characters."[5]

# %%
len("wonderful")

# %%
"Mystery"[:4]

# %%
"p" in "Pineapple"

# %%
"apple" in "Pineapple"

# %%
"pear" not in "Pineapple"

# %%

# Exercise 2
# Modify the below code so that Ouack and Quack are spelled correctly when printed.
prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
    print(letter + suffix)


# %%

# Exercise 3
# Encapsulate the below code in a function named count_letters and generalize it so that
# it accepts the string and the letter as arguments. Make the function return the number
# of characters, rather than print the answer.

fruit = "banana"
count = 0
for char in fruit:
    if char == "a":
        count += 1
print(count)

def count_letters():
    pass

test(count_letters("banana", "a") == 3)
test(count_letters("mississippi", "i") == 4)
