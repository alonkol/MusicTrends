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

    # Set key if does not exist, set value to 0
    for key in keys:
        if key not in items[0]["statistics"]:
            items[0]["statistics"][key] = 0

    return items[0]["statistics"]


# Right now gets first 10 comments.
# Can get up to 100 on a single page.
# Can get more with paging if necessary.
def GetCommentsForVideo(videoId):
    try:
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

    except Exception as e:
        print e
        return None


def GetAllSongsAndArtistsFromDB():
    offset = 0
    limit = 8000

    statement = "SELECT GROUP_CONCAT(artistName SEPARATOR ' ') AS artistName, songName, songs.songID " \
                "FROM Songs, Artists, SongToArtist " \
                "WHERE Songs.songID = SongToArtist.songID " \
                "AND Artists.artistID = SongToArtist.artistID " \
                "GROUP BY songName, songs.songID " \
                "ORDER BY songs.songID ASC " \
                "LIMIT %d, %d;" % (offset, limit)

    config.unsafe_cursor.execute(statement)
    return config.unsafe_cursor.fetchall()


def GetAllVideoIdsFromDB():
    statement = "SELECT videoID " \
                "FROM Videos; "
    config.unsafe_cursor.execute(statement)
    results = config.unsafe_cursor.fetchall()

    return [result["videoID"] for result in results]


def PopulateVideos():
    couples = GetAllSongsAndArtistsFromDB()

    statement = "INSERT INTO videos " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, Default);"

    for couple in couples:
        songId = couple["songID"]
        query = couple["artistName"] + " " + couple["songName"]

        video = youtube_search(query)

        if not video:
            continue

        videoId = video["id"]["videoId"]
        publishedAt = ConvertStringToDate(video["snippet"]["publishedAt"])
        title = video["snippet"]["title"].encode('unicode_escape')

        # Populate video table
        s = GetStatisticsForVideo(videoId)
        inputDataList = [videoId, songId, publishedAt, title, s["viewCount"], s["likeCount"],
                         s["dislikeCount"], s["favoriteCount"], s["commentCount"]]

        try:
            config.cursor.execute(statement, tuple(inputDataList))
        except Exception as e:
            print("Failed to insert video, proceeding...\n")
            print(e)
            continue

        if cnt[0] % 100 == 0:
            try:
                config.dbconnection.commit()
            except:
                config.dbconnection.rollback()


def ConvertStringToDate(s):
    translationTable = {ord(c): None for c in [':', '-']}
    return datetime.strptime(s.translate(translationTable), "%Y%m%dT%H%M%S.%fZ")


def PopulateComments():
    videoIds = GetAllVideoIdsFromDB()
    i = 0

    statement = "INSERT INTO comments " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s);"

    for videoId in videoIds:
        i += 1
        comments = GetCommentsForVideo(videoId)
        print("#%d - Got the comments for video %s\n" % (i, videoId))

        if comments is not None:
            try:
                for comment in comments:
                    c = comment["snippet"]["topLevelComment"]
                    s = c["snippet"]

                    publishedAt = ConvertStringToDate(s["publishedAt"])
                    viewerRating = s["viewerRating"]
                    textDisplay = s["textDisplay"].encode('unicode_escape')
                    author = s["authorDisplayName"].encode('unicode_escape')

                    if (viewerRating == 'none'):
                        viewerRating = None

                    inputDataList = [c["id"], s["videoId"], author,
                                     textDisplay, publishedAt,
                                     viewerRating, s["likeCount"]]

                    config.cursor.execute(statement, tuple(inputDataList))
            except Exception as e:
                print e

            if i % 100 == 0:
                try:
                    config.dbconnection.commit()
                except:
                    config.dbconnection.rollback()


if __name__ == "__main__":

    #PopulateVideos()
    PopulateComments()


