from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('ticker.html')

@app.route("/board")
def render_board():
    return {'messages': [{'text': 'HELLO'},
                         {'text': 'WORLD'}]}

