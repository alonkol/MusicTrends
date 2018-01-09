import json
from flask import Flask
from flask import render_template
import config

# general idea:
# show trends of word usage as a function of time (song's air-date)
# Like in google trends, but for music

app = Flask(__name__)

###############################
# -------- REST API --------- #
###############################

# --- Routes --- #
@app.route('/api')
def ApiWelcome():
    return render_template('api.html')


@app.route('/api/categories')
def Categories():
    statement = "SELECT categoryID as id, categoryName as name " \
                "FROM categories;"

    return GetJSONResult(statement)


@app.route('/api/songs/likes/top/<int:amount>')
def TopSongLikes(amount):
    statement = "SELECT songName, likeCount " \
                "FROM songs, videos " \
                "WHERE songs.songID = videos.songID " \
                "ORDER BY likeCount DESC " \
                "LIMIT %s;"

    return GetJSONResult(statement, (amount,))


@app.route('/api/songs/dislikes/top/<int:amount>')
def TopSongDislikes(amount):
    statement = "SELECT songName, dislikeCount " \
                "FROM songs, videos " \
                "WHERE songs.songID = videos.songID " \
                "ORDER BY dislikeCount DESC " \
                "LIMIT %s;"

    return GetJSONResult(statement, (amount,))


@app.route('/api/songs/views/top/<int:amount>')
def TopSongViews(amount):
    statement = "SELECT songName, viewCount " \
                "FROM songs, videos " \
                "WHERE songs.songID = videos.songID " \
                "ORDER BY viewCount DESC " \
                "LIMIT %s;"

    return GetJSONResult(statement, (amount,))


@app.route('/api/songs/views/bottom/<int:amount>')
def BottomSongViews(amount):
    statement = "SELECT songName, viewCount " \
                "FROM songs, videos " \
                "WHERE songs.songID = videos.songID " \
                "ORDER BY viewCount ASC " \
                "LIMIT %s;"

    return GetJSONResult(statement, (amount,))


@app.route('/api/words/top/<int:amount>')
def TopWords(amount):
    statement = "SELECT word, SUM(wordCount) AS count " \
                "FROM WordsPerSong " \
                "GROUP BY word " \
                "ORDER BY count DESC " \
                "LIMIT %s;"

    return GetJSONResult(statement, (amount,))


@app.route('/api/words/bottom/<int:amount>')
def BottomWords(amount):
    statement = "SELECT word, SUM(wordCount) AS count " \
                "FROM WordsPerSong " \
                "GROUP BY word " \
                "ORDER BY count ASC " \
                "LIMIT %s;"

    return GetJSONResult(statement, (amount,))

# TODO: query db
# create scoring system?
@app.route('/api/songs/wordscore/top/<int:amount>')
def TopSophisticatedSongs(amount):
    return ""


# --- Auxiliary --- #

def GetJSONResult(statement, params=None):
    if params is not None:
        config.cursor.execute(statement, params)
    else:
        config.cursor.execute(statement)

    rows = config.cursor.fetchall()

    # decode results to strings
    results = []

    # row to dict
    for row in rows:
        res = {}

        for index, cell in enumerate(row):
            res[config.cursor.column_names[index]] = str(cell).decode("utf-8")

        results.append(res)

    return json.dumps({
        "amount": len(results),
        "results": results}
    )


###############################
# --------- Pages ----------- #
###############################
@app.route('/')
def Homepage():
    return "Wabadabadubdub!"


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == '__main__':
    app.run(port=config.port, host=config.host, debug=True)
