from flask import Flask, redirect
from helpers import load_site, load_database

app = Flask(__name__)
database_data = load_database()

# the minimal Flask application
@app.route('/')
def root():
    return redirect('/index.html')

@app.route('/index.html')
def index():
    return load_site("./site/index.html")

@app.route('/style.css')
def style():
    return load_site("./site/style.css")
    
@app.route('/undefined')
def undefined():
    return 'Fuck off!'
        

@app.route('/package_route.html')
def package_route_page():
    return load_site("./site/package_route.html")

@app.route('/package_layout.html')
def package_layout_page():
    return load_site("./site/package_layout.html")

@app.route('/database.html')
def database_page():
    return load_site("./site/database.html")


@app.route('/database/get_entries', defaults={'number': 50})
@app.route('/database/get_entries/<int:number>')
def database(number: int):
    # loads 50 first entries
    res = ""
    products_data = sorted(database_data, key=lambda x: x['ID Produktu'], reverse=False)
    for i in range(0, min(number, len(products_data))):
        res = res + f"""
            <tr>
                <td>{products_data[i]['ID Produktu']}</td>
                <td>{products_data[i]['Nazwa Produktu']}</td>
                <td>{products_data[i]['Waga (kg)']}</td>
                <td>{products_data[i]['Wymiary (mm)']}</td>
            </tr>
            """
    
    return f"""
            <table>
                <tr>
                    <th>ID Produktu</th>
                    <th>Nazwa Produktu</th>
                    <th>Waga (kg)</th>
                    <th>Wymiary (mm)</th>
                </tr>
                {res}
            </table>
            """
        

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

# run
app.run(host='192.168.1.18', debug=True)
