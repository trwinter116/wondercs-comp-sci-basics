# %%
from test_helper import test

friends = ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]


def search_linear(xs, target):
    """Find and return the index of target in sequence xs"""
    for i, v in enumerate(xs):
        if v == target:
            return i
    return -1


test(search_linear(friends, "Zoe") == 1)
test(search_linear(friends, "Joe") == 0)
test(search_linear(friends, "Paris") == 6)
test(search_linear(friends, "Bill") == -1)


# %%
def find_unknown_words(vocab, wds):
    """Return a list of words in wds that do not occur in vocab"""
    result = []
    for w in wds:
        if search_linear(vocab, w) < 0:
            result.append(w)
    return result


vocab = ["apple", "boy", "dog", "down", "fell", "girl", "grass", "the", "tree"]
book_words = "the apple fell from the tree to the grass".split()
test(find_unknown_words(vocab, book_words) == ["from", "to"])
test(find_unknown_words([], book_words) == book_words)
test(find_unknown_words(vocab, ["the", "boy", "fell"]) == [])


# %%
def load_words_from_file(filename):
    """Read words from filename, return list of words."""
    with open(filename, "r") as f:
        file_content = f.read()
    return file_content.split()


bigger_vocab = load_words_from_file("vocab.txt")
print(
    "There are {0} words in the vocab, starting with\n {1} ".format(
        len(bigger_vocab), bigger_vocab[:6]
    )
)


# %%
def text_to_words(the_text):
    """return a list of words with all punctuation removed,
    and all in lowercase.
    """

    my_substitutions = the_text.maketrans(
        # If you find any of these
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
        # Replace them by these
        "abcdefghijklmnopqrstuvwxyz                                          ",
    )

    # Translate the text now.
    cleaned_text = the_text.translate(my_substitutions)
    return cleaned_text.split()


def get_words_in_book(filename):
    """Read a book from filename, and return a list of its words."""
    with open(filename, "r") as f:
        content = f.read()
    return text_to_words(content)


book_words = get_words_in_book("alice_in_wonderland.txt")
print(
    "There are {0} words in the book, the first 100 are\n{1}".format(
        len(book_words), book_words[:100]
    )
)

# %%
import time

t0 = time.process_time()
missing_words = find_unknown_words(bigger_vocab, book_words)
t1 = time.process_time()
print("There are {0} unknown words.".format(len(missing_words)))
print("That took {0:.4f} seconds.".format(t1 - t0))


# %%
def search_binary(xs, target):
    """Find and return the index of key in sequence xs"""
    lb = 0
    ub = len(xs)
    while True:
        if lb == ub:  # If region of interest (ROI) becomes empty
            return -1

        # Next probe should be in the middle of the ROI
        mid_index = (lb + ub) // 2

        # Fetch the item at that position
        item_at_mid = xs[mid_index]

        # print("ROI[{0}:{1}](size={2}), probed='{3}', target='{4}'"
        #       .format(lb, ub, ub-lb, item_at_mid, target))

        # How does the probed item compare to the target?
        if item_at_mid == target:
            return mid_index  # Found it!
        if item_at_mid < target:
            lb = mid_index + 1  # Use upper half of ROI next time
        else:
            ub = mid_index  # Use lower half of ROI next time


xs = [2, 3, 5, 7, 11, 13, 17, 23, 29, 31, 37, 43, 47, 53]
test(search_binary(xs, 20) == -1)
test(search_binary(xs, 99) == -1)
test(search_binary(xs, 1) == -1)
for i, v in enumerate(xs):
    test(search_binary(xs, v) == i)

# %%
t0 = time.process_time()
missing_words = find_unknown_words(bigger_vocab, book_words)
t1 = time.process_time()
print("There are {0} unknown words.".format(len(missing_words)))
print("That took {0:.4f} seconds.".format(t1 - t0))

# %%
xs = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
ys = [4, 8, 12, 16, 20, 24]

t0 = time.process_time()
new_list = xs + ys
new_list.sort()
t1 = time.process_time()
print("That took {0:.9f} seconds.".format(t1 - t0))


# %%
def merge(xs, ys):
    """merge sorted lists xs and ys. Return a sorted result"""
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):  # If xs list is finished,
            result.extend(ys[yi:])  # Add remaining items from ys
            return result  # And we're done.

        if yi >= len(ys):  # Same again, but swap roles
            result.extend(xs[xi:])
            return result

        # Both lists still have items, copy smaller item to result.
        if xs[xi] <= ys[yi]:
            result.append(xs[xi])
            xi += 1
        else:
            result.append(ys[yi])
            yi += 1


zs = xs + ys
zs.sort()
test(merge(xs, []) == xs)
test(merge([], ys) == ys)
test(merge([], []) == [])
test(merge(xs, ys) == zs)
test(merge([1, 2, 3], [3, 4, 5]) == [1, 2, 3, 3, 4, 5])
test(
    merge(["a", "big", "cat"], ["big", "bite", "dog"])
    == ["a", "big", "big", "bite", "cat", "dog"]
)
# %%
t0 = time.process_time()
new_list2 = merge(xs, ys)
t1 = time.process_time()
print("That took {0:.9f} seconds.".format(t1 - t0))
# %%


def find_unknowns_merge_pattern(vocab, wds):
    """Both the vocab and wds must be sorted.  Return a new
    list of words from wds that do not occur in vocab.
    """

    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(vocab):
            result.extend(wds[yi:])
            return result

        if yi >= len(wds):
            return result

        if vocab[xi] == wds[yi]:  # Good, word exists in vocab
            yi += 1

        elif vocab[xi] < wds[yi]:  # Move past this vocab word,
            xi += 1

        else:  # Got word that is not in vocab
            result.append(wds[yi])
            yi += 1


# %%
t0 = time.process_time()
missing_words = find_unknowns_merge_pattern(bigger_vocab, book_words)
t1 = time.process_time()
print("There are {0} unknown words.".format(len(missing_words)))
print("That took {0:.4f} seconds.".format(t1 - t0))
# %%
