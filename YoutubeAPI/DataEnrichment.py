from googleapiclient.discovery import build
from Server import config

DEVELOPER_KEY = "AIzaSyBmsB_Jle7kBYJrrGJAkkKO-PgKc0HSWfI"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                developerKey=DEVELOPER_KEY)


def youtube_search(queryString):
    search_response = youtube.search().list(
        q=queryString,
        part="id,snippet",
        maxResults=1
    ).execute()

    items = search_response.get("items", [])

    if len(items) == 0 or items[0]["id"]["kind"] != "youtube#video":
        return None

    return items[0]


# Right now only gets one result
def GetStatisticsForVideo(videoId):
    search_response = youtube.video().list(
        id=videoId,
        part="statistics",
        maxResults=1
    ).execute()

    items = search_response.get("items", [])

    if len(items) == 0:
        return None

    return items[0]["statistics"]


# Right now gets first 20 comments.
# Can get up to 100 on a single page.
# Can get more with paging if necessary.
def GetCommentsForVideo(videoId):
    results = youtube.commentThreads().list(
        part="snippet",
        videoId=videoId,
        textFormat="plainText",
        maxResults=20
    ).execute()

    items = results.get("items", [])

    if len(items) == 0:
        return None

    return items

def GetAllSongsAndArtistsFromDB():
    statement = "SELECT artist_name, song_name " \
                "FROM Songs, Artists, SongToArtist " \
                "WHERE Songs.song_id = SongToArtist.song_id " \
                "AND Artists.artist_id = SongToArtist.artist_id;"
    config.unsafe_cursor.execute(statement)
    return config.unsafe_cursor.fetchall()


def GetAllVideoIdsFromDB():
    statement = "SELECT videoId" \
                "FROM Videos; "
    config.unsafe_cursor.execute(statement)
    results = config.unsafe_cursor.fetchall()

    return [result["videoId"] for result in results]


def PopulateVideos():
    couples = GetAllSongsAndArtistsFromDB()

    statement = "INSERT INTO videos " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"

    for couple in couples:
        query = couple["artist_name"] + " " + couple["song_name"]

        video = youtube_search(query)
        videoId = video["id"]["videoId"]
        publishedAt = video["snippet"]["publishedAt"]
        title = video["snippet"]["title"]

        # Populate video table
        # TODO: add videos table creation code to creation.sql
        s = GetStatisticsForVideo(videoId)
        inputDataList = [videoId, publishedAt, title, ["viewCount"], s["likeCount"],
                         s["dislikeCount"], s["favoriteCount"], s["commentCount"]]

        try:
            config.cursor.execute(statement, tuple(inputDataList))
            config.dbconnection.commit()
        except:
            config.dbconnection.rollback()


def PopulateComments():
    videoIds = GetAllVideoIdsFromDB()

    statement = "INSERT INTO comments " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s);"

    for videoId in videoIds:
        comments = GetCommentsForVideo(videoId)

        # Warning: this table will be large
        for comment in comments:
            c = comment["snippet"]["topLevelComment"]
            s = c["snippet"]
            inputDataList = [c["id"], s["videoId"], s["authorDisplayName"],
                             s["textDisplay"], s["viewerRating"],
                             s["likeCount"], s["publishedAt"]]

            try:
                config.cursor.execute(statement, tuple(inputDataList))
                config.dbconnection.commit()
            except:
                config.dbconnection.rollback()


if __name__ == "__main__":

    PopulateVideos()
    PopulateComments()


