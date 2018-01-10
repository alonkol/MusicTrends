import json
from flask import Flask, request
from flask import render_template

import config

# general idea:
# show trends of word usage as a function of time (song's air-date)
# Like in google trends, but for music
from LyricsCollection.lyrics_analyzer import create_words_map
from Population.insert_queries import insert_into_lyrics_table, insert_into_words_per_song_table

app = Flask(__name__)


###############################
# -------- REST API --------- #
###############################

# --- Routes --- #
@app.route('/api')
def ApiWelcome():
    return render_template('api.html')


@app.route('/api/categories')
def Categories():
    statement = "SELECT categoryID as id, categoryName as name " \
                "FROM categories;"

    return GetJSONResult(statement)


@app.route('/api/songs/likes/top/<int:amount>')
def TopSongLikes(amount):
    statement = "SELECT songName, likeCount " \
                "FROM songs, videos " \
                "WHERE songs.songID = videos.songID " \
                "ORDER BY likeCount DESC " \
                "LIMIT %s;"

    return GetJSONResult(statement, (amount,))


@app.route('/api/songs/dislikes/top/<int:amount>')
def TopSongDislikes(amount):
    statement = "SELECT songName, dislikeCount " \
                "FROM songs, videos " \
                "WHERE songs.songID = videos.songID " \
                "ORDER BY dislikeCount DESC " \
                "LIMIT %s;"

    return GetJSONResult(statement, (amount,))


@app.route('/api/songs/views/top/<int:amount>')
def TopSongViews(amount):
    statement = "SELECT songName, viewCount " \
                "FROM songs, videos " \
                "WHERE songs.songID = videos.songID " \
                "ORDER BY viewCount DESC " \
                "LIMIT %s;"

    return GetJSONResult(statement, (amount,))


@app.route('/api/songs/views/bottom/<int:amount>')
def BottomSongViews(amount):
    statement = "SELECT songName, viewCount " \
                "FROM songs, videos " \
                "WHERE songs.songID = videos.songID " \
                "ORDER BY viewCount ASC " \
                "LIMIT %s;"

    return GetJSONResult(statement, (amount,))


@app.route('/api/words/top/<int:amount>')
def TopWords(amount):
    statement = "SELECT word, SUM(wordCount) AS count " \
                "FROM WordsPerSong " \
                "GROUP BY word " \
                "ORDER BY count DESC " \
                "LIMIT %s;"

    return GetJSONResult(statement, (amount,))


@app.route('/api/words/bottom/<int:amount>')
def BottomWords(amount):
    statement = "SELECT word, SUM(wordCount) AS count " \
                "FROM WordsPerSong " \
                "GROUP BY word " \
                "ORDER BY count ASC " \
                "LIMIT %s;"

    return GetJSONResult(statement, (amount,))

# Score = numberOfWords^2 * averageUniqueness / wordCount
# where uniqueness for a word is calculated as 1/(word frequency)
# and wordCount is the total count of words (penalty for repetitions)
@app.route('/api/songs/wordscore/top/<int:amount>')
def TopSophisticatedSongs(amount):
    statement = "SELECT songName, score " \
                "FROM " \
                "(" \
                    "SELECT songID, (POW(COUNT(WordsPerSong.word),2)/SUM(wordCount))*AVG(uniqueness) AS score " \
                    "FROM " \
                    "(" \
                        "SELECT word, 1/SUM(wordCount) AS uniqueness " \
                        "FROM WordsPerSong " \
                        "GROUP BY word " \
                    ") AS wordUniqueness, WordsPerSong  " \
                    "WHERE wordUniqueness.word = WordsPerSong.word " \
                    "GROUP BY WordsPerSong.songID" \
                ") AS a, songs " \
                "WHERE songs.songID = a.songID " \
                "ORDER BY score DESC " \
                "LIMIT %s;"

    return GetJSONResult(statement, (amount,))


# TODO: put in VIEW
@app.route('/api/songs/wordscore/bottom/<int:amount>')
def BottomSophisticatedSongs(amount):
    statement = "SELECT songName, score " \
                "FROM " \
                "(" \
                    "SELECT songID, (POW(COUNT(WordsPerSong.word),2)/SUM(wordCount))*AVG(uniqueness) AS score " \
                    "FROM " \
                    "(" \
                        "SELECT word, 1/SUM(wordCount) AS uniqueness " \
                        "FROM WordsPerSong " \
                        "GROUP BY word " \
                    ") AS wordUniqueness, WordsPerSong  " \
                    "WHERE wordUniqueness.word = WordsPerSong.word " \
                    "GROUP BY WordsPerSong.songID" \
                ") AS a, songs " \
                "WHERE songs.songID = a.songID " \
                "ORDER BY score ASC " \
                "LIMIT %s;"

    return GetJSONResult(statement, (amount,))


@app.route('/api/songs/discussionscore/top/<int:amount>')
def TopSophisticatedSongDiscussions(amount):
    return ""


