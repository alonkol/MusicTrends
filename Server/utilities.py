import hashlib
import json

from flask import request

from DBPopulation.insert_queries import *
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
JSON_DEBUG = json.dumps({"debug": True})

DONT_CACHE_PATHS = ['/api/lyrics/search', '/api/blacklist_artist', '/api/lyrics/update', '/api/youtube/update',
                    '/api/songs/add', '/api/lyrics/get',
                    '/debug/show_cache', '/debug/clear_cache', '/debug/clear_cache_all', '/debug/restart_cache',
                    '/debug/stop_cache']
# This will be used as a cache for our app, refreshed on every call, and invalidated on update calls
cache = {}
WORKING_CACHE = [True]


def check_manager_key(manager_key):
    if IGNORE_KEY:
        return True
    if manager_key is None:
        return False
    hash_object = hashlib.sha256(manager_key)
    hex_dig = hash_object.hexdigest()
    return hex_dig == HASHED_MANAGER_KEY


def get_result_for_queries(amount, query, query_per_category):
    amount = max(min(amount, 20), 1)
    category = request.args.get('category')
    if category is not None and isinstance(category, (int, long)):
        return get_json_result(query_per_category, (category, amount), rename_result_columns=True)

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
        queries.UPDATE_VIDEOS_DATA, (s['viewCount'], s['likeCount'], s['dislikeCount'], s["commentCount"], video_id))


def check_if_lyrics_exist(song_id):
    return json.loads(get_json_result(queries.FIND_LYRICS, (song_id, )))['amount'] != 0


def delete_all_words_for_song_id_in_words_per_song_table(song_id):
    return get_update_result(queries.REMOVE_SONG_FROM_WORDS_PER_SONG, (song_id,))


def update_in_lyrics_table(song_id, lyrics):
    return get_update_result(queries.UPDATE_LYRICS, (lyrics, song_id))


def update_in_lyrics_my_isam_table(song_id, lyrics):
    return get_update_result(queries.UPDATE_LYRICS_MY_ISAM, (lyrics, song_id))


def update_lyrics_in_db(song_id, lyrics):
    result = update_in_lyrics_table(song_id, lyrics)
    if result is JSON_FAIL_NOTICE:
        return JSON_FAIL_NOTICE
    result = update_in_lyrics_my_isam_table(song_id, lyrics)
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


def remove_all_occurrences_of_video_id_in_db(video_id):
    try:
        config.cursor.execute(queries.REMOVE_VIDEO_FROM_COMMENT_WORDS, (video_id,))
        config.dbconnection.commit()
        config.cursor.execute(queries.REMOVE_VIDEO_FROM_COMMENTS, (video_id,))
        config.dbconnection.commit()
        config.cursor.execute(queries.REMOVE_VIDEO_FROM_VIDEOS, (video_id,))
        config.dbconnection.commit()
    except Exception:
        config.dbconnection.rollback()
        raise


def remove_all_occurrences_of_song_id_in_db(song_id):
    try:
        config.cursor.execute(queries.REMOVE_SONG_FROM_SONGS_TO_CATEGORY, (song_id,))
        config.dbconnection.commit()
        config.cursor.execute(queries.REMOVE_SONG_FROM_SONGS_TO_ARTIST, (song_id,))
        config.dbconnection.commit()
        config.cursor.execute(queries.REMOVE_SONG_FROM_WORDS_PER_SONG, (song_id,))
        config.dbconnection.commit()
        config.cursor.execute(queries.REMOVE_SONG_FROM_LYRICS, (song_id,))
        config.dbconnection.commit()
        config.cursor.execute(queries.REMOVE_SONG_FROM_LYRICS_MyISAM, (song_id,))
        config.dbconnection.commit()
        config.cursor.execute(queries.REMOVE_SONG_FROM_SONGS, (song_id,))
        config.dbconnection.commit()
    except Exception:
        config.dbconnection.rollback()
        raise


def remove_all_occurrences_of_artist_id_in_db(artist_id):
    try:
        config.cursor.execute(queries.REMOVE_ARTIST_FROM_ARTIST_TO_CATEGORY, (artist_id,))
        config.dbconnection.commit()
        config.cursor.execute(queries.REMOVE_ARTIST_FROM_ARTISTS, (artist_id,))
        config.dbconnection.commit()
    except Exception:
        config.dbconnection.rollback()
        raise


