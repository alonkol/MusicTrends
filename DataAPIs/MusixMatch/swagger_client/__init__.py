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

# import models into sdk package
from .models.album import Album
from .models.album_primary_genres import AlbumPrimaryGenres
from .models.album_primary_genres_music_genre import AlbumPrimaryGenresMusicGenre
from .models.album_primary_genres_music_genre_list import AlbumPrimaryGenresMusicGenreList
from .models.artist import Artist
from .models.artist_artist_alias_list import ArtistArtistAliasList
from .models.artist_artist_credits import ArtistArtistCredits
from .models.artist_artist_name_translation import ArtistArtistNameTranslation
from .models.artist_artist_name_translation_list import ArtistArtistNameTranslationList
from .models.artist_primary_genres import ArtistPrimaryGenres
from .models.artist_primary_genres_music_genre import ArtistPrimaryGenresMusicGenre
from .models.artist_primary_genres_music_genre_list import ArtistPrimaryGenresMusicGenreList
from .models.artist_secondary_genres import ArtistSecondaryGenres
from .models.inline_response_200 import InlineResponse200
from .models.inline_response_200_1 import InlineResponse2001
from .models.inline_response_200_10 import InlineResponse20010
from .models.inline_response_200_10_message import InlineResponse20010Message
from .models.inline_response_200_10_message_body import InlineResponse20010MessageBody
from .models.inline_response_200_1_message import InlineResponse2001Message
from .models.inline_response_200_1_message_body import InlineResponse2001MessageBody
from .models.inline_response_200_1_message_header import InlineResponse2001MessageHeader
from .models.inline_response_200_2 import InlineResponse2002
from .models.inline_response_200_2_message import InlineResponse2002Message
from .models.inline_response_200_2_message_body import InlineResponse2002MessageBody
from .models.inline_response_200_2_message_header import InlineResponse2002MessageHeader
from .models.inline_response_200_3 import InlineResponse2003
from .models.inline_response_200_3_message import InlineResponse2003Message
from .models.inline_response_200_3_message_body import InlineResponse2003MessageBody
from .models.inline_response_200_4 import InlineResponse2004
from .models.inline_response_200_4_message import InlineResponse2004Message
from .models.inline_response_200_4_message_body import InlineResponse2004MessageBody
from .models.inline_response_200_5 import InlineResponse2005
from .models.inline_response_200_5_message import InlineResponse2005Message
from .models.inline_response_200_5_message_header import InlineResponse2005MessageHeader
from .models.inline_response_200_6 import InlineResponse2006
from .models.inline_response_200_6_message import InlineResponse2006Message
from .models.inline_response_200_6_message_body import InlineResponse2006MessageBody
from .models.inline_response_200_6_message_body_track_list import InlineResponse2006MessageBodyTrackList
from .models.inline_response_200_7 import InlineResponse2007
from .models.inline_response_200_7_message import InlineResponse2007Message
from .models.inline_response_200_7_message_body import InlineResponse2007MessageBody
from .models.inline_response_200_8 import InlineResponse2008
from .models.inline_response_200_8_message import InlineResponse2008Message
from .models.inline_response_200_8_message_body import InlineResponse2008MessageBody
from .models.inline_response_200_9 import InlineResponse2009
from .models.inline_response_200_9_message import InlineResponse2009Message
from .models.inline_response_200_message import InlineResponse200Message
from .models.inline_response_200_message_body import InlineResponse200MessageBody
from .models.inline_response_200_message_header import InlineResponse200MessageHeader
from .models.lyrics import Lyrics
from .models.snippet import Snippet
from .models.subtitle import Subtitle
from .models.track import Track
from .models.track_primary_genres import TrackPrimaryGenres
from .models.track_primary_genres_music_genre import TrackPrimaryGenresMusicGenre
from .models.track_primary_genres_music_genre_list import TrackPrimaryGenresMusicGenreList
from .models.track_secondary_genres import TrackSecondaryGenres
from .models.track_secondary_genres_music_genre import TrackSecondaryGenresMusicGenre
from .models.track_secondary_genres_music_genre_list import TrackSecondaryGenresMusicGenreList

# import apis into sdk package
from .apis.album_api import AlbumApi
from .apis.artist_api import ArtistApi
from .apis.lyrics_api import LyricsApi
from .apis.snippet_api import SnippetApi
from .apis.subtitle_api import SubtitleApi
from .apis.track_api import TrackApi

# import ApiClient
from .api_client import ApiClient

from .configuration import Configuration

configuration = Configuration()
