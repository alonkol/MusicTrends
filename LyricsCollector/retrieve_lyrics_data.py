import json
import re

import requests

DATA_TO_PARSE = 'data.json'


# returns all video descriptions from DATA
# the return value is a list of lists (per category)
def retrieve_all_tracks():
    with open(DATA_TO_PARSE, 'r') as data:
        js_data = json.load(data)
        num_of_categories = len(js_data['items'])
        num_of_tracks = 0
        tracks = [[] for x in range(num_of_categories)]
        for i in range(num_of_categories):
            num_of_tracks += len(js_data['items'][i]['items'])
            for j in range(len(js_data['items'][i]['items'])):
                line = js_data['items'][i]['items'][j]['snippet']['title']
                tracks[i].append(line)
        return tracks


def main():
    print retrieve_all_tracks()


if __name__ == '__main__':
    main()
