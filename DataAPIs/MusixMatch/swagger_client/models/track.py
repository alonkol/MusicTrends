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

from pprint import pformat
from six import iteritems
import re


class Track(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, instrumental=None, album_coverart_350x350=None, first_release_date=None, track_isrc=None, explicit=None, track_edit_url=None, num_favourite=None, album_coverart_500x500=None, album_name=None, track_rating=None, track_share_url=None, track_soundcloud_id=None, artist_name=None, album_coverart_800x800=None, album_coverart_100x100=None, track_name_translation_list=None, track_name=None, restricted=None, has_subtitles=None, updated_time=None, subtitle_id=None, lyrics_id=None, track_spotify_id=None, has_lyrics=None, artist_id=None, album_id=None, artist_mbid=None, secondary_genres=None, commontrack_vanity_id=None, track_id=None, track_xboxmusic_id=None, primary_genres=None, track_length=None, track_mbid=None, commontrack_id=None):
        """
        Track - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'instrumental': 'float',
            'album_coverart_350x350': 'str',
            'first_release_date': 'str',
            'track_isrc': 'str',
            'explicit': 'float',
            'track_edit_url': 'str',
            'num_favourite': 'float',
            'album_coverart_500x500': 'str',
            'album_name': 'str',
            'track_rating': 'float',
            'track_share_url': 'str',
            'track_soundcloud_id': 'float',
            'artist_name': 'str',
            'album_coverart_800x800': 'str',
            'album_coverart_100x100': 'str',
            'track_name_translation_list': 'list[str]',
            'track_name': 'str',
            'restricted': 'float',
            'has_subtitles': 'float',
            'updated_time': 'str',
            'subtitle_id': 'float',
            'lyrics_id': 'float',
            'track_spotify_id': 'str',
            'has_lyrics': 'float',
            'artist_id': 'float',
            'album_id': 'float',
            'artist_mbid': 'str',
            'secondary_genres': 'TrackSecondaryGenres',
            'commontrack_vanity_id': 'str',
            'track_id': 'float',
            'track_xboxmusic_id': 'str',
            'primary_genres': 'TrackPrimaryGenres',
            'track_length': 'float',
            'track_mbid': 'str',
            'commontrack_id': 'float'
        }

        self.attribute_map = {
            'instrumental': 'instrumental',
            'album_coverart_350x350': 'album_coverart_350x350',
            'first_release_date': 'first_release_date',
            'track_isrc': 'track_isrc',
            'explicit': 'explicit',
            'track_edit_url': 'track_edit_url',
            'num_favourite': 'num_favourite',
            'album_coverart_500x500': 'album_coverart_500x500',
            'album_name': 'album_name',
            'track_rating': 'track_rating',
            'track_share_url': 'track_share_url',
            'track_soundcloud_id': 'track_soundcloud_id',
            'artist_name': 'artist_name',
            'album_coverart_800x800': 'album_coverart_800x800',
            'album_coverart_100x100': 'album_coverart_100x100',
            'track_name_translation_list': 'track_name_translation_list',
            'track_name': 'track_name',
            'restricted': 'restricted',
            'has_subtitles': 'has_subtitles',
            'updated_time': 'updated_time',
            'subtitle_id': 'subtitle_id',
            'lyrics_id': 'lyrics_id',
            'track_spotify_id': 'track_spotify_id',
            'has_lyrics': 'has_lyrics',
            'artist_id': 'artist_id',
            'album_id': 'album_id',
            'artist_mbid': 'artist_mbid',
            'secondary_genres': 'secondary_genres',
            'commontrack_vanity_id': 'commontrack_vanity_id',
            'track_id': 'track_id',
            'track_xboxmusic_id': 'track_xboxmusic_id',
            'primary_genres': 'primary_genres',
            'track_length': 'track_length',
            'track_mbid': 'track_mbid',
            'commontrack_id': 'commontrack_id'
        }

        self._instrumental = instrumental
        self._album_coverart_350x350 = album_coverart_350x350
        self._first_release_date = first_release_date
        self._track_isrc = track_isrc
        self._explicit = explicit
        self._track_edit_url = track_edit_url
        self._num_favourite = num_favourite
        self._album_coverart_500x500 = album_coverart_500x500
        self._album_name = album_name
        self._track_rating = track_rating
        self._track_share_url = track_share_url
        self._track_soundcloud_id = track_soundcloud_id
        self._artist_name = artist_name
        self._album_coverart_800x800 = album_coverart_800x800
        self._album_coverart_100x100 = album_coverart_100x100
        self._track_name_translation_list = track_name_translation_list
        self._track_name = track_name
        self._restricted = restricted
        self._has_subtitles = has_subtitles
        self._updated_time = updated_time
        self._subtitle_id = subtitle_id
        self._lyrics_id = lyrics_id
        self._track_spotify_id = track_spotify_id
        self._has_lyrics = has_lyrics
        self._artist_id = artist_id
        self._album_id = album_id
        self._artist_mbid = artist_mbid
        self._secondary_genres = secondary_genres
        self._commontrack_vanity_id = commontrack_vanity_id
        self._track_id = track_id
        self._track_xboxmusic_id = track_xboxmusic_id
        self._primary_genres = primary_genres
        self._track_length = track_length
        self._track_mbid = track_mbid
        self._commontrack_id = commontrack_id

    @property
    def instrumental(self):
        """
        Gets the instrumental of this Track.
        

        :return: The instrumental of this Track.
        :rtype: float
        """
        return self._instrumental

    @instrumental.setter
    def instrumental(self, instrumental):
        """
        Sets the instrumental of this Track.
        

        :param instrumental: The instrumental of this Track.
        :type: float
        """

        self._instrumental = instrumental

    @property
    def album_coverart_350x350(self):
        """
        Gets the album_coverart_350x350 of this Track.
        

        :return: The album_coverart_350x350 of this Track.
        :rtype: str
        """
        return self._album_coverart_350x350

    @album_coverart_350x350.setter
    def album_coverart_350x350(self, album_coverart_350x350):
        """
        Sets the album_coverart_350x350 of this Track.
        

        :param album_coverart_350x350: The album_coverart_350x350 of this Track.
        :type: str
        """

        self._album_coverart_350x350 = album_coverart_350x350

    @property
    def first_release_date(self):
        """
        Gets the first_release_date of this Track.
        

        :return: The first_release_date of this Track.
        :rtype: str
        """
        return self._first_release_date

    @first_release_date.setter
    def first_release_date(self, first_release_date):
        """
        Sets the first_release_date of this Track.
        

        :param first_release_date: The first_release_date of this Track.
        :type: str
        """

        self._first_release_date = first_release_date

    @property
    def track_isrc(self):
        """
        Gets the track_isrc of this Track.
        

        :return: The track_isrc of this Track.
        :rtype: str
        """
        return self._track_isrc

    @track_isrc.setter
    def track_isrc(self, track_isrc):
        """
        Sets the track_isrc of this Track.
        

        :param track_isrc: The track_isrc of this Track.
        :type: str
        """

        self._track_isrc = track_isrc

    @property
    def explicit(self):
        """
        Gets the explicit of this Track.
        

        :return: The explicit of this Track.
        :rtype: float
        """
        return self._explicit

    @explicit.setter
    def explicit(self, explicit):
        """
        Sets the explicit of this Track.
        

        :param explicit: The explicit of this Track.
        :type: float
        """

        self._explicit = explicit

    @property
    def track_edit_url(self):
        """
        Gets the track_edit_url of this Track.
        

        :return: The track_edit_url of this Track.
        :rtype: str
        """
        return self._track_edit_url

    @track_edit_url.setter
    def track_edit_url(self, track_edit_url):
        """
        Sets the track_edit_url of this Track.
        

        :param track_edit_url: The track_edit_url of this Track.
        :type: str
        """

        self._track_edit_url = track_edit_url

    @property
    def num_favourite(self):
        """
        Gets the num_favourite of this Track.
        

        :return: The num_favourite of this Track.
        :rtype: float
        """
        return self._num_favourite

    @num_favourite.setter
    def num_favourite(self, num_favourite):
        """
        Sets the num_favourite of this Track.
        

        :param num_favourite: The num_favourite of this Track.
        :type: float
        """

        self._num_favourite = num_favourite

    @property
    def album_coverart_500x500(self):
        """
        Gets the album_coverart_500x500 of this Track.
        

        :return: The album_coverart_500x500 of this Track.
        :rtype: str
        """
        return self._album_coverart_500x500

    @album_coverart_500x500.setter
    def album_coverart_500x500(self, album_coverart_500x500):
        """
        Sets the album_coverart_500x500 of this Track.
        

        :param album_coverart_500x500: The album_coverart_500x500 of this Track.
        :type: str
        """

        self._album_coverart_500x500 = album_coverart_500x500

    @property
    def album_name(self):
        """
        Gets the album_name of this Track.
        

        :return: The album_name of this Track.
        :rtype: str
        """
        return self._album_name

    @album_name.setter
    def album_name(self, album_name):
        """
        Sets the album_name of this Track.
        

        :param album_name: The album_name of this Track.
        :type: str
        """

        self._album_name = album_name

    @property
    def track_rating(self):
        """
        Gets the track_rating of this Track.
        

        :return: The track_rating of this Track.
        :rtype: float
        """
        return self._track_rating

    @track_rating.setter
    def track_rating(self, track_rating):
        """
        Sets the track_rating of this Track.
        

        :param track_rating: The track_rating of this Track.
        :type: float
        """

        self._track_rating = track_rating

    @property
    def track_share_url(self):
        """
        Gets the track_share_url of this Track.
        

        :return: The track_share_url of this Track.
        :rtype: str
        """
        return self._track_share_url

    @track_share_url.setter
    def track_share_url(self, track_share_url):
        """
        Sets the track_share_url of this Track.
        

        :param track_share_url: The track_share_url of this Track.
        :type: str
        """

        self._track_share_url = track_share_url

    @property
    def track_soundcloud_id(self):
        """
        Gets the track_soundcloud_id of this Track.
        

        :return: The track_soundcloud_id of this Track.
        :rtype: float
        """
        return self._track_soundcloud_id

    @track_soundcloud_id.setter
    def track_soundcloud_id(self, track_soundcloud_id):
        """
        Sets the track_soundcloud_id of this Track.
        

        :param track_soundcloud_id: The track_soundcloud_id of this Track.
        :type: float
        """

        self._track_soundcloud_id = track_soundcloud_id

    @property
    def artist_name(self):
        """
        Gets the artist_name of this Track.
        

        :return: The artist_name of this Track.
        :rtype: str
        """
        return self._artist_name

    @artist_name.setter
    def artist_name(self, artist_name):
        """
        Sets the artist_name of this Track.
        

        :param artist_name: The artist_name of this Track.
        :type: str
        """

        self._artist_name = artist_name

    @property
    def album_coverart_800x800(self):
        """
        Gets the album_coverart_800x800 of this Track.
        

        :return: The album_coverart_800x800 of this Track.
        :rtype: str
        """
        return self._album_coverart_800x800

    @album_coverart_800x800.setter
    def album_coverart_800x800(self, album_coverart_800x800):
        """
        Sets the album_coverart_800x800 of this Track.
        

        :param album_coverart_800x800: The album_coverart_800x800 of this Track.
        :type: str
        """

        self._album_coverart_800x800 = album_coverart_800x800

    @property
    def album_coverart_100x100(self):
        """
        Gets the album_coverart_100x100 of this Track.
        

        :return: The album_coverart_100x100 of this Track.
        :rtype: str
        """
        return self._album_coverart_100x100

    @album_coverart_100x100.setter
    def album_coverart_100x100(self, album_coverart_100x100):
        """
        Sets the album_coverart_100x100 of this Track.
        

        :param album_coverart_100x100: The album_coverart_100x100 of this Track.
        :type: str
        """

        self._album_coverart_100x100 = album_coverart_100x100

    @property
    def track_name_translation_list(self):
        """
        Gets the track_name_translation_list of this Track.


        :return: The track_name_translation_list of this Track.
        :rtype: list[str]
        """
        return self._track_name_translation_list

    @track_name_translation_list.setter
    def track_name_translation_list(self, track_name_translation_list):
        """
        Sets the track_name_translation_list of this Track.


        :param track_name_translation_list: The track_name_translation_list of this Track.
        :type: list[str]
        """

        self._track_name_translation_list = track_name_translation_list

    @property
    def track_name(self):
        """
        Gets the track_name of this Track.
        

        :return: The track_name of this Track.
        :rtype: str
        """
        return self._track_name

    @track_name.setter
    def track_name(self, track_name):
        """
        Sets the track_name of this Track.
        

        :param track_name: The track_name of this Track.
        :type: str
        """

        self._track_name = track_name

    @property
    def restricted(self):
        """
        Gets the restricted of this Track.
        

        :return: The restricted of this Track.
        :rtype: float
        """
        return self._restricted

    @restricted.setter
    def restricted(self, restricted):
        """
        Sets the restricted of this Track.
        

        :param restricted: The restricted of this Track.
        :type: float
        """

        self._restricted = restricted

    @property
    def has_subtitles(self):
        """
        Gets the has_subtitles of this Track.
        

        :return: The has_subtitles of this Track.
        :rtype: float
        """
        return self._has_subtitles

    @has_subtitles.setter
    def has_subtitles(self, has_subtitles):
        """
        Sets the has_subtitles of this Track.
        

        :param has_subtitles: The has_subtitles of this Track.
        :type: float
        """

        self._has_subtitles = has_subtitles

    @property
    def updated_time(self):
        """
        Gets the updated_time of this Track.
        

        :return: The updated_time of this Track.
        :rtype: str
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """
        Sets the updated_time of this Track.
        

        :param updated_time: The updated_time of this Track.
        :type: str
        """

        self._updated_time = updated_time

    @property
    def subtitle_id(self):
        """
        Gets the subtitle_id of this Track.
        

        :return: The subtitle_id of this Track.
        :rtype: float
        """
        return self._subtitle_id

    @subtitle_id.setter
    def subtitle_id(self, subtitle_id):
        """
        Sets the subtitle_id of this Track.
        

        :param subtitle_id: The subtitle_id of this Track.
        :type: float
        """

        self._subtitle_id = subtitle_id

    @property
    def lyrics_id(self):
        """
        Gets the lyrics_id of this Track.
        

        :return: The lyrics_id of this Track.
        :rtype: float
        """
        return self._lyrics_id

    @lyrics_id.setter
    def lyrics_id(self, lyrics_id):
        """
        Sets the lyrics_id of this Track.
        

        :param lyrics_id: The lyrics_id of this Track.
        :type: float
        """

        self._lyrics_id = lyrics_id

    @property
    def track_spotify_id(self):
        """
        Gets the track_spotify_id of this Track.
        

        :return: The track_spotify_id of this Track.
        :rtype: str
        """
        return self._track_spotify_id

    @track_spotify_id.setter
    def track_spotify_id(self, track_spotify_id):
        """
        Sets the track_spotify_id of this Track.
        

        :param track_spotify_id: The track_spotify_id of this Track.
        :type: str
        """

        self._track_spotify_id = track_spotify_id

    @property
    def has_lyrics(self):
        """
        Gets the has_lyrics of this Track.
        

        :return: The has_lyrics of this Track.
        :rtype: float
        """
        return self._has_lyrics

    @has_lyrics.setter
    def has_lyrics(self, has_lyrics):
        """
        Sets the has_lyrics of this Track.
        

        :param has_lyrics: The has_lyrics of this Track.
        :type: float
        """

        self._has_lyrics = has_lyrics

    @property
    def artist_id(self):
        """
        Gets the artist_id of this Track.
        

        :return: The artist_id of this Track.
        :rtype: float
        """
        return self._artist_id

    @artist_id.setter
    def artist_id(self, artist_id):
        """
        Sets the artist_id of this Track.
        

        :param artist_id: The artist_id of this Track.
        :type: float
        """

        self._artist_id = artist_id

    @property
    def album_id(self):
        """
        Gets the album_id of this Track.
        

        :return: The album_id of this Track.
        :rtype: float
        """
        return self._album_id

    @album_id.setter
    def album_id(self, album_id):
        """
        Sets the album_id of this Track.
        

        :param album_id: The album_id of this Track.
        :type: float
        """

        self._album_id = album_id

    @property
    def artist_mbid(self):
        """
        Gets the artist_mbid of this Track.
        

        :return: The artist_mbid of this Track.
        :rtype: str
        """
        return self._artist_mbid

    @artist_mbid.setter
    def artist_mbid(self, artist_mbid):
        """
        Sets the artist_mbid of this Track.
        

        :param artist_mbid: The artist_mbid of this Track.
        :type: str
        """

        self._artist_mbid = artist_mbid

    @property
    def secondary_genres(self):
        """
        Gets the secondary_genres of this Track.


        :return: The secondary_genres of this Track.
        :rtype: TrackSecondaryGenres
        """
        return self._secondary_genres

    @secondary_genres.setter
    def secondary_genres(self, secondary_genres):
        """
        Sets the secondary_genres of this Track.


        :param secondary_genres: The secondary_genres of this Track.
        :type: TrackSecondaryGenres
        """

        self._secondary_genres = secondary_genres

    @property
    def commontrack_vanity_id(self):
        """
        Gets the commontrack_vanity_id of this Track.
        

        :return: The commontrack_vanity_id of this Track.
        :rtype: str
        """
        return self._commontrack_vanity_id

    @commontrack_vanity_id.setter
    def commontrack_vanity_id(self, commontrack_vanity_id):
        """
        Sets the commontrack_vanity_id of this Track.
        

        :param commontrack_vanity_id: The commontrack_vanity_id of this Track.
        :type: str
        """

        self._commontrack_vanity_id = commontrack_vanity_id

    @property
    def track_id(self):
        """
        Gets the track_id of this Track.
        

        :return: The track_id of this Track.
        :rtype: float
        """
        return self._track_id

    @track_id.setter
    def track_id(self, track_id):
        """
        Sets the track_id of this Track.
        

        :param track_id: The track_id of this Track.
        :type: float
        """

        self._track_id = track_id

    @property
    def track_xboxmusic_id(self):
        """
        Gets the track_xboxmusic_id of this Track.
        

        :return: The track_xboxmusic_id of this Track.
        :rtype: str
        """
        return self._track_xboxmusic_id

    @track_xboxmusic_id.setter
    def track_xboxmusic_id(self, track_xboxmusic_id):
        """
        Sets the track_xboxmusic_id of this Track.
        

        :param track_xboxmusic_id: The track_xboxmusic_id of this Track.
        :type: str
        """

        self._track_xboxmusic_id = track_xboxmusic_id

    @property
    def primary_genres(self):
        """
        Gets the primary_genres of this Track.


        :return: The primary_genres of this Track.
        :rtype: TrackPrimaryGenres
        """
        return self._primary_genres

    @primary_genres.setter
    def primary_genres(self, primary_genres):
        """
        Sets the primary_genres of this Track.


        :param primary_genres: The primary_genres of this Track.
        :type: TrackPrimaryGenres
        """

        self._primary_genres = primary_genres

    @property
    def track_length(self):
        """
        Gets the track_length of this Track.
        

        :return: The track_length of this Track.
        :rtype: float
        """
        return self._track_length

    @track_length.setter
    def track_length(self, track_length):
        """
        Sets the track_length of this Track.
        

        :param track_length: The track_length of this Track.
        :type: float
        """

        self._track_length = track_length

    @property
    def track_mbid(self):
        """
        Gets the track_mbid of this Track.
        

        :return: The track_mbid of this Track.
        :rtype: str
        """
        return self._track_mbid

    @track_mbid.setter
    def track_mbid(self, track_mbid):
        """
        Sets the track_mbid of this Track.
        

        :param track_mbid: The track_mbid of this Track.
        :type: str
        """

        self._track_mbid = track_mbid

    @property
    def commontrack_id(self):
        """
        Gets the commontrack_id of this Track.
        

        :return: The commontrack_id of this Track.
        :rtype: float
        """
        return self._commontrack_id

    @commontrack_id.setter
    def commontrack_id(self, commontrack_id):
        """
        Sets the commontrack_id of this Track.
        

        :param commontrack_id: The commontrack_id of this Track.
        :type: float
        """

        self._commontrack_id = commontrack_id

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
