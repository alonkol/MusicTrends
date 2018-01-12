import json
from flask import Flask, request
from flask import render_template

import config
import queries

# general idea:
# show trends of word usage as a function of time (song's air-date)
# Like in google trends, but for music

from DBPopulation.insert_queries import insert_into_lyrics_table, insert_into_words_per_song_table

app = Flask(__name__)
JSON_FAIL_NOTICE = json.dumps({"success": False, "reason": "DB Issue"})
JSON_SUCCESS_NOTICE = json.dumps({"success": True})
UNAUTHORIZED_ACTION_NOICE = json.dumps({"success": False, "reason": "Manager key is incorrect"})

HASHED_MANAGER_KEY = -3964674059591715977
# TODO OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO REMOVE THIS BEFORE SUBMISSION
IGNORE_KEY = True
MANAGER_KEY = "Wubalubadubdub!"

###############################
# -------- REST API --------- #
###############################

# --- Routes --- #
@app.route('/api')
def ApiWelcome():
    return render_template('api.html')


@app.route('/api/categories')
def Categories():
    return GetJSONResult(queries.CATEGORIES)


@app.route('/api/songs/likes/top/<int:amount>', methods=['GET'])
def TopSongLikes(amount):
    category = request.args.get('category')
    if category is not None:
        return GetJSONResult(queries.TOP_SONG_LIKES_PER_CATEGORY, (category, amount))

    return GetJSONResult(queries.TOP_SONG_LIKES, (amount,))


@app.route('/api/songs/dislikes/top/<int:amount>', methods=['GET'])
def TopSongDislikes(amount):
    category = request.args.get('category')
    if category is not None:
        return GetJSONResult(queries.TOP_SONG_DISLIKES_PER_CATEGORY, (category, amount))

    return GetJSONResult(queries.TOP_SONG_DISLIKES, (amount,))


@app.route('/api/songs/views/top/<int:amount>', methods=['GET'])
def TopSongViews(amount):
    category = request.args.get('category')
    if category is not None:
        return GetJSONResult(queries.TOP_SONG_VIEWS_PER_CATEGORY, (category, amount))

    return GetJSONResult(queries.TOP_SONG_VIEWS, (amount,))


@app.route('/api/songs/views/bottom/<int:amount>', methods=['GET'])
def BottomSongViews(amount):
    category = request.args.get('category')
    if category is not None:
        return GetJSONResult(queries.BOTTOM_SONG_VIEWS_PER_CATEGORY, (category, amount))

    return GetJSONResult(queries.BOTTOM_SONG_VIEWS, (amount,))


@app.route('/api/words/top/<int:amount>', methods=['GET'])
def TopWords(amount):
    category = request.args.get('category')
    if category is not None:
        return GetJSONResult(queries.TOP_WORDS_PER_CATEGORY, (category, amount))

    return GetJSONResult(queries.TOP_WORDS, (amount,))


@app.route('/api/words/bottom/<int:amount>', methods=['GET'])
def BottomWords(amount):
    category = request.args.get('category')
    if category is not None:
        return GetJSONResult(queries.BOTTOM_WORDS_PER_CATEGORY, (category, amount))

    return GetJSONResult(queries.BOTTOM_WORDS, (amount,))


# Score = numberOfWords^2 * averageUniqueness / wordCount
# where uniqueness for a word is calculated as 1/(word frequency)
# and wordCount is the total count of words (penalty for repetitions)
@app.route('/api/songs/wordscore/top/<int:amount>', methods=['GET'])
def TopSophisticatedSongs(amount):
    category = request.args.get('category')
    if category is not None:
        return GetJSONResult(queries.TOP_SOPHISTICATED_PER_CATEGORY, (category, amount))

    return GetJSONResult(queries.TOP_SOPHISTICATED, (amount,))


@app.route('/api/songs/wordscore/bottom/<int:amount>', methods=['GET'])
def BottomSophisticatedSongs(amount):
    category = request.args.get('category')
    if category is not None:
        return GetJSONResult(queries.BOTTOM_SOPHISTICATED_PER_CATEGORY, (category, amount))

    return GetJSONResult(queries.BOTTOM_SOPHISTICATED, (amount,))


@app.route('/api/songs/discussionscore/top/<int:amount>')
def TopSophisticatedSongDiscussions(amount):
    return ""


####################################
# --------- Admin Page ----------- #
####################################


@app.route('/api/artists')
def artists():
    statement = queries.ARTISTS

    return GetJSONResult(statement)


