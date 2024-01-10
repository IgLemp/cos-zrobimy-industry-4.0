from flask import Flask, redirect, Response, request, send_file
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
    return send_file('./site/index.html')

@app.route('/style.css')
def style():
    return send_file('./site/style.css')

@app.route('/package_route.html')
def package_route_page():
    return send_file('./site/package_route.html')

@app.route('/package_layout.html')
def package_layout_page():
    return send_file('./site/package_layout.html')

@app.route('/database.html')
def database_page():
    return send_file('./site/database.html')

@app.route('/orders.html')
def orders_page():
    return send_file('./site/orders.html')

@app.route('/order.html')
def order_page():
    id = request.args.get('id', default=1, type=int)
    return load_site('./site/order.html').replace('{id}', str(id))

@app.route('/components/menu.html')
def menu_component():
    return send_file('./components/menu.html')

@app.route('/data/kekw.png')
def kekw():
    return send_file('./data/kekw.png')



@app.route('/database/count')
def database_count():
    return f"{len(database_data)}"

@app.route('/orders/count')
def orders_count():
    return f"{len(orders_data)}"



@app.route('/orders')
def orders():
    orders_list = sorted(orders_data, key=lambda x: int(x['ID']), reverse=False)
    amount = len(orders_list)
    
    head = f"""<h2>Current number of orders: {amount}</h2>"""
    
    st = ""
    for order in orders_list:
        st = st + f"""
            <tr>
                <td>{order['ID']}</td>
                <td>{len(order['Data'])}</td>
                <td id="orderButton"><a href="/order.html?id={order['ID']}">Show order</a></td>
            </tr>
            """
    
    return f"""
        {head}
        <table>
            <tr>
                <th>ID</th>
                <th>Items amount</th>
                <th>button</th>
            </tr>
            {st}
        </table>
        """

@app.route('/order')
def order():
    id = request.args.get('id', default=1, type=int)
    order = ([ord for ord in orders_data if ord['ID'] == str(id)])[0]['Data']
    
    table = ""
    for prod in order:
        table = table + f"""
            <tr>
                <td>{prod['ID']}</td>
                <td>{prod['Name']}</td>
                <td>{prod['Location']}</td>
                <td>{prod['Amount']}</td>
            </tr>
            """
    
    return f"""
        <table>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Location</th>
                <th>Amount</th>
            </tr>
            {table}
        </table>
        """


@app.route('/database/get_entries')
def database():
    order_by = request.args.get('order', default='ID', type=str)
    selected = request.args.get('count', default=20, type=int)
    ascending = bool(request.args.get('ascending', default=1, type=int))
    
    order_by = order_by if order_by in ['ID', 'Name', 'Weight', 'Dimensions'] else 'ID'
    if selected < 0: selected = 0
    if selected > len(database_data): selected = len(database_data)
    
    res = ""
    products_data = sorted(database_data, key=lambda x: x[order_by], reverse=(not ascending))
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
        

app.run(host='192.168.1.18', debug=True)
