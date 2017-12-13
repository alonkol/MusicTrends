# -*- coding: utf-8 -*-

import os
import json

import flask
import retrieve_data

import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery

# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret.
CLIENT_SECRETS_FILE = "client_secret.json"

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account and requires requests to use an SSL connection.
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

app = flask.Flask(__name__)
# Note: A secret key is included in the sample so that it works, but if you
# use this code in your application please replace this with a truly secret
# key. See http://flask.pocoo.org/docs/0.12/quickstart/#sessions.
# app.secret_key = 'REPLACE ME - this value is here as a placeholder.'


@app.route('/')
def index():
    if 'credentials' not in flask.session:
        return flask.redirect('authorize')

    # Load the credentials from the session.
    credentials = google.oauth2.credentials.Credentials(
        **flask.session['credentials'])

    client = googleapiclient.discovery.build(
        API_SERVICE_NAME, API_VERSION, credentials=credentials)

    data = get_all_playlists(client)
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)

    return flask.jsonify({'success': True})

# get json of all playlists including songs
def get_all_playlists(client):
    playlists_keys = retrieve_data.retrieive_all_playlists()
    playlists = {'items': []}

    for (id, name) in playlists_keys:
        playlist = get_all_playlist_songs(client, playlistId=id)
        playlist['genre'] = name
        playlists['items'].append(playlist)

    return playlists


def get_all_playlist_songs(client, playlistId):
    songs = json.loads(playlist_items_list_by_playlist_id(client,
                                              part='snippet,contentDetails',
                                              maxResults=50,
                                              playlistId=playlistId).data)

    while songs['nextPageToken'] != 'null':

        song_chunk = json.loads(playlist_items_list_by_playlist_id(client,
                                              part='snippet,contentDetails',
                                              maxResults=50,
                                              pageToken=songs['nextPageToken'],
                                              playlistId=playlistId).data)

        if 'nextPageToken' in song_chunk:
            songs['nextPageToken'] = song_chunk['nextPageToken']
        else:
            songs['nextPageToken'] = 'null'

        songs['items'] += song_chunk['items']

    return songs

# Remove keyword arguments that are not set
def remove_empty_kwargs(**kwargs):
  good_kwargs = {}
  if kwargs is not None:
    for key, value in kwargs.iteritems():
      if value:
        good_kwargs[key] = value
  return good_kwargs


def print_response(response):
  print(response)


@app.route('/authorize')
def authorize():
    # Create a flow instance to manage the OAuth 2.0 Authorization Grant Flow
    # steps.
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE, scopes=SCOPES)
    flow.redirect_uri = flask.url_for('oauth2callback', _external=True)
    authorization_url, state = flow.authorization_url(
        # This parameter enables offline access which gives your application
        # both an access and refresh token.
        access_type='offline',
        # This parameter enables incremental auth.
        include_granted_scopes='true')

    # Store the state in the session so that the callback can verify that
    # the authorization server response.
    flask.session['state'] = state

    return flask.redirect(authorization_url)


@app.route('/oauth2callback')
def oauth2callback():
    # Specify the state when creating the flow in the callback so that it can
    # verify the authorization server response.
    state = flask.session['state']
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE, scopes=SCOPES, state=state)
    flow.redirect_uri = flask.url_for('oauth2callback', _external=True)

    # Use the authorization server's response to fetch the OAuth 2.0 tokens.
    authorization_response = flask.request.url
    flow.fetch_token(authorization_response=authorization_response)

    # Store the credentials in the session.
    # ACTION ITEM for developers:
    #     Store user's access and refresh tokens in your data store if
    #     incorporating this code into your real app.
    credentials = flow.credentials
    flask.session['credentials'] = {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes
    }

    return flask.redirect(flask.url_for('index'))


def channels_list_by_username(client, **kwargs):
    response = client.channels().list(
        **kwargs
    ).execute()

    return flask.jsonify(**response)


def playlist_items_list_by_playlist_id(client, **kwargs):
   # See full sample for function
   kwargs = remove_empty_kwargs(**kwargs)

   response = client.playlistItems().list(
     **kwargs
   ).execute()

   return flask.jsonify(**response)


if __name__ == '__main__':
    # When running locally, disable OAuthlib's HTTPs verification. When
    # running in production *do not* leave this option enabled.
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    app.run('localhost', 8090, debug=True)