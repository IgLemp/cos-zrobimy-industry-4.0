from flask import Flask, redirect

app = Flask(__name__)

index_file = open("./site/index.html", "r").read()
style_file = open("./site/style.css",  "r").read()

# the minimal Flask application
@app.route('/')
def root():
    return redirect('/index.html')

@app.route('/index.html')
def index():
    return index_file

@app.route('/style.css')
def style():
    return style_file

# bind multiple URL for one view function
@app.route('/hi')
@app.route('/hello')
def say_hello():
    return '<h1>Hello, Flask!</h1>'


# dynamic route, URL variable default
@app.route('/greet', defaults={'name': 'Programmer'})
@app.route('/greet/<name>')
def greet(name):
    return '<h1>Hello, %s!</h1>' % name
