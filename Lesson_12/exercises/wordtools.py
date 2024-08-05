import re


def clean_word(word: str) -> str:
    return re.sub(r'[^\w\s]', '', re.sub(r'\d', '', word))


def extract_words(s: str):
    if has_dash_dash(s):
        s = re.sub("--", " ", s)

    word_list = s.split(" ")
    part_clean_words = [clean_word(word).lower() for word in word_list]
    return [word for word in part_clean_words if len(word) > 0]


def has_dash_dash(s: str):
    return "--" in s


def longest_word(word_list: list):
    longest_word_value = 0

    for word in word_list:
        if len(word) > longest_word_value:
            longest_word_value = len(word)

    return longest_word_value


def word_count(word: str, word_list: list):
    return word_list.count(word)


def word_set(word_list: list):
    word_set = []
    for candidate in word_list:
        if candidate not in word_set:
            word_set.append(candidate)

    word_set.sort()
    return word_set
