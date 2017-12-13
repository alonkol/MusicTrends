import re
import requests

CHANNELS_URL = 'https://www.youtube.com/channel/UC-9-kyTW8ZkZNDHQJ6FgpwQ/channels'
FILE_TO_PARSE = 'Music-Youtube.html'


# returns list of (playlist_id, genre_name) in unicode
def retrieive_all_playlists():
    playlists = []

    for url in get_channels_urls():
        channel_html = requests.get(url).text
        playlist = retrieve_top_playlist_id_from_channel(channel_html)
        if playlist:
            playlists.append(retrieve_top_playlist_id_from_channel(channel_html))

    return playlists


# returns tuple (playlist_id, genre_name)
def retrieve_top_playlist_id_from_channel(channel_html):

    playlist = re.search(ur'<a href="/playlist\?list=(.+?)" class.+\s+<span.+\s+<span.+Top Tracks - (.+)<', channel_html)
    if playlist:
        return playlist.groups()

    return None


# get channels of different genres
def get_channels_urls():
    with open(FILE_TO_PARSE, 'r') as f:
        return re.findall(r'<a id="channel-info" .+ href="(.+)">', f.read())


def main():
    print retrieive_all_playlists()


if __name__ == '__main__':
    main()