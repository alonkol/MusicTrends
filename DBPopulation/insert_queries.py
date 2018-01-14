from DataAPIs.MusixMatch.lyrics_analyzer import create_words_map
from Server import config

INSERT_CATEGORY = "INSERT INTO Categories VALUES (Default, %s);"
INSERT_ARTIST = "INSERT INTO Artists VALUES (Default, %s, Default);"
INSERT_SONG = "INSERT INTO Songs VALUES (Default, %s);"
INSERT_SONG_TO_ARTIST = "INSERT INTO SongToArtist VALUES (%s, %s);"
INSERT_ARTIST_TO_CATEGORY = "INSERT INTO ArtistToCategory VALUES (%s, %s);"
INSERT_SONG_TO_CATEGORY = "INSERT INTO SongToCategory VALUES (%s, %s);"
INSERT_LYRICS = "INSERT INTO Lyrics VALUES (%s, %s);"
INSERT_LYRICS_MY_ISAM = "INSERT INTO Lyrics_MyISAM VALUES (%s, %s);"

INSERT_WORDS_PER_SONG = "INSERT INTO WordsPerSong VALUES (%s, %s, %s);"


def insert_into_categories_table(category_name):
    sql_insert = INSERT_CATEGORY
    cursor = config.cursor
    try:
        affected_count = cursor.execute(sql_insert, (category_name,))
        config.dbconnection.commit()
    except Exception as e:
        print e
        print "failed to insert value %s into Categories' " % category_name
        return
    return cursor.lastrowid


def insert_into_artists_table(artist_name):
    sql_insert = INSERT_ARTIST
    cursor = config.cursor
    try:
        # handle non-ascii charactes
        if not is_valid_ascii(artist_name):
            return
        affected_count = cursor.execute(sql_insert, (artist_name,))
        config.dbconnection.commit()
    except Exception as e:
        print e
        print "failed to insert value %s into Artists' " % artist_name
        return
    return cursor.lastrowid


def insert_into_songs_table(song_name):
    sql_insert = INSERT_SONG
    cursor = config.cursor
    try:
        # handle non-ascii charactes
        if not is_valid_ascii(song_name):
            return
        affected_count = cursor.execute(sql_insert, (song_name,))
        config.dbconnection.commit()
    except Exception as e:
        print e
        print "failed to insert value %s into Songs' " % song_name
        return
    return cursor.lastrowid


def insert_into_song_to_artist_table(song_id, artist_id):
    sql_insert = INSERT_SONG_TO_ARTIST
    cursor = config.cursor
    try:
        cursor.execute(sql_insert, (song_id, artist_id))
        config.dbconnection.commit()
    except Exception as e:
        print e
        print "failed to insert song %s and artist %s into SongToArtist' " % (song_id, artist_id)
        return
    return cursor.lastrowid


def insert_into_artist_to_category_table(artist_id, category_id):
    sql_insert = INSERT_ARTIST_TO_CATEGORY
    cursor = config.cursor
    try:
        cursor.execute(sql_insert, (artist_id, category_id))
        config.dbconnection.commit()
    except Exception as e:
        print e
        print "failed to insert artist %s and category %s into ArtistToCategory' " % (artist_id, category_id)
        return
    return cursor.lastrowid


def insert_into_song_to_category_table(song_id, category_id):
    sql_insert = INSERT_SONG_TO_CATEGORY
    cursor = config.cursor
    try:
        cursor.execute(sql_insert, (song_id, category_id))
        config.dbconnection.commit()
    except Exception as e:
        print e
        print "failed to insert song %s and category %s into SongToCategory' " % (song_id, category_id)
        return
    return cursor.lastrowid


def insert_into_lyrics_table(song_id, lyrics):
        sql_insert = INSERT_LYRICS
        sql_insert_to_my_isam = INSERT_LYRICS_MY_ISAM
        cursor = config.cursor
        try:
            cursor.execute(sql_insert, (song_id, lyrics))
            cursor.execute(sql_insert_to_my_isam, (song_id, lyrics))
            config.dbconnection.commit()
        except Exception as e:
            print e
            print "failed to insert lyrics for song %s' " % song_id
            return
        return cursor.lastrowid


def insert_into_words_per_song_table(song_id, lyrics):
    words_count = create_words_map(lyrics)
    sql_insert = INSERT_WORDS_PER_SONG
    cursor = config.cursor
    try:
        for word, cnt in words_count.iteritems():
            word = word[:20]
            cursor.execute(sql_insert, (song_id, word, cnt))
        config.dbconnection.commit()
    except Exception as e:
        print e
        print "failed to insert words for song %s' " % song_id
        return
    return cursor.lastrowid


def is_valid_ascii(string):
    return all(ord(c) < 128 for c in string)