@app.route('/api/songs_for_artist/<artist_id>')
def songs_for_artist(artist_id):
    statement = queries.SONGS_FOR_ARTISTS

    return GetJSONResult(statement, (artist_id,))


@app.route('/api/blacklist_artist')
def blacklist_artist():
    artist_id = request.args.get('artist')
    managerKey = request.args.get('key')
    if not IGNORE_KEY and hash(managerKey) != HASHED_MANAGER_KEY:
        return UNAUTHORIZED_ACTION_NOICE
    statement = queries.BLACKLIST_ARTIST

    return GetUpdateResult(statement, (artist_id,))


@app.route('/api/lyrics/get', methods=['GET'])
def get_lyrics():
    song_id = request.args.get('song')
    statement = queries.LYRICS
    return GetJSONResult(statement, (song_id,))


def delete_all_words_for_song_id_in_words_per_song_table(song_id):
    statement = queries.DELETE_FROM_WORDS_PER_SONG

    return GetUpdateResult(statement, (song_id,))


@app.route('/api/lyrics/update', methods=['GET'])
def update_lyrics():
    song_id = request.args.get('song')
    lyrics = request.args.get('lyrics')
    managerKey = request.args.get('key')
    if not IGNORE_KEY and hash(managerKey) != HASHED_MANAGER_KEY:
        return UNAUTHORIZED_ACTION_NOICE
    lyrics_exist = check_if_lyrics_exist(song_id)
    if lyrics_exist:
        return update_lyrics_in_db(song_id, lyrics)

    # currently supports only lyrics in english
    result = insert_lyrics_into_tables(song_id, lyrics, 'en')
    if result:
        return json.dumps({"success": True})
    return json.dumps({"success": True})

# TODO OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
@app.route('/api/youtube/update', methods=['GET'])
def update_youtube_data():
    song_id = request.args.get('song')
    managerKey = request.args.get('key')
    if not IGNORE_KEY and hash(managerKey) != HASHED_MANAGER_KEY:
        return UNAUTHORIZED_ACTION_NOICE
    return json.dumps({
            "success": True,
        })


# TODO OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
@app.route('/api/songs/add', methods=['GET'])
def add_song():
    artist = request.args.get('artist')
    song = request.args.get('song')
    category = request.args.get('category')
    managerKey = request.args.get('key')
    if not IGNORE_KEY and hash(managerKey) != HASHED_MANAGER_KEY:
        return UNAUTHORIZED_ACTION_NOICE
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
        return JSON_FAIL_NOTICE

    return JSON_SUCCESS_NOTICE



def find_artist_id_in_table(artist_name):
    statement = queries.FIND_ARTIST_ID
    try:
        config.cursor.execute(statement, (artist_name,))
    except Exception:
        return
    rows = config.cursor.fetchall()
    return rows[0][0] if rows else None


def find_song_id_by_song_name_and_artist(artist, song):
    statement = queries.FIND_SONG_ID
    res = json.loads(GetJSONResult(statement, (song, artist)))
    if res['amount'] > 0:
        return int(res['results'][0]['songID'])
    else:
        return None


def check_if_lyrics_exist(song_id):
    statement = queries.FIND_LYRICS

    return json.loads(GetJSONResult(statement, (song_id, )))['amount'] != 0


def update_in_lyrics_table(song_id, lyrics):
    statement = queries.UPDATE_LYRICS

    return GetUpdateResult(statement, (lyrics, song_id))


def update_lyrics_in_db(song_id, lyrics):
    result = update_in_lyrics_table(song_id, lyrics)
    if result is JSON_FAIL_NOTICE:
        return JSON_FAIL_NOTICE
    result = delete_all_words_for_song_id_in_words_per_song_table(song_id)
    if result is JSON_FAIL_NOTICE:
        return JSON_FAIL_NOTICE
    result = insert_into_words_per_song_table(song_id, lyrics)
    if result is None:
        return JSON_FAIL_NOTICE
    return JSON_SUCCESS_NOTICE


def insert_lyrics_into_tables(song_id, lyrics, language):
    result = insert_into_lyrics_table(song_id, lyrics, language)
    if result is None:
        return
    return insert_into_words_per_song_table(song_id, lyrics)


###############################
# --------- Pages ----------- #
###############################
@app.route('/')
def Homepage():
    return "Wubalubadubdub!"


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


if __name__ == '__main__':
    app.run(port=config.port, host=config.host, debug=True)
