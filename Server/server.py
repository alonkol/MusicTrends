import json
from flask import Flask, request, send_from_directory
from flask import render_template

import config
import queries

# general idea:
# show trends of word usage as a function of time (song's air-date)
# Like in google trends, but for music

from DBPopulation.insert_queries import insert_into_lyrics_table, insert_into_words_per_song_table, \
    insert_into_songs_table, insert_into_song_to_artist_table, insert_into_song_to_category_table
from DataAPIs.Youtube.DataEnrichment import get_statistics_for_video, populate_video

app = Flask(__name__, static_folder='frontend-build', static_url_path='')
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

@app.route('/api')
def api_welcome():
    return render_template('api.html')


@app.route('/api/categories')
def categories():
    return get_json_result(queries.CATEGORIES)


@app.route('/api/artists')
def artists():
    return get_json_result(queries.ARTISTS)


@app.route('/api/songs_for_artist/<artist_id>')
def songs_for_artist(artist_id):
    return get_json_result(queries.SONGS_FOR_ARTISTS, (artist_id,))


@app.route('/api/artists_for_category/<category_id>')
def artists_for_category(category_id):
    return get_json_result(queries.ARTISTS_FOR_CATEGORIES, (category_id,))


@app.route('/api/songs/likes/top/<int:amount>', methods=['GET'])
def top_song_likes(amount):
    return get_result_for_queries(amount, queries.TOP_SONG_LIKES, queries.TOP_SONG_LIKES_PER_CATEGORY)


@app.route('/api/songs/dislikes/top/<int:amount>', methods=['GET'])
def top_song_dislikes(amount):
    return get_result_for_queries(amount, queries.TOP_SONG_DISLIKES, queries.TOP_SONG_DISLIKES_PER_CATEGORY)


@app.route('/api/songs/views/top/<int:amount>', methods=['GET'])
def top_song_views(amount):
    return get_result_for_queries(amount, queries.TOP_SONG_VIEWS, queries.TOP_SONG_VIEWS_PER_CATEGORY)


@app.route('/api/songs/views/bottom/<int:amount>', methods=['GET'])
def bottom_song_views(amount):
    return get_result_for_queries(amount, queries.BOTTOM_SONG_VIEWS, queries.BOTTOM_SONG_VIEWS_PER_CATEGORY)


@app.route('/api/words/top/<int:amount>', methods=['GET'])
def top_words(amount):
    return get_result_for_queries(amount, queries.TOP_WORDS, queries.TOP_WORDS_PER_CATEGORY)


@app.route('/api/words/bottom/<int:amount>', methods=['GET'])
def bottom_words(amount):
    return get_result_for_queries(amount, queries.BOTTOM_WORDS, queries.BOTTOM_WORDS_PER_CATEGORY)


# Score = numberOfWords^2 * averageUniqueness / wordCount
# where uniqueness for a word is calculated as 1/(word frequency)
# and wordCount is the total count of words (penalty for repetitions)
@app.route('/api/songs/wordscore/top/<int:amount>', methods=['GET'])
def top_sophisticated_songs(amount):
    return get_result_for_queries(amount, queries.TOP_SOPHISTICATED, queries.TOP_SOPHISTICATED_PER_CATEGORY)


@app.route('/api/songs/wordscore/bottom/<int:amount>', methods=['GET'])
def bottom_sophisticated_songs(amount):
    return get_result_for_queries(amount, queries.BOTTOM_SOPHISTICATED, queries.BOTTOM_SOPHISTICATED_PER_CATEGORY)


@app.route('/api/songs/discussionscore/top/<int:amount>', methods=['GET'])
def top_sophisticated_song_discussions(amount):
    return get_result_for_queries(amount, queries.TOP_SOPHISTICATED_SONG_DISCUSSIONS, queries.TOP_SOPHISTICATED_SONG_DISCUSSIONS_PER_CATEGORY)


@app.route('/api/groupies/top/<int:amount>', methods=['GET'])
def top_groupies(amount):
    return get_result_for_queries(amount, queries.TOP_GROUPIES, queries.TOP_GROUPIES_PER_CATEGORY)


@app.route('/api/artists/head_eaters/top/<int:amount>', methods=['GET'])
def top_head_eater_artists(amount):
    return get_result_for_queries(amount, queries.TOP_HEAD_EATERS, queries.TOP_HEAD_EATERS_PER_CATEGORY)


@app.route('/api/artists/same_text_couples/top/<int:amount>', methods=['GET'])
def top_couples_with_same_text_style(amount):
    return get_result_for_queries(amount, queries.TOP_ARTIST_TEXT_COUPLES, queries.TOP_ARTIST_TEXT_COUPLES_PER_CATEGORY)


@app.route('/api/songs/days_with_most_comments/top/<int:amount>', methods=['GET'])
def days_with_most_comments(amount):
    return get_result_for_queries(amount, queries.TOP_DAYS_COMMENTS, queries.TOP_DAYS_COMMENTS_PER_CATEGORY)


@app.route('/api/artists/controversial/top/<int:amount>', methods=['GET'])
def top_controversial_artists(amount):
    return get_result_for_queries(amount, queries.TOP_CONTROVERSIAL_ARTISTS, queries.TOP_CONTROVERSIAL_ARTISTS_PER_CATEGORY)



