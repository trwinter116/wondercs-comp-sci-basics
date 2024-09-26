# %%
import re

from test_helper import test


def clean_word(word: str) -> str:
    return re.sub(r'[^\w\s]', '', re.sub(r'\d', '', word))


test(clean_word("what?") == "what")
test(clean_word("'now!'") == "now")
test(clean_word("?+='w-o-r-d!,@$()'") == "word")


def has_dash_dash(s: str):
    return "--" in s


test(has_dash_dash("distance--but"))
test(not has_dash_dash("several"))
test(has_dash_dash("spoke--"))
test(has_dash_dash("distance--but"))
test(not has_dash_dash("-yo-yo-"))

def extract_words(s: str):
    if has_dash_dash(s):
        s = re.sub("--", " ", s)

    word_list = s.split(" ")
    part_clean_words = [clean_word(word).lower() for word in word_list]
    return [word for word in part_clean_words if len(word) > 0]


test(
    extract_words("Now is the time!  'Now', is the time? Yes, now.")
    == ["now", "is", "the", "time", "now", "is", "the", "time", "yes", "now"]
)
test(
    extract_words("she tried to curtsey as she spoke--fancy")
    == ["she", "tried", "to", "curtsey", "as", "she", "spoke", "fancy"]
)

def word_count(word: str, word_list: list):
    return word_list.count(word)


test(word_count("now", ["now", "is", "time", "is", "now", "is", "is"]) == 2)
test(word_count("is", ["now", "is", "time", "is", "now", "the", "is"]) == 3)
test(word_count("time", ["now", "is", "time", "is", "now", "is", "is"]) == 1)
test(word_count("frog", ["now", "is", "time", "is", "now", "is", "is"]) == 0)

def word_set(word_list: list):
    word_set = []
    for candidate in word_list:
        if candidate not in word_set:
            word_set.append(candidate)

    word_set.sort()
    return word_set


test(word_set(["now", "is", "time", "is", "now", "is", "is"]) == ["is", "now", "time"])
test(word_set(["I", "a", "a", "is", "a", "is", "I", "am"]) == ["I", "a", "am", "is"])
test(
    word_set(["or", "a", "am", "is", "are", "be", "but", "am"])
    == ["a", "am", "are", "be", "but", "is", "or"]
)

def longest_word(word_list: list):
    longest_word_value = 0

    for word in word_list:
        if len(word) > longest_word_value:
            longest_word_value = len(word)

    return longest_word_value


test(longest_word(["a", "apple", "pear", "grape"]) == 5)
test(longest_word(["a", "am", "I", "be"]) == 2)
test(longest_word(["this", "supercalifragilisticexpialidocious"]) == 34)
test(longest_word([]) == 0)
