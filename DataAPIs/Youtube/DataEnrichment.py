from googleapiclient.discovery import build

from DBPopulation.insert_queries import is_valid_ascii
from DataAPIs.MusixMatch.lyrics_analyzer import create_words_map
from Server import config
from datetime import datetime

DEVELOPER_KEY = "AIzaSyBmsB_Jle7kBYJrrGJAkkKO-PgKc0HSWfI"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                developerKey=DEVELOPER_KEY)

INSERT_COMMENT_WORDS_PER_VIDEO = "INSERT INTO CommentWordsPerVideo VALUES (%s, %s, %s);"

# Used for fetching in groups
OFFSET = 20
LIMIT = 200


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
def get_statistics_for_video(video_id):
    search_response = youtube.videos().list(
        id=video_id,
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


def get_comments_for_video(video_id):
    # Right now gets first 10 comments, Can get up to 100 on a single page.
    try:
        results = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
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


def get_songs_artists_pairs_from_db():

    statement = "SELECT GROUP_CONCAT(artistName SEPARATOR ' ') AS artistName, Songs.songName, Songs.songID " \
                "FROM Songs, Artists, SongToArtist " \
                "WHERE Songs.songID = SongToArtist.songID " \
                "AND Artists.artistID = SongToArtist.artistID " \
                "GROUP BY songName, Songs.songID " \
                "ORDER BY Songs.songID ASC " \
                "LIMIT %d, %d;" % (OFFSET, LIMIT)

    config.unsafe_cursor.execute(statement)
    return config.unsafe_cursor.fetchall()


def populate_videos():
    couples = get_songs_artists_pairs_from_db()

    for i, couple in enumerate(couples):
        populate_video(couple["songID"], couple["artistName"], couple["songName"])
        if i % 100 == 0:
            try:
                config.dbconnection.commit()
            except:
                config.dbconnection.rollback()


def populate_video(song_id, artist_name, song_name):
    statement = "INSERT INTO Videos " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s);"
    query = artist_name + " " + song_name

    video = youtube_search(query)
    if not video:
        return

    videoId = video["id"]["videoId"]
    publishedAt = convert_string_to_date(video["snippet"]["publishedAt"])
    title = video["snippet"]["title"]
    # handle non-ascii characters
    if not is_valid_ascii(title):
        return

    # Populate video table
    s = get_statistics_for_video(videoId)
    inputDataList = [videoId, song_id, publishedAt, title, s["viewCount"], s["likeCount"],
                     s["dislikeCount"]]

    try:
        config.cursor.execute(statement, tuple(inputDataList))
    except Exception as e:
        print("Failed to insert video %s - %s, proceeding...\n" % (song_name, artist_name))
        print(e)
        return

    # Populate comments data
    populate_comment_for_video(videoId)
    return videoId


def convert_string_to_date(s):
    translationTable = {ord(c): None for c in [':', '-']}
    return datetime.strptime(s.translate(translationTable), "%Y%m%dT%H%M%S.%fZ")


def insert_into_comment_words_per_video_table(video_id, comment_text):
    words_count = create_words_map(comment_text)
    sql_insert = INSERT_COMMENT_WORDS_PER_VIDEO
    cursor = config.cursor
    try:
        for word, cnt in words_count.iteritems():
            word = word[:20]
            cursor.execute(sql_insert, (video_id, word, cnt))
        config.dbconnection.commit()
    except Exception as e:
        print e
        print "failed to insert comment words for video %s' " % video_id
        return
    return cursor.lastrowid


def populate_comment_for_video(video_id):
    statement = "INSERT INTO Comments " \
                "VALUES (%s, %s, %s, %s, %s);"

    comments = get_comments_for_video(video_id)
    if comments is None:
        return

    try:
        for comment in comments:
            c = comment["snippet"]["topLevelComment"]
            s = c["snippet"]

            publishedAt = convert_string_to_date(s["publishedAt"])
            textDisplay = s["textDisplay"]
            author = s["authorDisplayName"]
            # handle non-ascii characters
            if not is_valid_ascii(author) or not is_valid_ascii(textDisplay):
                continue

            inputDataList = [c["id"], s["videoId"], author,
                             textDisplay, publishedAt]

            config.cursor.execute(statement, tuple(inputDataList))
            # populate CommentWordsPerVideoTable
            insert_into_comment_words_per_video_table(video_id, textDisplay)
    except Exception as e:
        print e


def main():
    populate_videos()


if __name__ == "__main__":
    main()