def find_songs_and_videos_by_artist_id(artist_id):
    songs = json.loads(get_json_result(queries.SONGS_FOR_ARTISTS, (artist_id,)))['results']
    songs = [song['songID'] for song in songs]
    if len(songs) == 0:
        return [], []
    return songs, json.loads(get_json_result(queries.VIDEOS_FOR_SONGS % ', '.join(songs)))['results']


def find_categories_id_by_artist_id(artist_id):
    res = json.loads(get_json_result(queries.FIND_CATEGORIES_FOR_ARTIST, (artist_id,)))
    return [result['categoryID'] for result in res['results']]


def find_categories_id_by_song_id(song_id):
    res = json.loads(get_json_result(queries.FIND_CATEGORIES_FOR_SONG, (song_id,)))
    return [result['categoryID'] for result in res['results']]


def invalidate_apis_from_cache_after_blacklist_artist(artist_id):
    apis_to_invalidate = \
        ['/api/artists', '/api/songs_for_artist/{}'.format(artist_id),
         '/api/songs/likes/top/20', '/api/songs/dislikes/top/20', '/api/songs/views/top/20',
         '/api/songs/views/bottom/20',
         '/api/words/top/20',
         '/api/words/bottom/20',
         '/api/songs/wordscore/top/20',
         '/api/songs/wordscore/bottom/20',
         '/api/songs/discussionscore/top/20',
         '/api/groupies/top/20',
         '/api/artists/head_eaters/top/20',
         '/api/artists/head_eaters/top/20',
         '/api/songs/viral_songs/top/20',
         '/api/songs/days_with_most_comments/top/20',
         '/api/artists/controversial/top/20']

    categories = find_categories_id_by_artist_id(artist_id)
    apis_to_invalidate.extend(['/api/artists_for_category/{}'.format(category_id) for category_id in categories])
    invalidate_cache(apis_to_invalidate, categories=categories)


def invalidate_apis_from_cache_after_update_lyrics(song_id):
    apis_to_invalidate = \
        [
         '/api/words/top/20',
         '/api/words/bottom/20',
         '/api/songs/wordscore/top/20',
         '/api/songs/wordscore/bottom/20',
         '/api/artists/head_eaters/top/20',
         '/api/artists/head_eaters/top/20']
    categories = find_categories_id_by_song_id(song_id)
    invalidate_cache(apis_to_invalidate, categories=categories)


def invalidate_apis_from_cache_after_update_youtube_data(song_id):
    apis_to_invalidate = \
        [
         '/api/songs/likes/top/20', '/api/songs/dislikes/top/20',
         '/api/songs/views/top/20',
         '/api/songs/views/bottom/20',
         '/api/songs/discussionscore/top/20',
         '/api/groupies/top/20',
         '/api/songs/viral_songs/top/20',
         '/api/songs/days_with_most_comments/top/20',
         '/api/artists/controversial/top/20']

    categories = find_categories_id_by_song_id(song_id)
    invalidate_cache(apis_to_invalidate, categories=categories)


def invalidate_apis_from_cache_after_add_song(category_id, artist_id):
    apis_to_invalidate = \
        ['/api/songs_for_artist/{}'.format(artist_id),
         '/api/songs/likes/top/20', '/api/songs/dislikes/top/20',
         '/api/songs/views/top/20',
         '/api/songs/views/bottom/20',
         '/api/words/top/20',
         '/api/words/bottom/20',
         '/api/songs/wordscore/top/20',
         '/api/songs/wordscore/bottom/20',
         '/api/songs/discussionscore/top/20',
         '/api/groupies/top/20',
         '/api/artists/head_eaters/top/20',
         '/api/artists/head_eaters/top/20',
         '/api/songs/viral_songs/top/20',
         '/api/songs/days_with_most_comments/top/20',
         '/api/artists/controversial/top/20']

    invalidate_cache(apis_to_invalidate, categories=[category_id])


def invalidate_cache(paths, categories=None):
    for path in paths:
        print(path)
        if cache.get(path):
            del cache[path]
        if categories:
            for category in categories:
                path_with_category = '{}?category={}'.format(path, category)
                print(path_with_category)
                if cache.get(path_with_category):
                    del cache[path_with_category]


def build_cache_path(request):
    return '{}?{}'.format(request.path, request.query_string) if request.query_string else str(request.path)


def change_cache_status(status):
    WORKING_CACHE[0] = status
