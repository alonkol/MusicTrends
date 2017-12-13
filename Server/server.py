from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Wabadabadubdub!"

if __name__ == '__main__':
    app.run(port=40333, host="localhost", debug=True)