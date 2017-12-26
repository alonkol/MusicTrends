

import re

import MySQLdb
import requests
import json
from Server import config

API_KEY = 'secret'
BASE_URL = 'http://ws.audioscrobbler.com/2.0/?api_key={}&method&format=json'.format(API_KEY)


def handle_all_categories():
    d = get_data_from_file('categories.json')
    for k in d:
        insert_categories_to_db(k['name'])


def get_all_categories_from_api():
    url = BASE_URL + '&method=tag.getTopTags'
    response = requests.get(url)
    d = json.loads(response.text)['toptags']['tag']
    with open('categories.json', 'w') as outf:
        json.dump(d, outf)


def get_data_from_file(filename):
    return json.load(open(filename))


def insert_categories_to_db(value):
    sql_insert = "INSERT INTO Categories VALUES (Default, %s);"
    cursor = config.cursor
    try:
        affected_count = cursor.execute(sql_insert, (value,))
        config.dbconnection.commit()
    except MySQLdb.IntegrityError:
        print "failed to insert values %s to Categories' " % value


def insert_artists_to_db(value):
    sql_insert = "INSERT INTO Artists VALUES (Default, %s);"
    cursor = config.cursor
    try:
        affected_count = cursor.execute(sql_insert, (value,))
        config.dbconnection.commit()
    except MySQLdb.IntegrityError:
        print "failed to insert values %s to Artists' " % value


def handle_all_artists():
    artists_per_category = get_data_from_file('artists.json')
    artists = set()
    for cat in artists_per_category.values():
        for artist in cat:
            # make sure no duplicates
            if artist not in artists:
                print(artist)
                # handle non-ascii characters
                artist = artist.encode('unicode_escape')
                print(len(artist))
                artists.add(artist)
                insert_artists_to_db(artist)


def get_artists_per_category_from_api(category):
    cat_artists = []
    url = BASE_URL + '&method=tag.gettopartists&tag=' + category
    response = requests.get(url)
    d = json.loads(response.text)['topartists']['artist']
    for k in d:
        cat_artists.append(k['name'])
    return cat_artists

def get_all_artists_from_api():
    res = {}
    categories = get_data_from_file('categories.json')
    for category in categories:
        res[category['name']] = get_artists_per_category_from_api(category['name'])
    with open('artists.json', 'w') as outf:
        json.dump(res,outf)


def retrieve_songs_per_artist(request_song_base_url, artist):
    art_songs = []
    url = request_song_base_url + '&artist=' + artist
    response = requests.get(url)
    d = json.loads(response.text)['toptracks']['track']
    for k in d:
        art_songs.append(k['name'])
    return art_songs


def get_songs_per_artist_from_api(artist):
    res = []
    try:
        url = BASE_URL + '&method=artist.gettoptracks&artist=' + artist
        response = requests.get(url)
        if 'toptracks' in json.loads(response.text):
            d = json.loads(response.text)['toptracks']['track']
            for k in d:
                res.append(k['name'])
            return res
        else:
            print("no toptracks for artist % s" % artist)
            print(" response = %s " % response )
    except Exception as e:
        print('Problem with artist %s' % artist)
        print(e)
        return res


def get_all_songs_from_api():
    res = {}
    artists_per_category = get_data_from_file('artists.json')
    for cat in artists_per_category.values():
        for artist in cat:
            try:
                res[artist] = get_songs_per_artist_from_api(artist)
            except Exception as e:
                with open('songs_test.json', 'w') as outf:
                    json.dump(res, outf)

    with open('songs_test.json', 'w') as outf:
        json.dump(res, outf)


def remove_duplicate_songs():
    res = get_data_from_file('songs.json')
    seen = set()
    before = 0
    after = 0
    for artist in res.keys():
        if res[artist] is not None:
            before += len(res[artist])
            for song in res[artist]:
                if song in seen:
                    res[artist].remove(song)
                else:
                    seen.add(song)
    for artist in res.keys():
        if res[artist] is not None:
            after += len(res[artist])
    print 'before = %d' % before
    print 'after = %d' % after

    with open('songs_unique.json', 'w') as outf:
        json.dump(res, outf)


def main():
    assert API_KEY != 'secret'







""""
res = []
categories = retrieive_all_categories()
for cat in categories:
    request_artist_base_url = BASE_URL + '&method=tag.gettopartists'
    artists = retrieve_artists_per_category(request_artist_base_url, cat)
    for artist in artists:
        request_song_base_url = BASE_URL + '&method=artist.gettoptracks'
        songs = retrieve_songs_per_artist(request_song_base_url, artist)
        for song in songs:
            res.append((song,artist))
            
"""









if __name__ == '__main__':
    main()