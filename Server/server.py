from flask import Flask
app = Flask(__name__)

# general idea:
# show trends of word usage as a function of time (song's air-date)
# Like in google trends, but for music

import mysql.connector

cnx = mysql.connector.connect(user='MysqlDb07', password='MysqlDb07',
                              host='127.0.0.1',
                              database='sys')

cursor = cnx.cursor(prepared=True)

# dbconnection.close()

@app.route('/')
def hello_world():
    return "Wabadabadubdub!"

# TODO: get categories from db
@app.route('/categories')
def categories():
    # statement = "SELECT * FROM categories WHERE id = %s"
    statement = "SELECT * FROM categories"
    # cursor.execute(statement, (5,))

    return cursor.execute(statement)

# TODO: query db
@app.route('/songs/likes/top/<int:amount>')
def TopSongLikes(amount):
    return ""

# TODO: query db
@app.route('/songs/dislikes/top/<int:amount>')
def TopSongDislikes(amount):
    return ""

# TODO: query db
@app.route('/songs/views/top/<int:amount>')
def TopSongViews(amount):
    return ""

# TODO: query db
@app.route('/songs/views/bottom/<int:amount>')
def BottomSongViews(amount):
    return ""

# TODO: query db
@app.route('/words/top/<int:amount>')
def TopWords(amount):
    return ""

# TODO: query db
@app.route('/words/bottom/<int:amount>')
def BottomWords(amount):
    return ""

# TODO: query db
# create scoring system?
@app.route('/songs/wordscore/top/<int:amount>')
def TopSophisticatedSongs(amount):
    return ""


# TODO: write page not found html
'''
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
'''

if __name__ == '__main__':
    app.run(port=40333, host="delta-tomcat-vm", debug=True)