from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Home Page'

@app.route('/user/<name>')
def user_page(name):
    # return 'Welcome to My Watchlist!'
    return f'<h1>hi welcome: {escape(name)} </h1>'


@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('user_page', name = 'user1'))
    print(url_for('user_page', name = 'user2'))
    print(url_for('test_url_for', num=2))

    return 'Test Page for URL output'
