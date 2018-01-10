import json
from flask import Flask, request
from flask import render_template

import config

# general idea:
# show trends of word usage as a function of time (song's air-date)
# Like in google trends, but for music

from DBPopulation.insert_queries import insert_into_lyrics_table, insert_into_words_per_song_table

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

@app.route('/api/songs/likes/top/<int:amount>', methods=['GET'])
def TopSongLikes(amount):
    category = request.args.get('category')
    if category is not None:
        return TopSongLikesPerCategory(category, amount)

    statement = "SELECT songName, likeCount " \
                "FROM songs, videos " \
                "WHERE songs.songID = videos.songID " \
                "ORDER BY likeCount DESC " \
                "LIMIT %s;"

    return GetJSONResult(statement, (amount,))


def TopSongLikesPerCategory(category_name, amount):
    statement = "SELECT songName, likeCount " \
                "FROM songs, videos, categories, SongToCategory " \
                "WHERE songs.songID = videos.songID " \
                "AND SongToCategory.songID = songs.songID " \
                "AND SongToCategory.categoryID = categories.categoryID " \
                "AND categories.categoryName = %s " \
                "ORDER BY likeCount DESC " \
                "LIMIT %s;"

    return GetJSONResult(statement, (category_name, amount))


@app.route('/api/songs/dislikes/top/<int:amount>', methods=['GET'])
def TopSongDislikes(amount):
    category = request.args.get('category')
    if category is not None:
        return TopSongDislikesPerCategory(category, amount)

    statement = "SELECT songName, dislikeCount " \
                "FROM songs, videos " \
                "WHERE songs.songID = videos.songID " \
                "ORDER BY dislikeCount DESC " \
                "LIMIT %s;"

    return GetJSONResult(statement, (amount,))


def TopSongDislikesPerCategory(category_name, amount):
    statement = "SELECT songName, dislikeCount " \
                "FROM songs, videos, categories, SongToCategory " \
                "WHERE songs.songID = videos.songID " \
                "AND SongToCategory.songID = songs.songID " \
                "AND SongToCategory.categoryID = categories.categoryID " \
                "AND categories.categoryName = %s " \
                "ORDER BY dislikeCount DESC " \
                "LIMIT %s;"

    return GetJSONResult(statement, (category_name, amount))


@app.route('/api/songs/views/top/<int:amount>', methods=['GET'])
def TopSongViews(amount):
    category = request.args.get('category')
    if category is not None:
        return TopSongViewsPerCategory(category, amount)

    statement = "SELECT songName, viewCount " \
                "FROM songs, videos " \
                "WHERE songs.songID = videos.songID " \
                "ORDER BY viewCount DESC " \
                "LIMIT %s;"

    return GetJSONResult(statement, (amount,))


def TopSongViewsPerCategory(category_name, amount):
    statement = "SELECT songName, viewCount " \
                "FROM songs, videos, categories, SongToCategory " \
                "WHERE songs.songID = videos.songID " \
                "AND SongToCategory.songID = songs.songID " \
                "AND SongToCategory.categoryID = categories.categoryID " \
                "AND categories.categoryName = %s " \
                "ORDER BY viewCount DESC " \
                "LIMIT %s;"

    return GetJSONResult(statement, (category_name, amount))


@app.route('/api/songs/views/bottom/<int:amount>', methods=['GET'])
def BottomSongViews(amount):
    category = request.args.get('category')
    if category is not None:
        return BottomSongViewsPerCategory(category, amount)

    statement = "SELECT songName, viewCount " \
                "FROM songs, videos " \
                "WHERE songs.songID = videos.songID " \
                "ORDER BY viewCount ASC " \
                "LIMIT %s;"

    return GetJSONResult(statement, (amount,))


def BottomSongViewsPerCategory(category_name, amount):
    statement = "SELECT songName, viewCount " \
                "FROM songs, videos, categories, SongToCategory " \
                "WHERE songs.songID = videos.songID " \
                "AND SongToCategory.songID = songs.songID " \
                "AND SongToCategory.categoryID = categories.categoryID " \
                "AND categories.categoryName = %s " \
                "ORDER BY viewCount ASC " \
                "LIMIT %s;"

    return GetJSONResult(statement, (category_name, amount))


@app.route('/api/words/top/<int:amount>', methods=['GET'])
def TopWords(amount):
    category = request.args.get('category')
    if category is not None:
        return TopWordsPerCategory(category, amount)

    statement = "SELECT word, SUM(wordCount) AS count " \
                "FROM WordsPerSong " \
                "GROUP BY word " \
                "ORDER BY count DESC " \
                "LIMIT %s;"

    return GetJSONResult(statement, (amount,))


def TopWordsPerCategory(category_name, amount):
    statement = "SELECT word, SUM(wordCount) AS count " \
                "FROM WordsPerSong, categories, SongToCategory " \
                "WHERE WordsPerSong.songID = SongToCategory.songID " \
                "AND SongToCategory.categoryID = categories.categoryID " \
                "AND categories.categoryName = %s " \
                "GROUP BY word " \
                "ORDER BY count DESC " \
                "LIMIT %s;"

    return GetJSONResult(statement, (category_name, amount))


