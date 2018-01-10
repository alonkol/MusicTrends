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


class Album(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, album_coverart_500x500=None, restricted=None, artist_id=None, album_name=None, album_coverart_800x800=None, album_copyright=None, album_coverart_350x350=None, artist_name=None, primary_genres=None, album_id=None, album_rating=None, album_pline=None, album_track_count=None, album_release_type=None, album_release_date=None, album_edit_url=None, updated_time=None, secondary_genres=None, album_mbid=None, album_vanity_id=None, album_coverart_100x100=None, album_label=None):
        """
        Album - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'album_coverart_500x500': 'str',
            'restricted': 'float',
            'artist_id': 'float',
            'album_name': 'str',
            'album_coverart_800x800': 'str',
            'album_copyright': 'str',
            'album_coverart_350x350': 'str',
            'artist_name': 'str',
            'primary_genres': 'AlbumPrimaryGenres',
            'album_id': 'float',
            'album_rating': 'float',
            'album_pline': 'str',
            'album_track_count': 'float',
            'album_release_type': 'str',
            'album_release_date': 'str',
            'album_edit_url': 'str',
            'updated_time': 'str',
            'secondary_genres': 'ArtistSecondaryGenres',
            'album_mbid': 'str',
            'album_vanity_id': 'str',
            'album_coverart_100x100': 'str',
            'album_label': 'str'
        }

        self.attribute_map = {
            'album_coverart_500x500': 'album_coverart_500x500',
            'restricted': 'restricted',
            'artist_id': 'artist_id',
            'album_name': 'album_name',
            'album_coverart_800x800': 'album_coverart_800x800',
            'album_copyright': 'album_copyright',
            'album_coverart_350x350': 'album_coverart_350x350',
            'artist_name': 'artist_name',
            'primary_genres': 'primary_genres',
            'album_id': 'album_id',
            'album_rating': 'album_rating',
            'album_pline': 'album_pline',
            'album_track_count': 'album_track_count',
            'album_release_type': 'album_release_type',
            'album_release_date': 'album_release_date',
            'album_edit_url': 'album_edit_url',
            'updated_time': 'updated_time',
            'secondary_genres': 'secondary_genres',
            'album_mbid': 'album_mbid',
            'album_vanity_id': 'album_vanity_id',
            'album_coverart_100x100': 'album_coverart_100x100',
            'album_label': 'album_label'
        }

        self._album_coverart_500x500 = album_coverart_500x500
        self._restricted = restricted
        self._artist_id = artist_id
        self._album_name = album_name
        self._album_coverart_800x800 = album_coverart_800x800
        self._album_copyright = album_copyright
        self._album_coverart_350x350 = album_coverart_350x350
        self._artist_name = artist_name
        self._primary_genres = primary_genres
        self._album_id = album_id
        self._album_rating = album_rating
        self._album_pline = album_pline
        self._album_track_count = album_track_count
        self._album_release_type = album_release_type
        self._album_release_date = album_release_date
        self._album_edit_url = album_edit_url
        self._updated_time = updated_time
        self._secondary_genres = secondary_genres
        self._album_mbid = album_mbid
        self._album_vanity_id = album_vanity_id
        self._album_coverart_100x100 = album_coverart_100x100
        self._album_label = album_label

    @property
    def album_coverart_500x500(self):
        """
        Gets the album_coverart_500x500 of this Album.
        

        :return: The album_coverart_500x500 of this Album.
        :rtype: str
        """
        return self._album_coverart_500x500

    @album_coverart_500x500.setter
    def album_coverart_500x500(self, album_coverart_500x500):
        """
        Sets the album_coverart_500x500 of this Album.
        

        :param album_coverart_500x500: The album_coverart_500x500 of this Album.
        :type: str
        """

        self._album_coverart_500x500 = album_coverart_500x500

    @property
    def restricted(self):
        """
        Gets the restricted of this Album.
        

        :return: The restricted of this Album.
        :rtype: float
        """
        return self._restricted

    @restricted.setter
    def restricted(self, restricted):
        """
        Sets the restricted of this Album.
        

        :param restricted: The restricted of this Album.
        :type: float
        """

        self._restricted = restricted

    @property
    def artist_id(self):
        """
        Gets the artist_id of this Album.
        

        :return: The artist_id of this Album.
        :rtype: float
        """
        return self._artist_id

    @artist_id.setter
    def artist_id(self, artist_id):
        """
        Sets the artist_id of this Album.
        

        :param artist_id: The artist_id of this Album.
        :type: float
        """

        self._artist_id = artist_id

    @property
    def album_name(self):
        """
        Gets the album_name of this Album.
        

        :return: The album_name of this Album.
        :rtype: str
        """
        return self._album_name

    @album_name.setter
    def album_name(self, album_name):
        """
        Sets the album_name of this Album.
        

        :param album_name: The album_name of this Album.
        :type: str
        """

        self._album_name = album_name

    @property
    def album_coverart_800x800(self):
        """
        Gets the album_coverart_800x800 of this Album.
        

        :return: The album_coverart_800x800 of this Album.
        :rtype: str
        """
        return self._album_coverart_800x800

    @album_coverart_800x800.setter
    def album_coverart_800x800(self, album_coverart_800x800):
        """
        Sets the album_coverart_800x800 of this Album.
        

        :param album_coverart_800x800: The album_coverart_800x800 of this Album.
        :type: str
        """

        self._album_coverart_800x800 = album_coverart_800x800

    @property
    def album_copyright(self):
        """
        Gets the album_copyright of this Album.
        

        :return: The album_copyright of this Album.
        :rtype: str
        """
        return self._album_copyright

    @album_copyright.setter
    def album_copyright(self, album_copyright):
        """
        Sets the album_copyright of this Album.
        

        :param album_copyright: The album_copyright of this Album.
        :type: str
        """

        self._album_copyright = album_copyright

    @property
    def album_coverart_350x350(self):
        """
        Gets the album_coverart_350x350 of this Album.
        

        :return: The album_coverart_350x350 of this Album.
        :rtype: str
        """
        return self._album_coverart_350x350

    @album_coverart_350x350.setter
    def album_coverart_350x350(self, album_coverart_350x350):
        """
        Sets the album_coverart_350x350 of this Album.
        

        :param album_coverart_350x350: The album_coverart_350x350 of this Album.
        :type: str
        """

        self._album_coverart_350x350 = album_coverart_350x350

    @property
    def artist_name(self):
        """
        Gets the artist_name of this Album.
        

        :return: The artist_name of this Album.
        :rtype: str
        """
        return self._artist_name

    @artist_name.setter
    def artist_name(self, artist_name):
        """
        Sets the artist_name of this Album.
        

        :param artist_name: The artist_name of this Album.
        :type: str
        """

        self._artist_name = artist_name

    @property
    def primary_genres(self):
        """
        Gets the primary_genres of this Album.


        :return: The primary_genres of this Album.
        :rtype: AlbumPrimaryGenres
        """
        return self._primary_genres

    @primary_genres.setter
    def primary_genres(self, primary_genres):
        """
        Sets the primary_genres of this Album.


        :param primary_genres: The primary_genres of this Album.
        :type: AlbumPrimaryGenres
        """

        self._primary_genres = primary_genres

    @property
    def album_id(self):
        """
        Gets the album_id of this Album.
        

        :return: The album_id of this Album.
        :rtype: float
        """
        return self._album_id

    @album_id.setter
    def album_id(self, album_id):
        """
        Sets the album_id of this Album.
        

        :param album_id: The album_id of this Album.
        :type: float
        """

        self._album_id = album_id

    @property
    def album_rating(self):
        """
        Gets the album_rating of this Album.
        

        :return: The album_rating of this Album.
        :rtype: float
        """
        return self._album_rating

    @album_rating.setter
    def album_rating(self, album_rating):
        """
        Sets the album_rating of this Album.
        

        :param album_rating: The album_rating of this Album.
        :type: float
        """

        self._album_rating = album_rating

    @property
    def album_pline(self):
        """
        Gets the album_pline of this Album.
        

        :return: The album_pline of this Album.
        :rtype: str
        """
        return self._album_pline

    @album_pline.setter
    def album_pline(self, album_pline):
        """
        Sets the album_pline of this Album.
        

        :param album_pline: The album_pline of this Album.
        :type: str
        """

        self._album_pline = album_pline

    @property
    def album_track_count(self):
        """
        Gets the album_track_count of this Album.
        

        :return: The album_track_count of this Album.
        :rtype: float
        """
        return self._album_track_count

    @album_track_count.setter
    def album_track_count(self, album_track_count):
        """
        Sets the album_track_count of this Album.
        

        :param album_track_count: The album_track_count of this Album.
        :type: float
        """

        self._album_track_count = album_track_count

    @property
    def album_release_type(self):
        """
        Gets the album_release_type of this Album.
        

        :return: The album_release_type of this Album.
        :rtype: str
        """
        return self._album_release_type

    @album_release_type.setter
    def album_release_type(self, album_release_type):
        """
        Sets the album_release_type of this Album.
        

        :param album_release_type: The album_release_type of this Album.
        :type: str
        """

        self._album_release_type = album_release_type

    @property
    def album_release_date(self):
        """
        Gets the album_release_date of this Album.
        

        :return: The album_release_date of this Album.
        :rtype: str
        """
        return self._album_release_date

    @album_release_date.setter
    def album_release_date(self, album_release_date):
        """
        Sets the album_release_date of this Album.
        

        :param album_release_date: The album_release_date of this Album.
        :type: str
        """

        self._album_release_date = album_release_date

    @property
    def album_edit_url(self):
        """
        Gets the album_edit_url of this Album.
        

        :return: The album_edit_url of this Album.
        :rtype: str
        """
        return self._album_edit_url

    @album_edit_url.setter
    def album_edit_url(self, album_edit_url):
        """
        Sets the album_edit_url of this Album.
        

        :param album_edit_url: The album_edit_url of this Album.
        :type: str
        """

        self._album_edit_url = album_edit_url

    @property
    def updated_time(self):
        """
        Gets the updated_time of this Album.
        

        :return: The updated_time of this Album.
        :rtype: str
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """
        Sets the updated_time of this Album.
        

        :param updated_time: The updated_time of this Album.
        :type: str
        """

        self._updated_time = updated_time

    @property
    def secondary_genres(self):
        """
        Gets the secondary_genres of this Album.


        :return: The secondary_genres of this Album.
        :rtype: ArtistSecondaryGenres
        """
        return self._secondary_genres

    @secondary_genres.setter
    def secondary_genres(self, secondary_genres):
        """
        Sets the secondary_genres of this Album.


        :param secondary_genres: The secondary_genres of this Album.
        :type: ArtistSecondaryGenres
        """

        self._secondary_genres = secondary_genres

    @property
    def album_mbid(self):
        """
        Gets the album_mbid of this Album.
        

        :return: The album_mbid of this Album.
        :rtype: str
        """
        return self._album_mbid

    @album_mbid.setter
    def album_mbid(self, album_mbid):
        """
        Sets the album_mbid of this Album.
        

        :param album_mbid: The album_mbid of this Album.
        :type: str
        """

        self._album_mbid = album_mbid

    @property
    def album_vanity_id(self):
        """
        Gets the album_vanity_id of this Album.
        

        :return: The album_vanity_id of this Album.
        :rtype: str
        """
        return self._album_vanity_id

    @album_vanity_id.setter
    def album_vanity_id(self, album_vanity_id):
        """
        Sets the album_vanity_id of this Album.
        

        :param album_vanity_id: The album_vanity_id of this Album.
        :type: str
        """

        self._album_vanity_id = album_vanity_id

    @property
    def album_coverart_100x100(self):
        """
        Gets the album_coverart_100x100 of this Album.
        

        :return: The album_coverart_100x100 of this Album.
        :rtype: str
        """
        return self._album_coverart_100x100

    @album_coverart_100x100.setter
    def album_coverart_100x100(self, album_coverart_100x100):
        """
        Sets the album_coverart_100x100 of this Album.
        

        :param album_coverart_100x100: The album_coverart_100x100 of this Album.
        :type: str
        """

        self._album_coverart_100x100 = album_coverart_100x100

    @property
    def album_label(self):
        """
        Gets the album_label of this Album.
        

        :return: The album_label of this Album.
        :rtype: str
        """
        return self._album_label

    @album_label.setter
    def album_label(self, album_label):
        """
        Sets the album_label of this Album.
        

        :param album_label: The album_label of this Album.
        :type: str
        """

        self._album_label = album_label

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