####################################
# --------- Admin Page ----------- #
####################################

@app.route('/api/blacklist_artist')
def blacklist_artist():
    artist_id = request.args.get('artist')
    managerKey = request.args.get('key')
    if not IGNORE_KEY and hash(managerKey) != HASHED_MANAGER_KEY:
        return UNAUTHORIZED_ACTION_NOICE

    return get_update_result(queries.BLACKLIST_ARTIST, (artist_id,))


@app.route('/api/lyrics/get', methods=['GET'])
def get_lyrics():
    song_id = request.args.get('song')
    return get_json_result(queries.LYRICS, (song_id,))


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
    result = insert_lyrics_into_tables(song_id, lyrics)
    if result:
        return JSON_SUCCESS_NOTICE
    return JSON_FAIL_NOTICE


@app.route('/api/youtube/update', methods=['GET'])
def update_youtube_data():
    song_id = request.args.get('song')
    managerKey = request.args.get('key')
    if not IGNORE_KEY and hash(managerKey) != HASHED_MANAGER_KEY:
        return UNAUTHORIZED_ACTION_NOICE
    video_id = find_video_id_based_on_song_id(song_id)
    if video_id is None:
        return JSON_FAIL_NOTICE
    return update_stats_for_video(video_id)


def add_song_to_db(category_id, artist_id, song_name):
    song_id = insert_into_songs_table(song_name)
    if song_id is None:
        return
    insert_into_song_to_artist_table(song_id, artist_id)
    insert_into_song_to_category_table(song_id, category_id)
    return song_id


def find_lyrics_for_song(artist_name, song_name):
    return None


def insert_song_youtube_data(song_id, artist_name, song_name):
    return populate_video(song_id, artist_name, song_name)


@app.route('/api/songs/add', methods=['GET'])
def add_song():
    artist_id = request.args.get('artist')
    song_name = request.args.get('song')
    category_id = request.args.get('category')
    managerKey = request.args.get('key')
    if not IGNORE_KEY and hash(managerKey) != HASHED_MANAGER_KEY:
        return UNAUTHORIZED_ACTION_NOICE

    artist_name = find_artist_name_by_id_in_table(artist_id)
    print(artist_name)
    song_id = add_song_to_db(category_id, artist_id, song_name)
    if song_id is None:
        return JSON_FAIL_NOTICE

    lyrics = find_lyrics_for_song(artist_name, song_name)
    if lyrics:
        result = insert_lyrics_into_tables(song_id, lyrics)
    result = insert_song_youtube_data(song_id, artist_name, song_name)

    return JSON_SUCCESS_NOTICE


# --- Auxiliary --- #
def get_result_for_queries(amount, query, query_per_category):
    category = request.args.get('category')
    if category is not None:
        return get_json_result(query_per_category, (category, amount))

    return get_json_result(query, (amount,))


def get_json_result(statement, params=None):
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
            res[config.cursor.column_names[index]] = str(cell).decode("unicode_escape")

        results.append(res)

    return json.dumps({
        "amount": len(results),
        "results": results}
    )


def get_update_result(statement, params=None):
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


def find_artist_name_by_id_in_table(artist_id):
    res = json.loads(get_json_result(queries.FIND_ARTIST_NAME, (artist_id,)))
    if res['amount'] > 0:
        return str(res['results'][0]['artistName'])
    else:
        return None


def find_song_id_by_song_name_and_artist(artist, song):
    res = json.loads(get_json_result(queries.FIND_SONG_ID, (song, artist)))
    if res['amount'] > 0:
        return int(res['results'][0]['songID'])
    else:
        return None


def find_video_id_based_on_song_id(song_id):
    res = json.loads(get_json_result(queries.FIND_VIDEO_ID_BY_SONG_ID, (song_id,)))
    if res['amount'] > 0:
        return res['results'][0]['videoID']
    else:
        return None


def update_stats_for_video(video_id):
    s = get_statistics_for_video(video_id)
    return get_update_result(
        queries.UPDATE_VIDEOS_DATA, (s['viewCount'], s['likeCount'], s['dislikeCount'],
                                     s['favoriteCount'], s['commentCount'], video_id))


def check_if_lyrics_exist(song_id):
    return json.loads(get_json_result(queries.FIND_LYRICS, (song_id, )))['amount'] != 0


def delete_all_words_for_song_id_in_words_per_song_table(song_id):
    return get_update_result(queries.DELETE_FROM_WORDS_PER_SONG, (song_id,))


def update_in_lyrics_table(song_id, lyrics):
    return get_update_result(queries.UPDATE_LYRICS, (lyrics, song_id))


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


def insert_lyrics_into_tables(song_id, lyrics):
    result = insert_into_lyrics_table(song_id, lyrics)
    if result is None:
        return
    return insert_into_words_per_song_table(song_id, lyrics)


###############################
# --------- Pages ----------- #
###############################
@app.route('/')
def homepage():
    return send_from_directory('frontend-build', 'index.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


if __name__ == '__main__':
    app.run(port=config.port, host=config.host, debug=True)