####################################
# --------- Admin Page ----------- #
####################################


@app.route('/api/artists')
def artists():
    statement = "SELECT artistName FROM Artists WHERE active=1;"

    return GetJSONResult(statement)


@app.route('/api/songs_for_artist/<artist>')
def songs_for_artist(artist):
    statement = "SELECT Songs.songName FROM Artists, SongToArtist, Songs " \
                "WHERE artistName = %s " \
                "and Artists.artistID = SongToArtist.artistID and Songs.songID = SongToArtist.songID;"

    return GetJSONResult(statement, (artist,))


@app.route('/api/blacklist_artist/<artist>')
def blacklist_artist(artist):
    artist_id = find_artist_id_in_table(artist)
    if artist_id is None:
        return json.dumps({"success": False})

    statement = "UPDATE Artists SET active=0 WHERE artistID=%s;"

    return GetUpdateResult(statement, (artist_id,))

@app.route('/api/lyrics/get/', methods=['GET'])
def get_lyrics():
    artist = request.args.get('artist')
    song = request.args.get('song')
    statement = "SELECT lyrics " \
                "FROM Lyrics, Songs, SongToArtist, Artists " \
                "WHERE " \
                "artistName = %s AND " \
                "songName = %s AND " \
                "Artists.artistID = SongToArtist.artistID  AND " \
                "Songs.songID = SongToArtist.songID AND " \
                "Lyrics.songID = Songs.songID;"
    return GetJSONResult(statement, (artist, song))


@app.route('/api/lyrics/update', methods=['GET'])
def update_lyrics():
    artist = request.args.get('artist')
    song = request.args.get('song')
    lyrics = request.args.get('lyrics')
    song_id = get_song_id_by_song_name_and_artist(artist, song)
    lyrics_exist = check_if_lyrics_exist(song_id)
    if lyrics_exist:
        update_in_lyrics_table(artist, song, lyrics)
        insert_into_words_per_song_table(song_id, lyrics)
    else:
        # currently supports only lyrics in english
        insert_lyrics_into_tables(song_id, lyrics, 'en')

# --- Auxiliary --- #

def GetJSONResult(statement, params=None):
    if params is not None:
        config.cursor.execute(statement, params)
    else:
        config.cursor.execute(statement)

    rows = config.cursor.fetchall()

    # decode results to strings
    results = []

    # row to dict
    for row in rows:
        res = {}

        for index, cell in enumerate(row):
            res[config.cursor.column_names[index]] = str(cell).decode("utf-8")

        results.append(res)

    return json.dumps({
        "amount": len(results),
        "results": results}
    )


def GetUpdateResult(statement, params=None):
    if params is not None:
        config.cursor.execute(statement, params)
    else:
        config.cursor.execute(statement)

    try:
        config.dbconnection.commit()
    except Exception:
        config.dbconnection.rollback()
        return json.dumps({
            "success": False,
        })

    return json.dumps({
        "success": True,
        }
    )


def find_artist_id_in_table(artist_name):
    statement = "SELECT artistID FROM Artists WHERE artistName = %s;"
    try:
        config.cursor.execute(statement, (artist_name,))
    except Exception:
        return
    rows = config.cursor.fetchall()
    return rows[0][0] if rows else None


def check_if_lyrics_exist(song_id):
    statement = "SELECT lyrics " \
                "FROM Lyrics " \
                "WHERE " \
                "songID = %s;"

    return json.loads(GetJSONResult(statement, (song_id, )))['amount'] != 0


def update_in_lyrics_table(artist,song,lyrics):
    statement = "UPDATE lyrics " \
                "SET lyrics = %s " \
                "WHERE " \
                "(SELECT Songs.songID FROM Songs, SongToArtist, Artists " \
                "WHERE songName = %s AND " \
                "ArtistName = %s AND " \
                "Artists.artistID = SongToArtist.artistID AND " \
                "Songs.songID = SongToArtist.songID); "

    return GetJSONResult(statement, (lyrics, song, artist))


def insert_lyrics_into_tables(song_id, lyrics, language):
    insert_into_lyrics_table(song_id, lyrics, language)
    insert_into_words_per_song_table(song_id, lyrics)


def get_song_id_by_song_name_and_artist(artist, song):
    statement = "SELECT Songs.songID " \
                "FROM Songs, SongToArtist, Artists " \
                "WHERE songName = %s AND " \
                "ArtistName = %s AND " \
                "Artists.artistID = SongToArtist.artistID AND " \
                "Songs.songID = SongToArtist.songID; "
    res = json.loads(GetJSONResult(statement, (song, artist)))
    if res['amount'] > 0:
        return int(res['results'][0]['songID'])
    else:
        return None


###############################
# --------- Pages ----------- #
###############################
@app.route('/')
def Homepage():
    return "Wabadabadubdub!"


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


if __name__ == '__main__':
    app.run(port=config.port, host=config.host, debug=True)
