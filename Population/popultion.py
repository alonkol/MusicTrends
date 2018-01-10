import json

from Population.insert_queries import insert_into_lyrics_table, insert_into_words_per_song_table, \
    insert_into_categories_table, insert_into_artists_table, insert_into_artist_to_category_table, \
    insert_into_songs_table, insert_into_song_to_artist_table, insert_into_song_to_category_table

LYRICS_PATH = '../LyricsCollection/lyrics.json'
ARTISTS_PATH = '../LastFmApiHandler/artists.json'
SONGS_PATH = '../LastFmApiHandler/songs_with_mbid.json'


class Populator():
    def __init__(self):
        self._lyrics_data = self._get_data_from_file(LYRICS_PATH)
        self._artists_data = self._get_data_from_file(ARTISTS_PATH)
        self._songs_data = self._get_data_from_file(SONGS_PATH)

    @staticmethod
    def _get_data_from_file(filename):
        return json.load(open(filename))

    def _insert_lyrics_data_into_tables(self, song_id, mbid):
        song_lyrics_data = self._lyrics_data.get(mbid)
        if song_lyrics_data is None:
            return
        insert_into_lyrics_table(song_id, song_lyrics_data['lyrics'], song_lyrics_data['language'])
        insert_into_words_per_song_table(song_id, song_lyrics_data['lyrics'])

    def populate_tables(self):
        artists_in_db = {}
        songs_in_db = {}
        for category, artists in self._artists_data.iteritems():
            category_id = insert_into_categories_table(category)
            for artist in artists:
                if artist not in artists_in_db:
                    artist_id = insert_into_artists_table(artist)
                    artists_in_db[artist] = artist_id
                artist_id = artists_in_db[artist]
                insert_into_artist_to_category_table(artist_id, category_id)
                songs = self._songs_data.get(artist, [])
                if songs is not None:
                    for song in songs:
                        mbid = song[1]
                        if mbid not in songs_in_db:
                            song_id = insert_into_songs_table(song[0])
                            self._insert_lyrics_data_into_tables(song_id, mbid)
                            songs_in_db[mbid] = song_id
                        song_id = songs_in_db[mbid]
                        insert_into_song_to_artist_table(song_id, artist_id)
                        insert_into_song_to_category_table(song_id, category_id)

"""
THE FOLLOWING FUNCTIONS ARE NOT IN USE
"""

def populate_categories_table():
    d = get_data_from_file('categories.json')
    for k in d:
        insert_into_categories_table(k['name'])


def populate_artists_table():
    artists_per_category = get_data_from_file('artists.json')
    artists = set()
    for artist_list in artists_per_category.values():
        for artist in artist_list:
            # make sure no duplicates
            if artist not in artists:
                print(artist)
                # handle non-ascii characters
                artist = artist.encode('unicode_escape')
                print(len(artist))
                artists.add(artist)
                insert_into_artists_table(artist)


def populate_songs_table():
    songs_per_artist = get_data_from_file('songs_with_mbid.json')
    mbids = set()
    for songs_list in songs_per_artist.values():
        if songs_list is not None:
            for song in songs_list:
                # make sure no duplicates
                if song[1] not in mbids:
                    # handle non-ascii characters
                    song = song.encode('unicode_escape')
                    insert_into_songs_table(song)
                    print len(song)


def populate_song_to_artist_table():
    songs_per_artist = get_data_from_file('songs_unique.json')
    songs = set()
    i = 0
    for artist in songs_per_artist.keys():
        if songs_per_artist[artist] is not None:
            for song in songs_per_artist[artist]:
                i+=1
                # make sure no duplicates
                if song not in songs:
                    songs.add(song)
                    # handle non-ascii characters
                    song1= song.encode('unicode_escape')
                    artist1 = artist.encode('unicode_escape')
                    insert_into_song_to_artist_table(song1, artist1)


def populate_artist_to_category_table():
    artists_per_category = get_data_from_file('artists.json')
    for category in artists_per_category.keys():
        for artist in artists_per_category[category]:
            # handle non-ascii characters
            artist_encoded = artist.encode('unicode_escape')
            category_encoded = category.encode('unicode_escape')
            insert_into_artist_to_category_table(artist_encoded, category_encoded)


def populate_song_to_category_table():
    songs_per_artist = get_data_from_file('songs_unique.json')
    artists_per_category = get_data_from_file('artists.json')
    for category in artists_per_category.keys():
        for artist in artists_per_category[category]:
            for song in songs_per_artist[artist]:
                    # handle non-ascii characters
                    song_encoded = song.encode('unicode_escape')
                    category_encoded = category.encode('unicode_escape')
                    insert_into_artist_to_category_table(song_encoded, category_encoded)


def main():
    Populator().populate_tables()


if __name__ == '__main__':
    main()