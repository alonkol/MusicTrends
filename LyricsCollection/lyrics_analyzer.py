import json


def create_words_map(full_text):
    """
    This method takes full text and creates a mapping between each word in text to its count
    :param full_text:
    :return: dict <word, word_count>
    """
    counts = dict()
    words = full_text.split()

    for word in words:
        if word not in counts:
            counts[word] = 0
        counts[word] += 1

    return counts


def create_word_count_for_lyrics():
    data = json.load(open('lyrics.json'))
    word_counts = {}
    for song_name, lyrics in data.iteritems():
        word_counts[song_name] = create_words_map(lyrics)

    with open('lyrics_count.json', 'w') as lyrics_count_file:
        json.dump(word_counts, lyrics_count_file)

