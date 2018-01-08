from googleapiclient.discovery import build
from Server import config
from datetime import datetime

DEVELOPER_KEY = "AIzaSyBmsB_Jle7kBYJrrGJAkkKO-PgKc0HSWfI"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                developerKey=DEVELOPER_KEY)

cnt = [0]


def youtube_search(queryString):
    search_response = youtube.search().list(
        q=queryString,
        part="id,snippet",
        maxResults=1
    ).execute()

    items = search_response.get("items", [])

    if len(items) == 0 or items[0]["id"]["kind"] != "youtube#video":
        return None

    print("Got vid - #%d\n" % cnt[0])
    cnt[0] += 1

    return items[0]


# Right now only gets one result
def GetStatisticsForVideo(videoId):
    search_response = youtube.videos().list(
        id=videoId,
        part="statistics",
        maxResults=1
    ).execute()

    items = search_response.get("items", [])

    if len(items) == 0:
        return None

    keys = ["viewCount", "likeCount", "dislikeCount", "favoriteCount", "commentCount"]

    # Set key if does not exist, set value to null
    for key in keys:
        if key not in items[0]["statistics"]:
            items[0]["statistics"][key] = 0

    return items[0]["statistics"]


# Right now gets first 10 comments.
# Can get up to 100 on a single page.
# Can get more with paging if necessary.
def GetCommentsForVideo(videoId):
    results = youtube.commentThreads().list(
        part="snippet",
        videoId=videoId,
        textFormat="plainText",
        maxResults=10
    ).execute()

    items = results.get("items", [])

    if len(items) == 0:
        return None

    return items

def GetAllSongsAndArtistsFromDB():
    statement = "SELECT artistName, songName, songs.songID " \
                "FROM Songs, Artists, SongToArtist " \
                "WHERE Songs.songID = SongToArtist.songID " \
                "AND Artists.artistID = SongToArtist.artistID;"
    config.unsafe_cursor.execute(statement)
    return config.unsafe_cursor.fetchall()


def GetAllVideoIdsFromDB():
    statement = "SELECT videoID" \
                "FROM Videos; "
    config.unsafe_cursor.execute(statement)
    results = config.unsafe_cursor.fetchall()

    return [result["videoID"] for result in results]


def PopulateVideos():
    couples = GetAllSongsAndArtistsFromDB()

    statement = "INSERT INTO videos " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"

    for couple in couples:
        query = couple["artistName"] + " " + couple["songName"]
        songId = couple["songID"]

        video = youtube_search(query)

        if not video:
            continue

        videoId = video["id"]["videoId"]
        publishedAtString = video["snippet"]["publishedAt"]
        translationTable = {ord(c): None for c in [':', '-']}
        publishedAt = datetime.strptime(publishedAtString.translate(translationTable), "%Y%m%dT%H%M%S.%fZ")
        title = video["snippet"]["title"]

        # Populate video table
        s = GetStatisticsForVideo(videoId)
        inputDataList = [videoId, songId, publishedAt, title, s["viewCount"], s["likeCount"],
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


