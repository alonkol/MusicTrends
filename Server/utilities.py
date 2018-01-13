import hashlib
import json

from flask import request

from DBPopulation.insert_queries import insert_into_words_per_song_table, insert_into_lyrics_table, \
    insert_into_songs_table, insert_into_song_to_artist_table, insert_into_song_to_category_table
from DataAPIs.MusixMatch.lyrics_collector import get_lyrics_for_song
from DataAPIs.Youtube.DataEnrichment import get_statistics_for_video, populate_video
from Server import config, queries

HASHED_MANAGER_KEY = '4d0fb6ddc0b9a9a7d8d8e33ab46b06de97deea482ec854f0f3fe606452bf1119'
# TODO OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO REMOVE THIS BEFORE SUBMISSION
IGNORE_KEY = True
MANAGER_KEY = "Wubalubadubdub!"

JSON_FAIL_NOTICE = json.dumps({"success": False, "reason": "DB Issue"})
JSON_SUCCESS_NOTICE = json.dumps({"success": True})
UNAUTHORIZED_ACTION_NOTICE = json.dumps({"success": False, "reason": "Manager key is incorrect"})


def check_manager_key(manager_key):
    if IGNORE_KEY:
        return True
    hash_object = hashlib.sha256(manager_key)
    hex_dig = hash_object.hexdigest()
    return hex_dig == HASHED_MANAGER_KEY


def get_result_for_queries(amount, query, query_per_category):
    category = request.args.get('category')
    if category is not None:
        return get_json_result(query_per_category, (category, amount))

    return get_json_result(query, (amount,), rename_result_columns=True)


def get_json_result(statement, params=None, default_value=None, rename_result_columns=False):
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

        if rename_result_columns:
            res['value'] = str(row[0]).decode("unicode_escape")
            if len(row) == 1:
                res['count'] = None
            if len(row) == 2:
                res['count'] = str(row[1]).decode("unicode_escape")
        else:
            for index, cell in enumerate(row):
                res[config.cursor.column_names[index]] = str(cell).decode("unicode_escape")

        results.append(res)

    if len(results) == 0 and default_value:
        return default_value

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


def add_song_to_db(category_id, artist_id, song_name):
    song_id = insert_into_songs_table(song_name)
    if song_id is None:
        return
    insert_into_song_to_artist_table(song_id, artist_id)
    insert_into_song_to_category_table(song_id, category_id)
    return song_id


def find_lyrics_for_song(artist_name, song_name):
    return get_lyrics_for_song(song_name, artist_name)


def insert_song_youtube_data(song_id, artist_name, song_name):
    return populate_video(song_id, artist_name, song_name)
