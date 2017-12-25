from googleapiclient.discovery import build
from Server import config

DEVELOPER_KEY = "AIzaSyBmsB_Jle7kBYJrrGJAkkKO-PgKc0HSWfI"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def youtube_search(queryString, maxResults):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    search_response = youtube.search().list(
        q=queryString,
        part="id,snippet",
        maxResults=maxResults
    ).execute()

    videos = []

    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videos.append("%s (%s)" % (search_result["snippet"]["title"],
                                       search_result["id"]["videoId"]))

    return videos


if __name__ == "__main__":

    # TODO: fill this list with data from DB
    statement = "SELECT artist_name, song_name " \
                "FROM Songs, Artists, SongsToArtists " \
                "WHERE Songs.song_id = SongsToArtists.song_id " \
                "AND Artists.artist_id = SongsToArtists.artist_id;"
    config.unsafe_cursor.execute(statement)
    couples = config.unsafe_cursor.fetchall()

    for couple in couples:
        query = couple["artist_name"] + " " + couple["song_name"]

        # TODO: get all necessary data for songs:
        # - Likes
        # - Dislikes
        # - Top Comments (text, author, likes, dislikes) into Comments table
        # Endpoint to get vid's comments: https://developers.google.com/youtube/v3/docs/commentThreads/list
        # Getting all of the comments might be a HEAVY operation. Be careful
        res = youtube_search(query, maxResults=1)

        # TODO: enrich song table with data
        # statement = "UPDATE songs " \
        #             "SET column1 = value1, column2 = value2 " \
        #             "WHERE condition;"

        # TODO: populate comments table
        # statement = "INSERT INTO comments " \
        #             " VALUES () " \