@app.route('/api/words/bottom/<int:amount>', methods=['GET'])
def BottomWords(amount):
    category = request.args.get('category')
    if category is not None:
        return BottomWordsPerCategory(category, amount)

    statement = "SELECT word, SUM(wordCount) AS count " \
                "FROM WordsPerSong " \
                "GROUP BY word " \
                "ORDER BY count ASC " \
                "LIMIT %s;"

    return GetJSONResult(statement, (amount,))


def BottomWordsPerCategory(category_name, amount):
    statement = "SELECT word, SUM(wordCount) AS count " \
                "FROM WordsPerSong, categories, SongToCategory " \
                "WHERE WordsPerSong.songID = SongToCategory.songID " \
                "AND categories.categoryID = SongToCategory.categoryID " \
                "AND categories.categoryName = %s " \
                "GROUP BY word " \
                "ORDER BY count ASC " \
                "LIMIT %s;"

    return GetJSONResult(statement, (category_name, amount))


# Score = numberOfWords^2 * averageUniqueness / wordCount
# where uniqueness for a word is calculated as 1/(word frequency)
# and wordCount is the total count of words (penalty for repetitions)
@app.route('/api/songs/wordscore/top/<int:amount>', methods=['GET'])
def TopSophisticatedSongs(amount):
    category = request.args.get('category')
    if category is not None:
        return TopSophisticatedSongsPerCategory(category, amount)

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
                    "GROUP BY WordsPerSong.songID " \
                ") AS a, songs " \
                "WHERE songs.songID = a.songID " \
                "ORDER BY score DESC " \
                "LIMIT %s;"

    return GetJSONResult(statement, (amount,))


def TopSophisticatedSongsPerCategory(category_name, amount):
    statement = "SELECT songName, score " \
                "FROM " \
                "(" \
                    "SELECT WordsPerSong.songID, (POW(COUNT(WordsPerSong.word),2)/SUM(wordCount))*AVG(uniqueness) AS score " \
                    "FROM " \
                    "(" \
                        "SELECT word, 1/SUM(wordCount) AS uniqueness " \
                        "FROM WordsPerSong " \
                        "GROUP BY word " \
                    ") AS wordUniqueness, WordsPerSong, categories, SongToCategory " \
                    "WHERE wordUniqueness.word = WordsPerSong.word " \
                    "AND categories.categoryName = %s " \
                    "AND SongToCategory.categoryID = categories.categoryID " \
                    "AND SongToCategory.songID = WordsPerSong.songID " \
                    "GROUP BY WordsPerSong.songID " \
                ") AS a, songs " \
                "WHERE songs.songID = a.songID " \
                "ORDER BY score DESC " \
                "LIMIT %s;"

    return GetJSONResult(statement, (category_name, amount))


@app.route('/api/songs/wordscore/bottom/<int:amount>', methods=['GET'])
def BottomSophisticatedSongs(amount):
    category = request.args.get('category')
    if category is not None:
        return BottomSophisticatedSongsPerCategory(category, amount)

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


def BottomSophisticatedSongsPerCategory(category_name, amount):
    statement = "SELECT songName, score " \
                "FROM " \
                "(" \
                    "SELECT songID, (POW(COUNT(WordsPerSong.word),2)/SUM(wordCount))*AVG(uniqueness) AS score " \
                    "FROM " \
                    "(" \
                        "SELECT word, 1/SUM(wordCount) AS uniqueness " \
                        "FROM WordsPerSong" \
                        "GROUP BY word " \
                    ") AS wordUniqueness, WordsPerSong, categories, SongToCategory " \
                    "WHERE wordUniqueness.word = WordsPerSong.word " \
                    "AND categories.categoryName = %s " \
                    "AND SongToCategory.categoryID = categories.categoryID " \
                    "AND SongToCategory.songID = WordsPerSong.songID " \
                    "GROUP BY WordsPerSong.songID " \
                ") AS a, songs " \
                "WHERE songs.songID = a.songID " \
                "ORDER BY score ASC " \
                "LIMIT %s;"

    return GetJSONResult(statement, (category_name, amount))



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


@app.route('/api/blacklist_artist')
def blacklist_artist():
    artist = request.args.get('artist')
    managerKey = request.args.get('key')
    artist_id = find_artist_id_in_table(artist)
    if artist_id is None:
        return json.dumps({"success": False})

    statement = "UPDATE Artists SET active=0 WHERE artistID=%s;"

    return GetUpdateResult(statement, (artist_id,))


@app.route('/api/lyrics/get', methods=['GET'])
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
    managerKey = request.args.get('key')
    song_id = get_song_id_by_song_name_and_artist(artist, song)
    lyrics_exist = check_if_lyrics_exist(song_id)
    if lyrics_exist:
        update_in_lyrics_table(artist, song, lyrics)
        insert_into_words_per_song_table(song_id, lyrics)
    else:
        # currently supports only lyrics in english
        insert_lyrics_into_tables(song_id, lyrics, 'en')

# TODO OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
app.route('/api/youtube/update', methods=['GET'])
def update_youtube_data():
    artist = request.args.get('artist')
    song = request.args.get('song')
    managerKey = request.args.get('key')
    return json.dumps({
            "success": True,
        })


# TODO OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
app.route('/api/songs/add', methods=['GET'])
def add_song():
    artist = request.args.get('artist')
    song = request.args.get('song')
    category = request.args.get('category')
    managerKey = request.args.get('key')
    return json.dumps({
            "success": True,
        })
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

    return GetUpdateResult(statement, (lyrics, song, artist))


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
