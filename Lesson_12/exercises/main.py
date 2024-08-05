from test import test

from wordtools import (
    clean_word,
    extract_words,
    has_dash_dash,
    longest_word,
    word_count,
    word_set,
)

test(clean_word("what?") == "what")
test(clean_word("'now!'") == "now")
test(clean_word("?+='w-o-r-d!,@$()'") == "word")

test(has_dash_dash("distance--but"))
test(not has_dash_dash("several"))
test(has_dash_dash("spoke--"))
test(has_dash_dash("distance--but"))
test(not has_dash_dash("-yo-yo-"))

test(
    extract_words("Now is the time!  'Now', is the time? Yes, now.")
    == ["now", "is", "the", "time", "now", "is", "the", "time", "yes", "now"]
)
test(
    extract_words("she tried to curtsey as she spoke--fancy")
    == ["she", "tried", "to", "curtsey", "as", "she", "spoke", "fancy"]
)

test(word_count("now", ["now", "is", "time", "is", "now", "is", "is"]) == 2)
test(word_count("is", ["now", "is", "time", "is", "now", "the", "is"]) == 3)
test(word_count("time", ["now", "is", "time", "is", "now", "is", "is"]) == 1)
test(word_count("frog", ["now", "is", "time", "is", "now", "is", "is"]) == 0)

test(word_set(["now", "is", "time", "is", "now", "is", "is"]) == ["is", "now", "time"])
test(word_set(["I", "a", "a", "is", "a", "is", "I", "am"]) == ["I", "a", "am", "is"])
test(
    word_set(["or", "a", "am", "is", "are", "be", "but", "am"])
    == ["a", "am", "are", "be", "but", "is", "or"]
)

test(longest_word(["a", "apple", "pear", "grape"]) == 5)
test(longest_word(["a", "am", "I", "be"]) == 2)
test(longest_word(["this", "supercalifragilisticexpialidocious"]) == 34)
test(longest_word([]) == 0)
