import os
from flask import Flask, request, send_from_directory, render_template
from gevent.wsgi import WSGIServer

# fix in order to work on the tomcat server
import sys
sys.path.insert(0, "../")

from Server.utilities import *


app = Flask(__name__, static_folder='frontend-build', static_url_path='')


# Cache management
@app.before_request
def return_cached():
    if not WORKING_CACHE[0]:
        return
    response = cache.get(build_cache_path(request))
    if response:
        return response


@app.after_request
def cache_response(response):
    if not WORKING_CACHE[0] or str(request.path) in DONT_CACHE_PATHS:
        return response
    cache_path = build_cache_path(request)
    if cache.get(cache_path) is None and response.status_code == 200:
        cache[cache_path] = response
    return response


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


@app.route('/api/songs_for_artist/<int:artist_id>')
def songs_for_artist(artist_id):
    return get_json_result(queries.SONGS_FOR_ARTISTS, (artist_id,))


@app.route('/api/artists_for_category/<int:category_id>')
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


@app.route('/api/songs/wordscore/top/<int:amount>', methods=['GET'])
def top_sophisticated_songs(amount):
    return get_result_for_queries(amount, queries.TOP_SOPHISTICATED, queries.TOP_SOPHISTICATED_PER_CATEGORY)


@app.route('/api/songs/wordscore/bottom/<int:amount>', methods=['GET'])
def bottom_sophisticated_songs(amount):
    return get_result_for_queries(amount, queries.BOTTOM_SOPHISTICATED, queries.BOTTOM_SOPHISTICATED_PER_CATEGORY)


@app.route('/api/songs/discussionscore/top/<int:amount>', methods=['GET'])
def top_sophisticated_song_discussions(amount):
    return get_result_for_queries(amount, queries.TOP_SOPHISTICATED_SONG_DISCUSSIONS,
                                  queries.TOP_SOPHISTICATED_SONG_DISCUSSIONS_PER_CATEGORY)


@app.route('/api/groupies/top/<int:amount>', methods=['GET'])
def top_groupies(amount):
    return get_result_for_queries(amount, queries.TOP_GROUPIES, queries.TOP_GROUPIES_PER_CATEGORY)


@app.route('/api/artists/head_eaters/top/<int:amount>', methods=['GET'])
def top_head_eater_artists(amount):
    return get_result_for_queries(amount, queries.TOP_HEAD_EATERS, queries.TOP_HEAD_EATERS_PER_CATEGORY)


@app.route('/api/songs/viral_songs/top/<int:amount>', methods=['GET'])
def top_viral_songs(amount):
    return get_result_for_queries(amount, queries.TOP_VIRAL_SONGS, queries.TOP_VIRAL_SONGS_PER_CATEGORY)


@app.route('/api/songs/days_with_most_comments/top/<int:amount>', methods=['GET'])
def days_with_most_comments(amount):
    return get_result_for_queries(amount, queries.TOP_DAYS_COMMENTS, queries.TOP_DAYS_COMMENTS_PER_CATEGORY)


@app.route('/api/artists/controversial/top/<int:amount>', methods=['GET'])
def top_controversial_artists(amount):
    return get_result_for_queries(amount, queries.TOP_CONTROVERSIAL_ARTISTS,
                                  queries.TOP_CONTROVERSIAL_ARTISTS_PER_CATEGORY)


####################################
# --------- Admin Pages ----------- #
####################################
@app.route('/api/blacklist_artist', methods=['GET', 'POST', 'PUT'])
def blacklist_artist():
    artist_id = request.args.get('artist')
    if artist_id is None:
        return JSON_FAIL_NOTICE
    manager_key = request.args.get('key')
    if not check_manager_key(manager_key):
        return UNAUTHORIZED_ACTION_NOTICE
    songs, videos = find_songs_and_videos_by_artist_id(artist_id)
    try:
        for video in videos:
            remove_all_occurrences_of_video_id_in_db(video['videoID'])
        for song_id in songs:
            remove_all_occurrences_of_song_id_in_db(song_id)
        remove_all_occurrences_of_artist_id_in_db(artist_id)
    except Exception:
        return JSON_FAIL_NOTICE

    invalidate_apis_from_cache_after_blacklist_artist(artist_id)
    return JSON_SUCCESS_NOTICE


@app.route('/api/lyrics/get', methods=['GET'])
def get_lyrics():
    song_id = request.args.get('song')
    default_answer = json.dumps({"amount": 1, "results": [{"lyrics": "Lyrics not found."}]})
    if song_id is None:
        return default_answer
    lyrics_result = get_json_result(
        queries.FIND_LYRICS, (song_id,),
        default_value=default_answer)
    return lyrics_result


