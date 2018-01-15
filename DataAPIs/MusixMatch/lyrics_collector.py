# -*- coding: utf-8 -*-

import codecs
import json

import swagger_client
from swagger_client.rest import ApiException

import retrieve_lyrics_data
from DataAPIs.LastFM.retreive_data_from_last_fm import SONGS_FILE

LYRICS_FILE = 'lyrics_for_artists.json'
SONGS_JSON = '../LastFmApiHandler/'+SONGS_FILE
MUSIXMATCH_API_KEY = '476c97d9273a03b4ef62f21a5de63b59'


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


def is_valid_asci(string):
    return all(ord(c) < 128 for c in string)


def main():
    get_all_lyrics()


if __name__ == '__main__':
    main()
