import json

from DataAPIs.LastFM.retreive_data_from_last_fm import SONGS_FILE, ARTISTS_FILE
from DataAPIs.MusixMatch.lyrics_collector import LYRICS_FILE
from DataAPIs.Youtube.DataEnrichment import PopulateVideos, PopulateComments
from DBPopulation.insert_queries import insert_into_lyrics_table, insert_into_words_per_song_table, \
    insert_into_categories_table, insert_into_artists_table, insert_into_artist_to_category_table, \
    insert_into_songs_table, insert_into_song_to_artist_table, insert_into_song_to_category_table

from Server.config import cursor
from TestJsons.create_test_json import TEST_ARTISTS_PATH, TEST_SONGS_PATH, TEST_LYRICS_PATH
from TestJsons import create_test_json

CREATE_DB_PATH = '../DB/creation.sql'
DELETE_DB_PATH = '../DB/delete_tables.sql'
LYRICS_PATH = '../MusixMatch/' + LYRICS_FILE
ARTISTS_PATH = '../LastFM/' + ARTISTS_FILE
SONGS_PATH = '../LastFM/' + SONGS_FILE

TEST_JSONS_PATH = '../TestJsons/'
FULL_TEST_LYRICS_PATH = TEST_JSONS_PATH + TEST_LYRICS_PATH
FULL_TEST_ARTISTS_PATH = TEST_JSONS_PATH + TEST_ARTISTS_PATH
FULL_TEST_SONGS_PATH = TEST_JSONS_PATH + TEST_SONGS_PATH


class Populator():
    def __init__(self, numCat, numArtist, numSongs):
        lyricsPath = LYRICS_PATH
        artistsPath = ARTISTS_PATH
        songsPath = SONGS_PATH

        if numCat is not None and numArtist is not None and numSongs is not None:
            create_test_json.create_jsons(numCat, numArtist, numSongs)
            lyricsPath = FULL_TEST_LYRICS_PATH
            artistsPath = FULL_TEST_ARTISTS_PATH
            songsPath = FULL_TEST_SONGS_PATH

        self._lyrics_data = self._get_data_from_file(lyricsPath)
        self._artists_data = self._get_data_from_file(artistsPath)
        self._songs_data = self._get_data_from_file(songsPath)


    @staticmethod
    def _get_data_from_file(filename):
        return json.load(open(filename))

    def _insert_lyrics_data_into_tables(self, song_id, mbid):
        song_lyrics_data = self._lyrics_data.get(mbid)
        if song_lyrics_data is None:
            return
        insert_into_lyrics_table(song_id, song_lyrics_data['lyrics'], song_lyrics_data['language'])
        insert_into_words_per_song_table(song_id, song_lyrics_data['lyrics'])

    def populate_lastfm_musixmatch_data(self):
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



    @staticmethod
    def run_sql_file(file_path):
        # Open and read the file as a single buffer
        fd = open(file_path, 'r')
        sql_file = fd.read()
        fd.close()

        # all SQL commands (split on ';')
        sql_commands = sql_file.split(';')

        # Execute every command from the input file
        for command in sql_commands[: -1]:
            command += ";"
            try:
                cursor.execute(command)
            except Exception as e:
                raise


def main():

    numOfCategories = 10
    artistsPerCategory = 10
    songsPerArtist = 10

    populator = Populator(numOfCategories, artistsPerCategory, songsPerArtist)

    try:
        # delete old db
        populator.run_sql_file(DELETE_DB_PATH)
        # create tables
        populator.run_sql_file(CREATE_DB_PATH)
    except Exception:
        raise

    # populate Songs, Artists, Categories, Lyrics, SongToArtist, ArtistToCategory, SongToCategory TABLES
    populator.populate_lastfm_musixmatch_data()

    # populate Youtube videos data
    PopulateVideos()

    # populate Youtube videos data
    PopulateComments()

if __name__ == '__main__':
    main()

