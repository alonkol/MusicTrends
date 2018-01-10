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


class Lyrics(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, instrumental=None, pixel_tracking_url=None, publisher_list=None, lyrics_language_description=None, restricted=None, updated_time=None, explicit=None, lyrics_copyright=None, html_tracking_url=None, lyrics_language=None, script_tracking_url=None, verified=None, lyrics_body=None, lyrics_id=None, writer_list=None, can_edit=None, action_requested=None, locked=None):
        """
        Lyrics - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'instrumental': 'float',
            'pixel_tracking_url': 'str',
            'publisher_list': 'list[str]',
            'lyrics_language_description': 'str',
            'restricted': 'float',
            'updated_time': 'str',
            'explicit': 'float',
            'lyrics_copyright': 'str',
            'html_tracking_url': 'str',
            'lyrics_language': 'str',
            'script_tracking_url': 'str',
            'verified': 'float',
            'lyrics_body': 'str',
            'lyrics_id': 'float',
            'writer_list': 'list[str]',
            'can_edit': 'float',
            'action_requested': 'str',
            'locked': 'float'
        }

        self.attribute_map = {
            'instrumental': 'instrumental',
            'pixel_tracking_url': 'pixel_tracking_url',
            'publisher_list': 'publisher_list',
            'lyrics_language_description': 'lyrics_language_description',
            'restricted': 'restricted',
            'updated_time': 'updated_time',
            'explicit': 'explicit',
            'lyrics_copyright': 'lyrics_copyright',
            'html_tracking_url': 'html_tracking_url',
            'lyrics_language': 'lyrics_language',
            'script_tracking_url': 'script_tracking_url',
            'verified': 'verified',
            'lyrics_body': 'lyrics_body',
            'lyrics_id': 'lyrics_id',
            'writer_list': 'writer_list',
            'can_edit': 'can_edit',
            'action_requested': 'action_requested',
            'locked': 'locked'
        }

        self._instrumental = instrumental
        self._pixel_tracking_url = pixel_tracking_url
        self._publisher_list = publisher_list
        self._lyrics_language_description = lyrics_language_description
        self._restricted = restricted
        self._updated_time = updated_time
        self._explicit = explicit
        self._lyrics_copyright = lyrics_copyright
        self._html_tracking_url = html_tracking_url
        self._lyrics_language = lyrics_language
        self._script_tracking_url = script_tracking_url
        self._verified = verified
        self._lyrics_body = lyrics_body
        self._lyrics_id = lyrics_id
        self._writer_list = writer_list
        self._can_edit = can_edit
        self._action_requested = action_requested
        self._locked = locked

    @property
    def instrumental(self):
        """
        Gets the instrumental of this Lyrics.
        

        :return: The instrumental of this Lyrics.
        :rtype: float
        """
        return self._instrumental

    @instrumental.setter
    def instrumental(self, instrumental):
        """
        Sets the instrumental of this Lyrics.
        

        :param instrumental: The instrumental of this Lyrics.
        :type: float
        """

        self._instrumental = instrumental

    @property
    def pixel_tracking_url(self):
        """
        Gets the pixel_tracking_url of this Lyrics.
        

        :return: The pixel_tracking_url of this Lyrics.
        :rtype: str
        """
        return self._pixel_tracking_url

    @pixel_tracking_url.setter
    def pixel_tracking_url(self, pixel_tracking_url):
        """
        Sets the pixel_tracking_url of this Lyrics.
        

        :param pixel_tracking_url: The pixel_tracking_url of this Lyrics.
        :type: str
        """

        self._pixel_tracking_url = pixel_tracking_url

    @property
    def publisher_list(self):
        """
        Gets the publisher_list of this Lyrics.


        :return: The publisher_list of this Lyrics.
        :rtype: list[str]
        """
        return self._publisher_list

    @publisher_list.setter
    def publisher_list(self, publisher_list):
        """
        Sets the publisher_list of this Lyrics.


        :param publisher_list: The publisher_list of this Lyrics.
        :type: list[str]
        """

        self._publisher_list = publisher_list

    @property
    def lyrics_language_description(self):
        """
        Gets the lyrics_language_description of this Lyrics.
        

        :return: The lyrics_language_description of this Lyrics.
        :rtype: str
        """
        return self._lyrics_language_description

    @lyrics_language_description.setter
    def lyrics_language_description(self, lyrics_language_description):
        """
        Sets the lyrics_language_description of this Lyrics.
        

        :param lyrics_language_description: The lyrics_language_description of this Lyrics.
        :type: str
        """

        self._lyrics_language_description = lyrics_language_description

    @property
    def restricted(self):
        """
        Gets the restricted of this Lyrics.
        

        :return: The restricted of this Lyrics.
        :rtype: float
        """
        return self._restricted

    @restricted.setter
    def restricted(self, restricted):
        """
        Sets the restricted of this Lyrics.
        

        :param restricted: The restricted of this Lyrics.
        :type: float
        """

        self._restricted = restricted

    @property
    def updated_time(self):
        """
        Gets the updated_time of this Lyrics.
        

        :return: The updated_time of this Lyrics.
        :rtype: str
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """
        Sets the updated_time of this Lyrics.
        

        :param updated_time: The updated_time of this Lyrics.
        :type: str
        """

        self._updated_time = updated_time

    @property
    def explicit(self):
        """
        Gets the explicit of this Lyrics.
        

        :return: The explicit of this Lyrics.
        :rtype: float
        """
        return self._explicit

    @explicit.setter
    def explicit(self, explicit):
        """
        Sets the explicit of this Lyrics.
        

        :param explicit: The explicit of this Lyrics.
        :type: float
        """

        self._explicit = explicit

    @property
    def lyrics_copyright(self):
        """
        Gets the lyrics_copyright of this Lyrics.
        

        :return: The lyrics_copyright of this Lyrics.
        :rtype: str
        """
        return self._lyrics_copyright

    @lyrics_copyright.setter
    def lyrics_copyright(self, lyrics_copyright):
        """
        Sets the lyrics_copyright of this Lyrics.
        

        :param lyrics_copyright: The lyrics_copyright of this Lyrics.
        :type: str
        """

        self._lyrics_copyright = lyrics_copyright

    @property
    def html_tracking_url(self):
        """
        Gets the html_tracking_url of this Lyrics.
        

        :return: The html_tracking_url of this Lyrics.
        :rtype: str
        """
        return self._html_tracking_url

    @html_tracking_url.setter
    def html_tracking_url(self, html_tracking_url):
        """
        Sets the html_tracking_url of this Lyrics.
        

        :param html_tracking_url: The html_tracking_url of this Lyrics.
        :type: str
        """

        self._html_tracking_url = html_tracking_url

    @property
    def lyrics_language(self):
        """
        Gets the lyrics_language of this Lyrics.
        

        :return: The lyrics_language of this Lyrics.
        :rtype: str
        """
        return self._lyrics_language

    @lyrics_language.setter
    def lyrics_language(self, lyrics_language):
        """
        Sets the lyrics_language of this Lyrics.
        

        :param lyrics_language: The lyrics_language of this Lyrics.
        :type: str
        """

        self._lyrics_language = lyrics_language

    @property
    def script_tracking_url(self):
        """
        Gets the script_tracking_url of this Lyrics.
        

        :return: The script_tracking_url of this Lyrics.
        :rtype: str
        """
        return self._script_tracking_url

    @script_tracking_url.setter
    def script_tracking_url(self, script_tracking_url):
        """
        Sets the script_tracking_url of this Lyrics.
        

        :param script_tracking_url: The script_tracking_url of this Lyrics.
        :type: str
        """

        self._script_tracking_url = script_tracking_url

    @property
    def verified(self):
        """
        Gets the verified of this Lyrics.
        

        :return: The verified of this Lyrics.
        :rtype: float
        """
        return self._verified

    @verified.setter
    def verified(self, verified):
        """
        Sets the verified of this Lyrics.
        

        :param verified: The verified of this Lyrics.
        :type: float
        """

        self._verified = verified

    @property
    def lyrics_body(self):
        """
        Gets the lyrics_body of this Lyrics.
        

        :return: The lyrics_body of this Lyrics.
        :rtype: str
        """
        return self._lyrics_body

    @lyrics_body.setter
    def lyrics_body(self, lyrics_body):
        """
        Sets the lyrics_body of this Lyrics.
        

        :param lyrics_body: The lyrics_body of this Lyrics.
        :type: str
        """

        self._lyrics_body = lyrics_body

    @property
    def lyrics_id(self):
        """
        Gets the lyrics_id of this Lyrics.
        

        :return: The lyrics_id of this Lyrics.
        :rtype: float
        """
        return self._lyrics_id

    @lyrics_id.setter
    def lyrics_id(self, lyrics_id):
        """
        Sets the lyrics_id of this Lyrics.
        

        :param lyrics_id: The lyrics_id of this Lyrics.
        :type: float
        """

        self._lyrics_id = lyrics_id

    @property
    def writer_list(self):
        """
        Gets the writer_list of this Lyrics.


        :return: The writer_list of this Lyrics.
        :rtype: list[str]
        """
        return self._writer_list

    @writer_list.setter
    def writer_list(self, writer_list):
        """
        Sets the writer_list of this Lyrics.


        :param writer_list: The writer_list of this Lyrics.
        :type: list[str]
        """

        self._writer_list = writer_list

    @property
    def can_edit(self):
        """
        Gets the can_edit of this Lyrics.
        

        :return: The can_edit of this Lyrics.
        :rtype: float
        """
        return self._can_edit

    @can_edit.setter
    def can_edit(self, can_edit):
        """
        Sets the can_edit of this Lyrics.
        

        :param can_edit: The can_edit of this Lyrics.
        :type: float
        """

        self._can_edit = can_edit

    @property
    def action_requested(self):
        """
        Gets the action_requested of this Lyrics.
        

        :return: The action_requested of this Lyrics.
        :rtype: str
        """
        return self._action_requested

    @action_requested.setter
    def action_requested(self, action_requested):
        """
        Sets the action_requested of this Lyrics.
        

        :param action_requested: The action_requested of this Lyrics.
        :type: str
        """

        self._action_requested = action_requested

    @property
    def locked(self):
        """
        Gets the locked of this Lyrics.
        

        :return: The locked of this Lyrics.
        :rtype: float
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """
        Sets the locked of this Lyrics.
        

        :param locked: The locked of this Lyrics.
        :type: float
        """

        self._locked = locked

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
