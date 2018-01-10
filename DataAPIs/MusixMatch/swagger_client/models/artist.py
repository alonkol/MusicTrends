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


class Artist(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, artist_credits=None, artist_mbid=None, artist_name=None, secondary_genres=None, artist_alias_list=None, artist_vanity_id=None, restricted=None, artist_country=None, artist_comment=None, artist_name_translation_list=None, artist_edit_url=None, artist_share_url=None, artist_id=None, updated_time=None, managed=None, primary_genres=None, artist_twitter_url=None, artist_rating=None):
        """
        Artist - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'artist_credits': 'ArtistArtistCredits',
            'artist_mbid': 'str',
            'artist_name': 'str',
            'secondary_genres': 'ArtistSecondaryGenres',
            'artist_alias_list': 'list[ArtistArtistAliasList]',
            'artist_vanity_id': 'str',
            'restricted': 'float',
            'artist_country': 'str',
            'artist_comment': 'str',
            'artist_name_translation_list': 'list[ArtistArtistNameTranslationList]',
            'artist_edit_url': 'str',
            'artist_share_url': 'str',
            'artist_id': 'float',
            'updated_time': 'str',
            'managed': 'float',
            'primary_genres': 'ArtistPrimaryGenres',
            'artist_twitter_url': 'str',
            'artist_rating': 'float'
        }

        self.attribute_map = {
            'artist_credits': 'artist_credits',
            'artist_mbid': 'artist_mbid',
            'artist_name': 'artist_name',
            'secondary_genres': 'secondary_genres',
            'artist_alias_list': 'artist_alias_list',
            'artist_vanity_id': 'artist_vanity_id',
            'restricted': 'restricted',
            'artist_country': 'artist_country',
            'artist_comment': 'artist_comment',
            'artist_name_translation_list': 'artist_name_translation_list',
            'artist_edit_url': 'artist_edit_url',
            'artist_share_url': 'artist_share_url',
            'artist_id': 'artist_id',
            'updated_time': 'updated_time',
            'managed': 'managed',
            'primary_genres': 'primary_genres',
            'artist_twitter_url': 'artist_twitter_url',
            'artist_rating': 'artist_rating'
        }

        self._artist_credits = artist_credits
        self._artist_mbid = artist_mbid
        self._artist_name = artist_name
        self._secondary_genres = secondary_genres
        self._artist_alias_list = artist_alias_list
        self._artist_vanity_id = artist_vanity_id
        self._restricted = restricted
        self._artist_country = artist_country
        self._artist_comment = artist_comment
        self._artist_name_translation_list = artist_name_translation_list
        self._artist_edit_url = artist_edit_url
        self._artist_share_url = artist_share_url
        self._artist_id = artist_id
        self._updated_time = updated_time
        self._managed = managed
        self._primary_genres = primary_genres
        self._artist_twitter_url = artist_twitter_url
        self._artist_rating = artist_rating

    @property
    def artist_credits(self):
        """
        Gets the artist_credits of this Artist.


        :return: The artist_credits of this Artist.
        :rtype: ArtistArtistCredits
        """
        return self._artist_credits

    @artist_credits.setter
    def artist_credits(self, artist_credits):
        """
        Sets the artist_credits of this Artist.


        :param artist_credits: The artist_credits of this Artist.
        :type: ArtistArtistCredits
        """

        self._artist_credits = artist_credits

    @property
    def artist_mbid(self):
        """
        Gets the artist_mbid of this Artist.
        

        :return: The artist_mbid of this Artist.
        :rtype: str
        """
        return self._artist_mbid

    @artist_mbid.setter
    def artist_mbid(self, artist_mbid):
        """
        Sets the artist_mbid of this Artist.
        

        :param artist_mbid: The artist_mbid of this Artist.
        :type: str
        """

        self._artist_mbid = artist_mbid

    @property
    def artist_name(self):
        """
        Gets the artist_name of this Artist.
        

        :return: The artist_name of this Artist.
        :rtype: str
        """
        return self._artist_name

    @artist_name.setter
    def artist_name(self, artist_name):
        """
        Sets the artist_name of this Artist.
        

        :param artist_name: The artist_name of this Artist.
        :type: str
        """

        self._artist_name = artist_name

    @property
    def secondary_genres(self):
        """
        Gets the secondary_genres of this Artist.


        :return: The secondary_genres of this Artist.
        :rtype: ArtistSecondaryGenres
        """
        return self._secondary_genres

    @secondary_genres.setter
    def secondary_genres(self, secondary_genres):
        """
        Sets the secondary_genres of this Artist.


        :param secondary_genres: The secondary_genres of this Artist.
        :type: ArtistSecondaryGenres
        """

        self._secondary_genres = secondary_genres

    @property
    def artist_alias_list(self):
        """
        Gets the artist_alias_list of this Artist.


        :return: The artist_alias_list of this Artist.
        :rtype: list[ArtistArtistAliasList]
        """
        return self._artist_alias_list

    @artist_alias_list.setter
    def artist_alias_list(self, artist_alias_list):
        """
        Sets the artist_alias_list of this Artist.


        :param artist_alias_list: The artist_alias_list of this Artist.
        :type: list[ArtistArtistAliasList]
        """

        self._artist_alias_list = artist_alias_list

    @property
    def artist_vanity_id(self):
        """
        Gets the artist_vanity_id of this Artist.
        

        :return: The artist_vanity_id of this Artist.
        :rtype: str
        """
        return self._artist_vanity_id

    @artist_vanity_id.setter
    def artist_vanity_id(self, artist_vanity_id):
        """
        Sets the artist_vanity_id of this Artist.
        

        :param artist_vanity_id: The artist_vanity_id of this Artist.
        :type: str
        """

        self._artist_vanity_id = artist_vanity_id

    @property
    def restricted(self):
        """
        Gets the restricted of this Artist.
        

        :return: The restricted of this Artist.
        :rtype: float
        """
        return self._restricted

    @restricted.setter
    def restricted(self, restricted):
        """
        Sets the restricted of this Artist.
        

        :param restricted: The restricted of this Artist.
        :type: float
        """

        self._restricted = restricted

    @property
    def artist_country(self):
        """
        Gets the artist_country of this Artist.
        

        :return: The artist_country of this Artist.
        :rtype: str
        """
        return self._artist_country

    @artist_country.setter
    def artist_country(self, artist_country):
        """
        Sets the artist_country of this Artist.
        

        :param artist_country: The artist_country of this Artist.
        :type: str
        """

        self._artist_country = artist_country

    @property
    def artist_comment(self):
        """
        Gets the artist_comment of this Artist.
        

        :return: The artist_comment of this Artist.
        :rtype: str
        """
        return self._artist_comment

    @artist_comment.setter
    def artist_comment(self, artist_comment):
        """
        Sets the artist_comment of this Artist.
        

        :param artist_comment: The artist_comment of this Artist.
        :type: str
        """

        self._artist_comment = artist_comment

    @property
    def artist_name_translation_list(self):
        """
        Gets the artist_name_translation_list of this Artist.


        :return: The artist_name_translation_list of this Artist.
        :rtype: list[ArtistArtistNameTranslationList]
        """
        return self._artist_name_translation_list

    @artist_name_translation_list.setter
    def artist_name_translation_list(self, artist_name_translation_list):
        """
        Sets the artist_name_translation_list of this Artist.


        :param artist_name_translation_list: The artist_name_translation_list of this Artist.
        :type: list[ArtistArtistNameTranslationList]
        """

        self._artist_name_translation_list = artist_name_translation_list

    @property
    def artist_edit_url(self):
        """
        Gets the artist_edit_url of this Artist.
        

        :return: The artist_edit_url of this Artist.
        :rtype: str
        """
        return self._artist_edit_url

    @artist_edit_url.setter
    def artist_edit_url(self, artist_edit_url):
        """
        Sets the artist_edit_url of this Artist.
        

        :param artist_edit_url: The artist_edit_url of this Artist.
        :type: str
        """

        self._artist_edit_url = artist_edit_url

    @property
    def artist_share_url(self):
        """
        Gets the artist_share_url of this Artist.
        

        :return: The artist_share_url of this Artist.
        :rtype: str
        """
        return self._artist_share_url

    @artist_share_url.setter
    def artist_share_url(self, artist_share_url):
        """
        Sets the artist_share_url of this Artist.
        

        :param artist_share_url: The artist_share_url of this Artist.
        :type: str
        """

        self._artist_share_url = artist_share_url

    @property
    def artist_id(self):
        """
        Gets the artist_id of this Artist.
        

        :return: The artist_id of this Artist.
        :rtype: float
        """
        return self._artist_id

    @artist_id.setter
    def artist_id(self, artist_id):
        """
        Sets the artist_id of this Artist.
        

        :param artist_id: The artist_id of this Artist.
        :type: float
        """

        self._artist_id = artist_id

    @property
    def updated_time(self):
        """
        Gets the updated_time of this Artist.
        

        :return: The updated_time of this Artist.
        :rtype: str
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """
        Sets the updated_time of this Artist.
        

        :param updated_time: The updated_time of this Artist.
        :type: str
        """

        self._updated_time = updated_time

    @property
    def managed(self):
        """
        Gets the managed of this Artist.
        

        :return: The managed of this Artist.
        :rtype: float
        """
        return self._managed

    @managed.setter
    def managed(self, managed):
        """
        Sets the managed of this Artist.
        

        :param managed: The managed of this Artist.
        :type: float
        """

        self._managed = managed

    @property
    def primary_genres(self):
        """
        Gets the primary_genres of this Artist.


        :return: The primary_genres of this Artist.
        :rtype: ArtistPrimaryGenres
        """
        return self._primary_genres

    @primary_genres.setter
    def primary_genres(self, primary_genres):
        """
        Sets the primary_genres of this Artist.


        :param primary_genres: The primary_genres of this Artist.
        :type: ArtistPrimaryGenres
        """

        self._primary_genres = primary_genres

    @property
    def artist_twitter_url(self):
        """
        Gets the artist_twitter_url of this Artist.
        

        :return: The artist_twitter_url of this Artist.
        :rtype: str
        """
        return self._artist_twitter_url

    @artist_twitter_url.setter
    def artist_twitter_url(self, artist_twitter_url):
        """
        Sets the artist_twitter_url of this Artist.
        

        :param artist_twitter_url: The artist_twitter_url of this Artist.
        :type: str
        """

        self._artist_twitter_url = artist_twitter_url

    @property
    def artist_rating(self):
        """
        Gets the artist_rating of this Artist.
        

        :return: The artist_rating of this Artist.
        :rtype: float
        """
        return self._artist_rating

    @artist_rating.setter
    def artist_rating(self, artist_rating):
        """
        Sets the artist_rating of this Artist.
        

        :param artist_rating: The artist_rating of this Artist.
        :type: float
        """

        self._artist_rating = artist_rating

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
