from flask import Flask, render_template
import datetime
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello dear DB students!"

if __name__ == '__main__':
    app.run(port=8888, host="0.0.0.0", debug=True)