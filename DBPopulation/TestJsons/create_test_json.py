import json

# ORIGINAL PATHS
from DataAPIs.LastFM.retreive_data_from_last_fm import ARTISTS_FILE, SONGS_FILE
from DataAPIs.MusixMatch.lyrics_collector import LYRICS_FILE

LYRICS_PATH = '../../DataAPIs/MusixMatch/' + LYRICS_FILE
ARTISTS_PATH = '../../DataAPIs/LastFM/' + ARTISTS_FILE
SONGS_PATH = '../../DataAPIs/LastFM/' + SONGS_FILE

TEST_PREFIX = 'test_'
TEST_ARTISTS_PATH = TEST_PREFIX + ARTISTS_FILE
TEST_SONGS_PATH = TEST_PREFIX + SONGS_FILE
TEST_LYRICS_PATH = TEST_PREFIX + LYRICS_FILE

def create_jsons(num_of_categories, num_of_artists_per_category, num_of_songs_per_artist):
    artists_data = get_data_from_file(ARTISTS_PATH)
    songs_data = get_data_from_file(SONGS_PATH)
    lyrics_data = get_data_from_file(LYRICS_PATH)

    new_artists_data = {}
    for count, (category, artist_list) in enumerate(artists_data.iteritems()):
        if count == num_of_categories:
            break
        new_artists_data[category] = artist_list[:num_of_artists_per_category]

    new_songs_data = {}
    mbids = []
    for artist_list in new_artists_data.itervalues():
        for artist in artist_list:
            try:
                if songs_data[artist] is not None:
                    new_songs_data[artist] = songs_data[artist][:num_of_songs_per_artist]
                    mbids.extend([song_data[1] for song_data in new_songs_data[artist]])
            except Exception as e:
                print e

    new_lyrics_data = {}
    for mbid in mbids:
        data = lyrics_data.get(mbid)
        if data is None:
            continue
        new_lyrics_data[mbid] = data

    write_data_to_file(new_artists_data, TEST_ARTISTS_PATH)
    write_data_to_file(new_songs_data, TEST_SONGS_PATH)
    write_data_to_file(new_lyrics_data, TEST_LYRICS_PATH)


def get_data_from_file(filename):
    return json.load(open(filename))


def write_data_to_file(data, filename):
    with open(filename, 'w') as file_path:
        json.dump(data, file_path)

