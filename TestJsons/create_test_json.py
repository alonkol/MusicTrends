import json

# ORIGINAL PATHS
from LastFmApiHandler.retreive_data_from_last_fm import ARTISTS_FILE, SONGS_FILE


LYRICS_PATH = '../LyricsCollection/' + 'lyrics.json'
ARTISTS_PATH = '../LastFmApiHandler/' + ARTISTS_FILE
SONGS_PATH = '../LastFmApiHandler/' + SONGS_FILE


TEST_ARTISTS_PATH = 'test_artists.json'
TEST_SONGS_PATH = 'test_songs_with_mbid.json'
TEST_LYRICS_PATH = 'test_lyrics.json'

NUMBER_OF_CATEGORIES = 10
NUMBER_OF_ARTIST_PER_CATEGORY = 3
NUMBER_OF_SONGS_PER_ARTIST = 3


def get_data_from_file(filename):
    return json.load(open(filename))


def write_data_to_file(data, filename):
    with open(filename, 'w') as file_path:
        json.dump(data, file_path)

artists_data = get_data_from_file(ARTISTS_PATH)
songs_data = get_data_from_file(SONGS_PATH)

new_artists_data = {}
for count, (category, artist_list) in enumerate(artists_data.iteritems()):
    if count == NUMBER_OF_CATEGORIES:
        break
    new_artists_data[category] = artist_list[:NUMBER_OF_ARTIST_PER_CATEGORY]

new_songs_data = {}
for artist_list in new_artists_data.itervalues():
    for artist in artist_list:
        new_songs_data[artist] = songs_data[artist][:NUMBER_OF_SONGS_PER_ARTIST]

write_data_to_file(new_artists_data, TEST_ARTISTS_PATH)
write_data_to_file(new_songs_data, TEST_SONGS_PATH)

