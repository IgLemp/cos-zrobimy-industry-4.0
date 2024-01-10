from flask import Flask, redirect

app = Flask(__name__)


# the minimal Flask application
@app.route('/')
def root():
    return redirect('/index.html')

@app.route('/index.html')
def index():
    with open("./site/index.html", "r") as file:
        return file.read()

@app.route('/style.css')
def style():
    with open("./site/style.css",  "r") as file:
        return file.read()
    
@app.route('/undefined')
def undefined():
    return 'Fuck off!'
        

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
