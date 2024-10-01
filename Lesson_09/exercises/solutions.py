# %%
from test_helper import test


# Exercise 1
# Write a function that reverses its string argument, and satisfies the below tests.
def reverse(s):
    return s[::-1]

    # Alternate approach
    # reversed_string = ""  # Initialize an empty string to hold the reversed result

    # # Loop through the original string in reverse order
    # for i in range(len(s) - 1, -1, -1):
    #     reversed_string += s[i]  # Append each character to the reversed string

    # return reversed_string


test(reverse("happy") == "yppah")
test(reverse("Python") == "nohtyP")
test(reverse("") == "")
test(reverse("a") == "a")

# %%


# Exercise 2
# Write a function that removes all occurrences of a given letter from a string.
def remove_letter(letter, s):
    return "".join(char for char in s if char != letter)

    # Alternate approach
    # result = ""  # Initialize an empty string to hold the result

    # # Loop through each character in the original string
    # for char in s:
    #     if char != letter:  # Check if the character is not the letter to remove
    #         result += char  # Append the character to the result if it's not the letter

    # return result


test(remove_letter("a", "apple") == "pple")
test(remove_letter("a", "banana") == "bnn")
test(remove_letter("z", "banana") == "banana")
test(remove_letter("i", "Mississippi") == "Msssspp")
test(remove_letter("b", "") == "")
test(remove_letter("b", "c") == "c")

# %%

# Exercise 3
# Print a neat looking multiplication table like the below:
#        1   2   3   4   5   6   7   8   9  10  11  12
# :--------------------------------------------------
# 1:     1   2   3   4   5   6   7   8   9  10  11  12
# 2:     2   4   6   8  10  12  14  16  18  20  22  24
# 3:     3   6   9  12  15  18  21  24  27  30  33  36
# 4:     4   8  12  16  20  24  28  32  36  40  44  48
# 5:     5  10  15  20  25  30  35  40  45  50  55  60
# 6:     6  12  18  24  30  36  42  48  54  60  66  72
# 7:     7  14  21  28  35  42  49  56  63  70  77  84
# 8:     8  16  24  32  40  48  56  64  72  80  88  96
# 9:     9  18  27  36  45  54  63  72  81  90  99 108
# 10:    10  20  30  40  50  60  70  80  90 100 110 120
# 11:    11  22  33  44  55  66  77  88  99 110 121 132
# 12:    12  24  36  48  60  72  84  96 108 120 132 144

# Approach 1

print("      1   2   3   4   5   6   7   8   9  10  11  12")
print(":--------------------------------------------------")

layout = (
    "{0}:{1:>4}{2:>4}{3:>4}{4:>4}{5:>4}{6:>4}{7:>4}{8:>4}{9:>4}{10:>4}{11:>4}{12:>4}"
)
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for i in nums:
    print(
        layout.format(
            i,
            i * 1,
            i * 2,
            i * 3,
            i * 4,
            i * 5,
            i * 6,
            i * 7,
            i * 8,
            i * 9,
            i * 10,
            i * 11,
            i * 12,
        )
    )

# %%

# Approach 2
size = 12
header = " " * 3  # Initial space for alignment
for i in range(1, size + 1):
    header += f"{i:>4}"  # Right-align numbers in the header
print(header)

print(" " + ":" + "-" * (size * 4))  # Separator line

# Print the multiplication table
for i in range(1, size + 1):
    row = f"{i:>2}:"  # Right-align the row label
    for j in range(1, size + 1):
        row += f"{i * j:>4}"  # Right-align the product
    print(row)
# %%