@app.route('/api/lyrics/update', methods=['GET', 'POST', 'PUT'])
def update_lyrics():
    song_id = request.args.get('song')
    lyrics = request.args.get('lyrics')
    if song_id is None or lyrics is None:
        return JSON_FAIL_NOTICE
    manager_key = request.args.get('key')
    if not check_manager_key(manager_key):
        return UNAUTHORIZED_ACTION_NOTICE
    lyrics_exist = check_if_lyrics_exist(song_id)
    if lyrics_exist:
        result = update_lyrics_in_db(song_id, lyrics)
        if result is JSON_SUCCESS_NOTICE:
            invalidate_apis_from_cache_after_update_lyrics(song_id)
        return result

    # currently supports only lyrics in english
    result = insert_lyrics_into_tables(song_id, lyrics)
    if result is not None:
        invalidate_apis_from_cache_after_update_lyrics(song_id)
        return JSON_SUCCESS_NOTICE
    return JSON_FAIL_NOTICE


@app.route('/api/youtube/update', methods=['GET', 'POST', 'PUT'])
def update_youtube_data():
    song_id = request.args.get('song')
    if song_id is None:
        return JSON_FAIL_NOTICE
    manager_key = request.args.get('key')
    if not check_manager_key(manager_key):
        return UNAUTHORIZED_ACTION_NOTICE
    video_id = find_video_id_based_on_song_id(song_id)
    if video_id is None:
        return JSON_FAIL_NOTICE
    result = update_stats_for_video(video_id)
    if result is JSON_SUCCESS_NOTICE:
        invalidate_apis_from_cache_after_update_youtube_data(song_id)
    return result


@app.route('/api/songs/add', methods=['GET', 'POST', 'PUT'])
def add_song():
    artist_id = request.args.get('artist')
    song_name = request.args.get('song')
    category_id = request.args.get('category')
    if artist_id is None or song_name is None or category_id is None:
        return JSON_FAIL_NOTICE
    manager_key = request.args.get('key')
    if not check_manager_key(manager_key):
        return UNAUTHORIZED_ACTION_NOTICE

    artist_name = find_artist_name_by_id_in_table(artist_id)
    song_id = add_song_to_db(category_id, artist_id, song_name)
    if song_id is None:
        return JSON_FAIL_NOTICE

    # We try and add youtube and lyrics data,
    # If any of them fails, we continue without this data
    lyrics = find_lyrics_for_song(artist_name, song_name)
    if lyrics:
        insert_lyrics_into_tables(song_id, lyrics)
    insert_song_youtube_data(song_id, artist_name, song_name)
    invalidate_apis_from_cache_after_add_song(category_id, artist_id)
    return JSON_SUCCESS_NOTICE


####################################
# ----- FULL TEXT SEARCH --------- #
####################################

@app.route('/api/lyrics/search', methods=['GET'])
def find_best_matching_song_to_given_text():
    text = request.args.get('text')
    return get_json_result(queries.FIND_FIVE_MATCHING_SONG_NAMES, (text, ))


######################################################
# --------- DEBUGGING - CACHE MANAGEMENT ----------- #
######################################################
@app.route('/debug/show_cache')
def show_cache():
    manager_key = request.args.get('key')
    if not check_manager_key(manager_key):
        return UNAUTHORIZED_ACTION_NOTICE
    print('Cache content:')
    print('\n'.join(cache.iterkeys()))
    return JSON_DEBUG


@app.route('/debug/clear_cache')
def clear_from_cache():
    manager_key = request.args.get('key')
    if not check_manager_key(manager_key):
        return UNAUTHORIZED_ACTION_NOTICE
    url = request.args.get('url')
    if url in cache:
        del cache[url]
        print('{} removed from cached.'.format(url))
    return JSON_DEBUG


@app.route('/debug/clear_cache_all')
def clear_all_cache():
    manager_key = request.args.get('key')
    if not check_manager_key(manager_key):
        return UNAUTHORIZED_ACTION_NOTICE
    cache.clear()
    print('Cache is cleared.')
    return JSON_DEBUG


@app.route('/debug/restart_cache')
def restart_cache():
    manager_key = request.args.get('key')
    if not check_manager_key(manager_key):
        return UNAUTHORIZED_ACTION_NOTICE
    change_cache_status(True)
    print('Cache restarted, consider using clear_cache.')
    return JSON_DEBUG


@app.route('/debug/stop_cache')
def stop_cache():
    manager_key = request.args.get('key')
    if not check_manager_key(manager_key):
        return UNAUTHORIZED_ACTION_NOTICE
    change_cache_status(False)
    print('Cache stopped.')
    return JSON_DEBUG


###############################
# --------- Pages ----------- #
###############################
@app.route('/')
def homepage():
    return send_from_directory('frontend-build', 'index.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


###############################
# --- React Static Fies ----- #
###############################


@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    http_server = WSGIServer(('', config.port), app)
    http_server.serve_forever()
