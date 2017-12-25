import mysql.connector
import json
from flask import Flask
from flask import render_template

# general idea:
# show trends of word usage as a function of time (song's air-date)
# Like in google trends, but for music

# Local
# host = "localhost"
# dbhost = "localhost"
# user = "root"
# password = "DbMysql07"
# dbname = "sys"

# Production
host = "delta-tomcat-vm"
dbhost = "mysqlsrv.cs.tau.ac.il"
user = "DbMysql07"
password = "DbMysql07"
dbname = "DbMysql07"

app = Flask(__name__)
port = 40335

cnx = mysql.connector.connect(user=user, password=password,
                              host=dbhost,
                              database=dbname)

cursor = cnx.cursor(prepared=True)


###############################
# -------- REST API --------- #
###############################


# --- Routes --- #
@app.route('/api')
def ApiWelcome():
    return render_template('api.html')


@app.route('/api/categories')
def Categories():
    statement = "SELECT id, name " \
                "FROM categories;"

    return GetJSONResult(statement)


@app.route('/api/songs/likes/top/<int:amount>')
def TopSongLikes(amount):
    statement = "SELECT * " \
                "FROM songs " \
                "ORDER BY likes DESC " \
                "LIMIT %s;"

    return GetJSONResult(statement, (amount,))


@app.route('/api/songs/dislikes/top/<int:amount>')
def TopSongDislikes(amount):
    statement = "SELECT * " \
                "FROM songs " \
                "ORDER BY dislikes DESC " \
                "LIMIT %s;"

    return GetJSONResult(statement, (amount,))


@app.route('/api/songs/views/top/<int:amount>')
def TopSongViews(amount):
    statement = "SELECT * " \
                "FROM songs " \
                "ORDER BY views DESC " \
                "LIMIT %s;"

    return GetJSONResult(statement, (amount,))


@app.route('/api/songs/views/bottom/<int:amount>')
def BottomSongViews(amount):
    statement = "SELECT * " \
                "FROM songs " \
                "ORDER BY views ASC " \
                "LIMIT %s;"

    return GetJSONResult(statement, (amount,))


@app.route('/api/words/top/<int:amount>')
def TopWords(amount):
    statement = "SELECT word, SUM(count) AS count " \
                "FROM WordsPerSong " \
                "GROUP BY word " \
                "ORDER BY count DESC " \
                "LIMIT %s;"

    return GetJSONResult(statement, (amount,))


@app.route('/api/words/bottom/<int:amount>')
def BottomWords(amount):
    statement = "SELECT word, SUM(count) AS count " \
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
        cursor.execute(statement, params)
    else:
        cursor.execute(statement)

    rows = cursor.fetchall()

    # converts every row from (index, ByteArray1, ByteArray2, ...) to (String1, String2, ...)
    tuples = [row[1].decode("utf-8") for row in rows]

    return json.dumps({"result": tuples})


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
    app.run(port=port, host=host, debug=True)
