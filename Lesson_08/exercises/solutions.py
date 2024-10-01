# %%
from test_helper import test

# Exercise 1
# Execute the below cells, thinking about what you expect the output to be and if the output
# is different, think about why.
"Python"[1]  # y

# %%
"Strings are sequences of characters."[5]  # g

# %%
len("wonderful")  # 9

# %%
"Mystery"[:4]  # Myst

# %%
"p" in "Pineapple"  # True

# %%
"apple" in "Pineapple"  # True

# %%
"pear" not in "Pineapple"  # True

# %%

# Exercise 2
# Modify the below code so that Ouack and Quack are spelled correctly when printed.
prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
    if letter in "OQ":
        print(letter + "u" + suffix)
    else:
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


def count_letters(strng, letter):
    count = 0
    for char in strng:
        if char == letter:
            count += 1

    return count


test(count_letters("banana", "a") == 3)
test(count_letters("mississippi", "i") == 4)

# %%
