import requests
import json
import time

LASTFM_API_KEY = 'bb71a65a3332770c8340f1b151d3e0ef'
BASE_URL = 'http://ws.audioscrobbler.com/2.0/?api_key={}&method&format=json'.format(LASTFM_API_KEY)

ARTISTS_FILE = 'artists.json'
SONGS_FILE = 'songs.json'
CATEGORIES_FILE = 'categories.json'


def get_all_categories_from_api():
    url = BASE_URL + '&method=tag.getTopTags'
    response = requests.get(url)
    d = json.loads(response.text)['toptags']['tag']
    with open('categories.json', 'w') as outf:
        json.dump(d, outf)


def get_data_from_file(filename):
    return json.load(open(filename))


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
    categories = get_data_from_file(CATEGORIES_FILE)
    for category in categories:
        res[category['name']] = get_artists_per_category_from_api(category['name'])
    with open(ARTISTS_FILE, 'w') as outf:
        json.dump(res, outf)


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
        time.sleep(0.1)
        response = requests.get(url)
        if 'toptracks' in json.loads(response.text):
            d = json.loads(response.text)['toptracks']['track']
            for k in d:
                try:
                    res.append((k['name'], k['mbid']))
                except KeyError:
                    continue
            return res
        else:
            print("no toptracks for artist % s" % artist)
            print url
            print(" response = %s " % response)
    except Exception as e:
        print('Problem with artist %s' % artist)
        print(e)
        return res


def get_all_songs_from_api():
    res = {}
    artists_per_category = get_data_from_file(ARTISTS_FILE)
    for cat in artists_per_category.values():
        for artist in cat:
            try:
                res[artist] = get_songs_per_artist_from_api(artist)
            except Exception as e:
                print(e)

    with open(SONGS_FILE, 'w') as outf:
        json.dump(res, outf)


def main():
    assert LASTFM_API_KEY != 'secret'
    get_all_songs_from_api()

if __name__ == '__main__':
    main()