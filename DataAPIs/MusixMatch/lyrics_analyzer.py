import json
import re


def create_words_map(full_text):
    """
    This method takes full text and creates a mapping between each word in text to its count,
    it ignores all non text characters and transfers all words to lower case
    :param full_text:
    :return: dict <word, word_count>
    """
    counts = dict()
    full_text = " ".join(re.findall("[a-zA-Z]+", full_text))
    words = full_text.lower().split()

    for word in words:
        if word not in counts:
            counts[word] = 0
        counts[word] += 1

    return counts
