from flask import Flask, redirect, Response, request
from helpers import load_site, load_database, load_orders

app = Flask(__name__)

# TODO: this is awfull, make it use a real database with ORM
database_data = load_database()
orders_data = load_orders()

# the minimal Flask application
@app.route('/')
def root():
    return redirect('/index.html')

@app.route('/index.html')
def index():
    return load_site('./site/index.html')

@app.route('/style.css')
def style():
    return Response(load_site('./site/style.css'), mimetype='text/css')

@app.route('/package_route.html')
def package_route_page():
    return load_site('./site/package_route.html')

@app.route('/package_layout.html')
def package_layout_page():
    return load_site('./site/package_layout.html')

@app.route('/database.html')
def database_page():
    return load_site('./site/database.html')

@app.route('/orders.html')
def orders_page():
    return load_site('./site/orders.html')


@app.route('/orders')
def orders():
    amount = len(orders_data)
    
    head = f"""<h2>Current number of orders: {amount}</h2>"""
    
    st = ""
    for order in orders_data:
        st = st + f"""
            <tr>
                <td>{order['ID']}</td>
                <td>{len(order['Data'])}</td>
            </tr>
            """
    
    return f"""
        {head}
        <table>
            <tr>
                <th>ID</th>
                <th>items amount</th>
            </tr>
            {st}
        </table>
        """

@app.route('/order')
def order():
    request.args.get()
    return ''


@app.route('/database/get_entries')
def database():
    order_by = request.args.get('order', default='ID', type=str)
    selected = request.args.get('count', default=20, type=int)
    ascending = request.args.get('ascending', default=True, type=bool)
    print("order_by:", order_by)
    print("selected:", selected)
    print("ascending:", ascending)
    
    order_by = order_by if order_by in ['ID', 'Name', 'Weight', 'Dimensions'] else 'ID'
    if selected < 0: selected = 0
    if selected > len(database_data): selected = len(database_data)
    
    res = ""
    products_data = sorted(database_data, key=lambda x: x[order_by], reverse=ascending)
    for i in range(0, min(selected, len(products_data))):
        res = res + f"""
            <tr>
                <td>{products_data[i]['ID']}</td>
                <td>{products_data[i]['Name']}</td>
                <td>{products_data[i]['Weight']}</td>
                <td>{'x'.join(products_data[i]['Dimensions'])}</td>
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
