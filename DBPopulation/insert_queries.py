from DataAPIs.MusixMatch.lyrics_analyzer import create_words_map
from Server import config


def insert_into_categories_table(category_name):
    sql_insert = "INSERT INTO Categories VALUES (Default, %s);"
    cursor = config.cursor
    try:
        affected_count = cursor.execute(sql_insert, (category_name,))
        config.dbconnection.commit()
    except Exception as e:
        print e
        print "failed to insert value %s into Categories' " % category_name
    return cursor.lastrowid


def insert_into_artists_table(artist_name):
    sql_insert = "INSERT INTO Artists VALUES (Default, %s, Default);"
    cursor = config.cursor
    try:
        # handle non-ascii charactes
        artist_name = artist_name.encode('unicode_escape')
        affected_count = cursor.execute(sql_insert, (artist_name,))
        config.dbconnection.commit()
    except Exception as e:
        print e
        print "failed to insert value %s into Artists' " % artist_name
    return cursor.lastrowid


def insert_into_songs_table(song_name):
    sql_insert = "INSERT INTO Songs VALUES (Default, %s);"
    cursor = config.cursor
    try:
        # handle non-ascii charactes
        song_name = song_name.encode('unicode_escape')
        affected_count = cursor.execute(sql_insert, (song_name,))
        config.dbconnection.commit()
    except Exception as e:
        print e
        print "failed to insert value %s into Songs' " % song_name
    return cursor.lastrowid


def insert_into_song_to_artist_table(song_id, artist_id):
    sql_insert = "INSERT INTO SongToArtist VALUES (%s, %s);"
    cursor = config.cursor
    try:
        cursor.execute(sql_insert, (song_id, artist_id))
        config.dbconnection.commit()
    except Exception as e:
        print e
        print "failed to insert song %s and artist %s into SongToArtist' " % (song_id, artist_id)


def insert_into_artist_to_category_table(artist_id, category_id):
    sql_insert = "INSERT INTO ArtistToCategory VALUES (%s, %s);"
    cursor = config.cursor
    try:
        cursor.execute(sql_insert, (artist_id, category_id))
        config.dbconnection.commit()
    except Exception as e:
        print e
        print "failed to insert artist %s and category %s into ArtistToCategory' " % (artist_id, category_id)


def insert_into_song_to_category_table(song_id, category_id):
    sql_insert = "INSERT INTO SongToCategory VALUES (%s, %s);"
    cursor = config.cursor
    try:
        cursor.execute(sql_insert, (song_id, category_id))
        config.dbconnection.commit()
    except Exception as e:
        print e
        print "failed to insert song %s and category %s into SongToCategory' " % (song_id, category_id)


def insert_into_lyrics_table(song_id, lyrics, language):
        sql_insert = "INSERT INTO Lyrics VALUES (%s, %s, %s);"
        lyrics = lyrics.encode('unicode_escape')
        cursor = config.cursor
        try:
            cursor.execute(sql_insert, (song_id, lyrics, language))
            config.dbconnection.commit()
        except Exception as e:
            print e
            print "failed to insert lyrics for song %s' " % song_id


def insert_into_words_per_song_table(song_id, lyrics):
    words_count = create_words_map(lyrics)
    sql_insert = "INSERT INTO WordsPerSong VALUES (%s, %s, %s);"
    cursor = config.cursor
    try:
        for word, cnt in words_count.iteritems():
            word = word.encode('unicode_escape')[:20]
            cursor.execute(sql_insert, (song_id, word, cnt))
        config.dbconnection.commit()
    except Exception as e:
        print e
        print "failed to insert words for song %s' " % song_id