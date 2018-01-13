# -*- coding: utf-8 -*-

import codecs
import json

import swagger_client
from swagger_client.rest import ApiException

import retrieve_lyrics_data
from DataAPIs.LastFM.retreive_data_from_last_fm import SONGS_FILE

LYRICS_FILE = 'lyrics_with_language.json'
SONGS_JSON = '../LastFmApiHandler/'+SONGS_FILE
MUSIXMATCH_API_KEY = '476c97d9273a03b4ef62f21a5de63b59'


def find_duplicates():
    removed_from_asci = 0
    removed_from_empty = 0
    asci_empty = 0
    with open('lyrics.json', 'r') as track_with_lyrics:
        lyrics = json.load(track_with_lyrics)
        not_ascii_tracks = get_unique_data_from_text_file('not_asci.txt')
        empty = get_unique_data_from_text_file('empty_lyrics.txt')
        data = json.load(open(SONGS_JSON))
        for song in lyrics.keys():
            if song in not_ascii_tracks:
                removed_from_asci += 1
                not_ascii_tracks.remove(song)
            if song in empty:
                removed_from_empty += 1
                empty.remove(song)

    for x in not_ascii_tracks:
        if x in empty:
            asci_empty += 1
    print removed_from_asci
    print removed_from_empty
    print asci_empty


def store_remaining_songs():
    songs_left = set()
    cnt = 0
    total_songs = 0
    with open('lyrics.json', 'r') as track_with_lyrics:
        lyrics = json.load(track_with_lyrics)
        not_ascii_tracks = get_unique_data_from_text_file('not_asci.txt')
        empty = get_unique_data_from_text_file('empty_lyrics.txt')
        data = json.load(open(SONGS_JSON))
        for artist in data.keys():
            if data[artist] is not None:
                for song in data[artist]:
                    total_songs += 1
                    if (song not in not_ascii_tracks) and (song not in lyrics) and (song not in empty):
                        cnt += 1
                        songs_left.add(song)

    with codecs.open('remaining_songs.txt', 'w', encoding='utf-8') as f:
        for item in songs_left:
            f.write("%s\n" % item)

    print "total songs = %d" % total_songs
    print "num of songs left = %d" % len(songs_left)
    print "count = %d" % cnt
    print "lyrics = %d" % len(lyrics.keys())
    print "non_ascii = %d" % len(not_ascii_tracks)
    print "empty = %d" % len(empty)


def get_lyrics_from_api(track_name,artist_name, api_instance=None):
    if api_instance is None:
        # str | Account api key, to be used in every api call
        api_key = MUSIXMATCH_API_KEY
        assert api_key != 'secret'
        swagger_client.configuration.api_key['apikey'] = api_key
        # create an instance of the API class
        api_instance = swagger_client.LyricsApi()
    try:
        api_response = api_instance.matcher_lyrics_get_get(format='json', q_track=track_name, q_artist=artist_name).to_dict()
        if api_response['message']['body']['lyrics'] is not None:
            lyrics = api_response['message']['body']['lyrics']['lyrics_body']
            language = api_response['message']['body']['lyrics']['lyrics_language']
            return lyrics, language
    except ApiException as e:
        print "Exception when calling LyricsApi->matcher_lyrics_get_get: %s\n" % e
    return None, None


def store_empty_lyrics_from_json(fname):
    with open(fname) as f:
        lyrics = json.load(f)
        empty = []
        for song in lyrics:
            if lyrics[song] == "":
                empty.append(song)
        with codecs.open('empty_lyrics.txt', 'w', encoding='utf-8') as f:
            for item in empty:
                f.write("%s\n" % item)
        print len(empty)


def get_unique_data_from_text_file(fname):
    with codecs.open(fname, 'r', encoding='utf-8') as f1:
        lines = f1.readlines()
        return set([x.strip() for x in lines])


def remove_empty_lyrics_from_json():
    with open('lyrics_with_empty.json') as f:
        removed = 0
        lyrics = json.load(f)
        for song , words in lyrics.items():
            if words == "":
                del lyrics[song]
                removed += 1

    with open(LYRICS_FILE, 'w') as lyrics_file:
        json.dump(lyrics, lyrics_file)
    print "removed %d itmes" % removed


def get_all_lyrics():
    # str | Account api key, to be used in every api call
    api_key = MUSIXMATCH_API_KEY
    assert api_key != 'secret'
    swagger_client.configuration.api_key['apikey'] = api_key
    # create an instance of the API class
    api_instance = swagger_client.LyricsApi()
    total_lyrics = 0
    data = json.load(open(SONGS_JSON))

    # dictionary to store (track : lyrics)
    d = {}
    for artist in data.keys():
        if data[artist] is not None:
            for song_data in data[artist]:
                song_name = song_data[0]
                mbid = song_data[1]
                if (is_valid_asci(song_name)) and is_valid_asci(artist):
                        lyrics = get_lyrics_for_song(song_name, artist, api_instance)
                        d_inner = {'song_name': song_name, 'lyrics': lyrics}
                        d[mbid] = d_inner.copy()
                        total_lyrics += 1
    print "Total lyrics count = {:d} ".format(total_lyrics)

    with open(LYRICS_FILE, 'w') as lyrics_file:
        json.dump(d, lyrics_file)

    return True


def get_lyrics_for_song(song, artist, api_instance=None):
    lyrics, language = get_lyrics_from_api(song, artist, api_instance)
    if lyrics is None or lyrics == "" or language == "" or language != "en":
        return None
    if is_valid_asci(lyrics):
        return lyrics
    return None


# get json of all playlists including songs
def get_all_tracks():
    return retrieve_lyrics_data.retrieve_all_tracks()


def is_valid_asci(string):
    return all(ord(c) < 128 for c in string)


def main():
    get_all_lyrics()


if __name__ == '__main__':
    main()
