from LastFmApiHandler.retreive_data_from_last_fm import get_data_from_file
from LyricsCollection.lyrics_analyzer import create_words_map
from Server import config


def find_song_id(song_title):
    sql_get = "SELECT songID from Songs WHERE songName = %s;"
    cursor = config.cursor
    cursor.execute(sql_get, (song_title,))
    rows = cursor.fetchall()
    if not rows:
        # no lyrics for this song
        return
    return rows[0][0]


def insert_into_lyrics_table(song_id, lyrics):
    sql_insert = "INSERT INTO Lyrics VALUES (%s, %s);"
    lyrics = lyrics.encode('unicode_escape')
    cursor = config.cursor
    try:
        cursor.execute(sql_insert, (song_id, lyrics))
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


def main():
    lyrics_data = get_data_from_file('../LyricsCollection/lyrics.json')
    for song_title, lyrics in lyrics_data.iteritems():
        song_id = find_song_id(song_title)
        if song_id is None:
            continue
        insert_into_lyrics_table(song_id, lyrics)
        insert_into_words_per_song_table(song_id, lyrics)

if __name__ == '__main__':
    main()