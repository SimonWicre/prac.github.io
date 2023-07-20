from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def hello():
    # return 'Welcome to My Watchlist!'
    return '<h1>hello tororo!</h1>'
 