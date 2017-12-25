# -*- coding: utf-8 -*-

import os
import json
import codecs
import retrieve_lyrics_data

import swagger_client
from swagger_client.rest import ApiException


def main():
    # str | Account api key, to be used in every api call
    api_key = 'secret'
    swagger_client.configuration.api_key['apikey'] = api_key
    # create an instance of the API class
    api_instance = swagger_client.LyricsApi()
    err_cnt = 0
    none_response = 0
    not_ascii_cnt = 0
    total_lyrics = 0
    data = get_all_tracks()
    # dictionary to store (track : lyrics)
    d = {}
    # a list to store all the titles which contain non-asci characters
    # TODO repair some of the non-ascii
    not_ascii = []
    for category in data:
        for track in category:
            if is_valid_asci(track):
                try:
                    api_response = api_instance.matcher_lyrics_get_get(format='json', q_track=track).to_dict()
                    if api_response['message']['body']['lyrics'] is not None:
                        lyrics = api_response['message']['body']['lyrics']['lyrics_body']
                        d[track] = lyrics
                        total_lyrics += 1
                    else:
                        none_response += 1
                except ApiException as e:
                    err_cnt += 1
                    print "Exception when calling LyricsApi->matcher_lyrics_get_get: %s\n" % e
            # not a valid ascii
            else:
                not_ascii.append(track)
                not_ascii_cnt += 1
    print "Total lyrcs count = {:d} ".format(total_lyrics)
    print "Not ASCII count = {:d} ".format(not_ascii_cnt)
    print "Error count = {:d} ".format(err_cnt)
    print "None response = {:d} ".format(none_response)

    with open('lyrics.json', 'w') as lyrics_file:
        json.dump(d, lyrics_file)

    with codecs.open('not_asci.txt', 'w', encoding='utf-8') as not_asci_file:
        for item in not_ascii:
            not_asci_file.write("%s\n" % item)

    return True


# get json of all playlists including songs
def get_all_tracks():
    return retrieve_lyrics_data.retrieve_all_tracks()


def is_valid_asci(track):
    return all(ord(c) < 128 for c in track)


if __name__ == '__main__':
    main()
