# coding: utf-8

"""
    Musixmatch API

    Musixmatch lyrics API is a robust service that permits you to search and retrieve lyrics in the simplest possible way. It just works.  Include millions of licensed lyrics on your website or in your application legally.  The fastest, most powerful and legal way to display lyrics on your website or in your application.  #### Read musixmatch API Terms & Conditions and the Privacy Policy: Before getting started, you must take a look at the [API Terms & Conditions](http://musixmatch.com/apiterms/) and the [Privacy Policy](https://developer.musixmatch.com/privacy). We’ve worked hard to make this service completely legal so that we are all protected from any foreseeable liability. Take the time to read this stuff.  #### Register for an API key: All you need to do is [register](https://developer.musixmatch.com/signup) in order to get your API key, a mandatory parameter for most of our API calls. It’s your personal identifier and should be kept secret:  ```   https://api.musixmatch.com/ws/v1.1/track.get?apikey=YOUR_API_KEY ``` #### Integrate the musixmatch service with your web site or application In the most common scenario you only need to implement two API calls:  The first call is to match your catalog to ours using the [track.search](#!/Track/get_track_search) function and the second is to get the lyrics using the [track.lyrics.get](#!/Lyrics/get_track_lyrics_get) api. That’s it!  ## API Methods What does the musiXmatch API do?  The musiXmatch API allows you to read objects from our huge 100% licensed lyrics database.  To make your life easier we are providing you with one or more examples to show you how it could work in the wild. You’ll find both the API request and API response in all the available output formats for each API call. Follow the links below for the details.  The current API version is 1.1, the root URL is located at https://api.musixmatch.com/ws/1.1/  Supported input parameters can be found on the page [Input Parameters](https://developer.musixmatch.com/documentation/input-parameters). Use UTF-8 to encode arguments when calling API methods.  Every response includes a status_code. A list of all status codes can be consulted at [Status Codes](https://developer.musixmatch.com/documentation/status-codes).  ## Music meta data The musiXmatch api is built around lyrics, but there are many other data we provide through the api that can be used to improve every existent music service.  ## Track Inside the track object you can get the following extra information:  ### TRACK RATING  The track rating is a score 0-100 identifying how popular is a song in musixmatch.  You can use this information to sort search results, like the most popular songs of an artist, of a music genre, of a lyrics language.  ### INSTRUMENTAL AND EXPLICIT FLAGS  The instrumental flag identifies songs with music only, no lyrics.  The explicit flag identifies songs with explicit lyrics or explicit title. We're able to identify explicit words and set the flag for the most common languages.  ### FAVOURITES  How many users have this song in their list of favourites.  Can be used to sort tracks by num favourite to identify more popular tracks within a set.  ### MUSIC GENRE  The music genere of the song.  Can be used to group songs by genre, as input for similarity alghorithms, artist genre identification, navigate songs by genere, etc.  ### SONG TITLES TRANSLATIONS  The track title, as translated in different lanauages, can be used to display the right writing for a given user, example:  LIES (Bigbang) becomes 在光化門 in chinese HALLELUJAH (Bigbang) becomes ハレルヤ in japanese   ## Artist Inside the artist object you can get the following nice extra information:  ### COMMENTS AND COUNTRY  An artist comment is a short snippet of text which can be mainly used for disambiguation.  The artist country is the born country of the artist/group  There are two perfect search result if you search by artist with the keyword \"U2\". Indeed there are two distinct music groups with this same name, one is the most known irish group of Bono Vox, the other is a less popular (world wide speaking) group from Japan.  Here's how you can made use of the artist comment in your search result page:  U2 (Irish rock band) U2 (あきやまうに) You can also show the artist country for even better disambiguation:  U2 (Irish rock band) from Ireland U2 (あきやまうに) from Japan ARTIST TRANSLATIONS  When you create a world wide music related service you have to take into consideration to display the artist name in the user's local language. These translation are also used as aliases to improve the search results.  Let's use PSY for this example.  Western people know him as PSY but korean want to see the original name 싸이.  Using the name translations provided by our api you can show to every user the writing they expect to see.  Furthermore, when you search for \"psy gangnam style\" or \"싸이 gangnam style\" with our search/match api you will still be able to find the song.  ### ARTIST RATING  The artist rating is a score 0-100 identifying how popular is an artist in musixmatch.  You can use this information to build charts, for suggestions, to sort search results. In the example above about U2, we use the artist rating to show the irish band before the japanese one in our serp.  ### ARTIST MUSIC GENRE  We provide one or more main artist genre, this information can be used to calculate similar artist, suggestions, or the filter a search by artist genre.    ## Album Inside the album object you can get the following nice extra information:  ### ALBUM RATING  The album rating is a score 0-100 identifying how popular is an album in musixmatch.  You can use this information to sort search results, like the most popular albums of an artist.  ### ALBUM RATING  The album rating is a score 0-100 identifying how popular is an album in musixmatch.  You can use this information to sort search results, like the most popular albums of an artist.  ### ALBUM COPYRIGHT AND LABEL  For most of our albums we can provide extra information like for example:  Label: Universal-Island Records Ltd. Copyright: (P) 2013 Rubyworks, under license to Columbia Records, a Division of Sony Music Entertainment. ALBUM TYPE AND RELEASE DATE  The album official release date can be used to sort an artist's albums view starting by the most recent one.  Album can also be filtered or grouped by type: Single, Album, Compilation, Remix, Live. This can help to build an artist page with a more organized structure.  ### ALBUM MUSIC GENRE  For most of the albums we provide two groups of music genres. Primary and secondary. This information can be used to help user navigate albums by genre.  An example could be:  Primary genere: POP Secondary genre: K-POP or Mandopop 

    OpenAPI spec version: 1.1.0
    Contact: info@musixmatch.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class TrackApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def album_tracks_get_get(self, album_id, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.album_tracks_get_get(album_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str album_id: The musiXmatch album id (required)
        :param str format: output format: json, jsonp, xml.
        :param str callback: jsonp callback
        :param str f_has_lyrics: When set, filter only contents with lyrics
        :param float page: Define the page number for paginated results
        :param float page_size: Define the page size for paginated results.Range is 1 to 100.
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.album_tracks_get_get_with_http_info(album_id, **kwargs)
        else:
            (data) = self.album_tracks_get_get_with_http_info(album_id, **kwargs)
            return data

    def album_tracks_get_get_with_http_info(self, album_id, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.album_tracks_get_get_with_http_info(album_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str album_id: The musiXmatch album id (required)
        :param str format: output format: json, jsonp, xml.
        :param str callback: jsonp callback
        :param str f_has_lyrics: When set, filter only contents with lyrics
        :param float page: Define the page number for paginated results
        :param float page_size: Define the page size for paginated results.Range is 1 to 100.
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['album_id', 'format', 'callback', 'f_has_lyrics', 'page', 'page_size']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method album_tracks_get_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'album_id' is set
        if ('album_id' not in params) or (params['album_id'] is None):
            raise ValueError("Missing the required parameter `album_id` when calling `album_tracks_get_get`")

        resource_path = '/album.tracks.get'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'format' in params:
            query_params['format'] = params['format']
        if 'callback' in params:
            query_params['callback'] = params['callback']
        if 'album_id' in params:
            query_params['album_id'] = params['album_id']
        if 'f_has_lyrics' in params:
            query_params['f_has_lyrics'] = params['f_has_lyrics']
        if 'page' in params:
            query_params['page'] = params['page']
        if 'page_size' in params:
            query_params['page_size'] = params['page_size']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['key']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='InlineResponse2001',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def chart_tracks_get_get(self, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.chart_tracks_get_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str format: output format: json, jsonp, xml.
        :param str callback: jsonp callback
        :param float page: Define the page number for paginated results
        :param float page_size: Define the page size for paginated results.Range is 1 to 100.
        :param str country: A valid ISO 3166 country code
        :param str f_has_lyrics: When set, filter only contents with lyrics
        :return: InlineResponse2006
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.chart_tracks_get_get_with_http_info(**kwargs)
        else:
            (data) = self.chart_tracks_get_get_with_http_info(**kwargs)
            return data

    def chart_tracks_get_get_with_http_info(self, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.chart_tracks_get_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str format: output format: json, jsonp, xml.
        :param str callback: jsonp callback
        :param float page: Define the page number for paginated results
        :param float page_size: Define the page size for paginated results.Range is 1 to 100.
        :param str country: A valid ISO 3166 country code
        :param str f_has_lyrics: When set, filter only contents with lyrics
        :return: InlineResponse2006
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['format', 'callback', 'page', 'page_size', 'country', 'f_has_lyrics']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method chart_tracks_get_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/chart.tracks.get'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'format' in params:
            query_params['format'] = params['format']
        if 'callback' in params:
            query_params['callback'] = params['callback']
        if 'page' in params:
            query_params['page'] = params['page']
        if 'page_size' in params:
            query_params['page_size'] = params['page_size']
        if 'country' in params:
            query_params['country'] = params['country']
        if 'f_has_lyrics' in params:
            query_params['f_has_lyrics'] = params['f_has_lyrics']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['key']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='InlineResponse2006',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def matcher_track_get_get(self, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.matcher_track_get_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str format: output format: json, jsonp, xml.
        :param str callback: jsonp callback
        :param str q_artist: The song artist
        :param str q_track: The song title
        :param float f_has_lyrics: When set, filter only contents with lyrics
        :param float f_has_subtitle: When set, filter only contents with subtitles
        :return: InlineResponse2009
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.matcher_track_get_get_with_http_info(**kwargs)
        else:
            (data) = self.matcher_track_get_get_with_http_info(**kwargs)
            return data

    def matcher_track_get_get_with_http_info(self, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.matcher_track_get_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str format: output format: json, jsonp, xml.
        :param str callback: jsonp callback
        :param str q_artist: The song artist
        :param str q_track: The song title
        :param float f_has_lyrics: When set, filter only contents with lyrics
        :param float f_has_subtitle: When set, filter only contents with subtitles
        :return: InlineResponse2009
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['format', 'callback', 'q_artist', 'q_track', 'f_has_lyrics', 'f_has_subtitle']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method matcher_track_get_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/matcher.track.get'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'format' in params:
            query_params['format'] = params['format']
        if 'callback' in params:
            query_params['callback'] = params['callback']
        if 'q_artist' in params:
            query_params['q_artist'] = params['q_artist']
        if 'q_track' in params:
            query_params['q_track'] = params['q_track']
        if 'f_has_lyrics' in params:
            query_params['f_has_lyrics'] = params['f_has_lyrics']
        if 'f_has_subtitle' in params:
            query_params['f_has_subtitle'] = params['f_has_subtitle']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['key']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='InlineResponse2009',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def track_get_get(self, track_id, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.track_get_get(track_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str track_id: The musiXmatch track id (required)
        :param str format: output format: json, jsonp, xml.
        :param str callback: jsonp callback
        :return: InlineResponse2009
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.track_get_get_with_http_info(track_id, **kwargs)
        else:
            (data) = self.track_get_get_with_http_info(track_id, **kwargs)
            return data

    def track_get_get_with_http_info(self, track_id, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.track_get_get_with_http_info(track_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str track_id: The musiXmatch track id (required)
        :param str format: output format: json, jsonp, xml.
        :param str callback: jsonp callback
        :return: InlineResponse2009
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['track_id', 'format', 'callback']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method track_get_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'track_id' is set
        if ('track_id' not in params) or (params['track_id'] is None):
            raise ValueError("Missing the required parameter `track_id` when calling `track_get_get`")

        resource_path = '/track.get'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'format' in params:
            query_params['format'] = params['format']
        if 'callback' in params:
            query_params['callback'] = params['callback']
        if 'track_id' in params:
            query_params['track_id'] = params['track_id']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['key']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='InlineResponse2009',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def track_search_get(self, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.track_search_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str format: output format: json, jsonp, xml.
        :param str callback: jsonp callback
        :param str q_track: The song title
        :param str q_artist: The song artist
        :param str q_lyrics: Any word in the lyrics
        :param float f_artist_id: When set, filter by this artist id
        :param float f_music_genre_id: When set, filter by this music category id
        :param float f_lyrics_language: Filter by the lyrics language (en,it,..)
        :param float f_has_lyrics: When set, filter only contents with lyrics
        :param str s_artist_rating: Sort by our popularity index for artists (asc|desc)
        :param str s_track_rating: Sort by our popularity index for tracks (asc|desc)
        :param float quorum_factor: Search only a part of the given query string.Allowed range is (0.1 – 0.9)
        :param float page_size: Define the page size for paginated results.Range is 1 to 100.
        :param float page: Define the page number for paginated results
        :return: InlineResponse2006
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.track_search_get_with_http_info(**kwargs)
        else:
            (data) = self.track_search_get_with_http_info(**kwargs)
            return data

    def track_search_get_with_http_info(self, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.track_search_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str format: output format: json, jsonp, xml.
        :param str callback: jsonp callback
        :param str q_track: The song title
        :param str q_artist: The song artist
        :param str q_lyrics: Any word in the lyrics
        :param float f_artist_id: When set, filter by this artist id
        :param float f_music_genre_id: When set, filter by this music category id
        :param float f_lyrics_language: Filter by the lyrics language (en,it,..)
        :param float f_has_lyrics: When set, filter only contents with lyrics
        :param str s_artist_rating: Sort by our popularity index for artists (asc|desc)
        :param str s_track_rating: Sort by our popularity index for tracks (asc|desc)
        :param float quorum_factor: Search only a part of the given query string.Allowed range is (0.1 – 0.9)
        :param float page_size: Define the page size for paginated results.Range is 1 to 100.
        :param float page: Define the page number for paginated results
        :return: InlineResponse2006
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['format', 'callback', 'q_track', 'q_artist', 'q_lyrics', 'f_artist_id', 'f_music_genre_id', 'f_lyrics_language', 'f_has_lyrics', 's_artist_rating', 's_track_rating', 'quorum_factor', 'page_size', 'page']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method track_search_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/track.search'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'format' in params:
            query_params['format'] = params['format']
        if 'callback' in params:
            query_params['callback'] = params['callback']
        if 'q_track' in params:
            query_params['q_track'] = params['q_track']
        if 'q_artist' in params:
            query_params['q_artist'] = params['q_artist']
        if 'q_lyrics' in params:
            query_params['q_lyrics'] = params['q_lyrics']
        if 'f_artist_id' in params:
            query_params['f_artist_id'] = params['f_artist_id']
        if 'f_music_genre_id' in params:
            query_params['f_music_genre_id'] = params['f_music_genre_id']
        if 'f_lyrics_language' in params:
            query_params['f_lyrics_language'] = params['f_lyrics_language']
        if 'f_has_lyrics' in params:
            query_params['f_has_lyrics'] = params['f_has_lyrics']
        if 's_artist_rating' in params:
            query_params['s_artist_rating'] = params['s_artist_rating']
        if 's_track_rating' in params:
            query_params['s_track_rating'] = params['s_track_rating']
        if 'quorum_factor' in params:
            query_params['quorum_factor'] = params['quorum_factor']
        if 'page_size' in params:
            query_params['page_size'] = params['page_size']
        if 'page' in params:
            query_params['page'] = params['page']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['key']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='InlineResponse2006',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
