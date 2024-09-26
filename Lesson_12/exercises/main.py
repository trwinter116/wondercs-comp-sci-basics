# %%
import re

from test_helper import test

# We import the re library here to be used in pattern matching as we clean strings.
# For more information on regular expressions, visit https://regex101.com/.


# Exercise 1
# Write a function called clean_word which takes a string representation of a word and
# removed any punctuation from the string, returning the cleaned string.
def clean_word(word: str) -> str:

    # *** Write your code here ***

    return word


test(clean_word("what?") == "what")
test(clean_word("'now!'") == "now")
test(clean_word("?+='w-o-r-d!,@$()'") == "word")

# %%
# Exercise 2
# Write a function called has_dash_dash which takes a string representation of a word and
# checks if there are ANY instances of the pattern "--" contained in it. Returning a boolean
# true if there are, otherwise returning false.
def has_dash_dash(s: str):

    # *** Write your code here ***

    return True


test(has_dash_dash("distance--but"))
test(not has_dash_dash("several"))
test(has_dash_dash("spoke--"))
test(has_dash_dash("distance--but"))
test(not has_dash_dash("-yo-yo-"))

# %%
# Exercise 3
# Write a function called extract_words which takes a string containing a sentence,
# and returns a list of ALL of the words in the sentence. Every word must be cleaned and
# converted to lowercase.
def extract_words(s: str):

    # *** Write your code here ***

    return [s]


test(
    extract_words("Now is the time!  'Now', is the time? Yes, now.")
    == ["now", "is", "the", "time", "now", "is", "the", "time", "yes", "now"]
)
test(
    extract_words("she tried to curtsey as she spoke--fancy")
    == ["she", "tried", "to", "curtsey", "as", "she", "spoke", "fancy"]
)

# %%
# Exercise 4
# Write a function called word_count which takes a string containing a word and a list
# of words. The function must return the number of times the word appears in the list.
def word_count(word: str, word_list: list):

    # *** Write your code here ***

    return 0


test(word_count("now", ["now", "is", "time", "is", "now", "is", "is"]) == 2)
test(word_count("is", ["now", "is", "time", "is", "now", "the", "is"]) == 3)
test(word_count("time", ["now", "is", "time", "is", "now", "is", "is"]) == 1)
test(word_count("frog", ["now", "is", "time", "is", "now", "is", "is"]) == 0)

# %%
# Exercise 5
# Write a function called word_set which takes a list of words and then returns a new list
# containing only one of each word found in the provided. There must not be any duplicates.
def word_set(word_list: list):

    # *** Write your code here ***

    return word_set


test(word_set(["now", "is", "time", "is", "now", "is", "is"]) == ["is", "now", "time"])
test(word_set(["I", "a", "a", "is", "a", "is", "I", "am"]) == ["I", "a", "am", "is"])
test(
    word_set(["or", "a", "am", "is", "are", "be", "but", "am"])
    == ["a", "am", "are", "be", "but", "is", "or"]
)

# %%
# Exercise 6
# Write a function called longest_word which takes a list of words and then returns the
# length of the longest word in the list of words.
def longest_word(word_list: list):

    # *** Write your code here ***

    return len(word_list[0])

test(longest_word(["a", "apple", "pear", "grape"]) == 5)
test(longest_word(["a", "am", "I", "be"]) == 2)
test(longest_word(["this", "supercalifragilisticexpialidocious"]) == 34)
test(longest_word([]) == 0)
