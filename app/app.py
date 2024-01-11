from flask import Flask, redirect, Response, request, send_file
from helpers import load_site
from attic import database_data, orders_data
from packing import pack_to_palette
from movement import generate_path
from drawing import generate_path_image

app = Flask(__name__)

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

@app.route('/order.html/<id>')
def order_page(id: int):
    figures = pack_to_palette(str(id))
    plots = ""
    for f in figures:
        plots += f"""
            <img src="/data/plots/{f}" alt="figure">
            """
    
    maps = ""
    for d in orders_data[1:]:
        maps += f"""
            <img src="/order/{id}/map" alt="map">
            """
    
    site = load_site('./site/order.html').replace('{id}', str(id))
    site = site.replace("{plots}", plots)
    site = site.replace("{plots_n}", str(len(figures)))
    site = site.replace("{map_source}", maps)
    return site

@app.route('/components/menu.html')
def menu_component():
    return send_file('./components/menu.html')

@app.route('/data/plots/<p_name>')
def get_plot(p_name: str):
    return send_file(f"./data/plots/{p_name}")


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
    order_by = request.args.get('order', default='ID', type=str)
    ascending = bool(request.args.get('ascending', default=1, type=int))
    
    if order_by == 'ID': orders_list = sorted(orders_data, key=lambda x: int(x['ID']), reverse=(not ascending))
    elif order_by == 'Count': orders_list = sorted(orders_data, key=lambda x: len(x['Data']), reverse=(not ascending))
    
    amount = len(orders_list)
    
    st = ""
    for order in orders_list:
        st = st + f"""
            <tr>
                <td>{order['ID']}</td>
                <td>{len(order['Data'])}</td>
                <td id="orderButton"><a href="/order.html/{order['ID']}">Show order</a></td>
            </tr>
            """
    
    return f"""
        <table>
            <tr>
                <th>ID</th>
                <th>Items amount</th>
                <th></th>
            </tr>
            {st}
        </table>
        """

@app.route('/order/<id>/map')
def get_map(id: int):
    order = ([ord for ord in orders_data if ord['ID'] == str(id)])[0]['Data']
    
    # Utter retardedness
    prev_loc = order[0]['Location']
    for d in order[1:]:
        generate_path(prev_loc, d['Location'])
        generate_path_image(f"{id}-{d['Location']}.jpg")
    
    return send_file(f"{id}-{d['Location']}.jpg")
        

@app.route('/order/<id>')
def order(id: int):
    order_by = request.args.get('order', default='ID', type=str)
    ascending = bool(request.args.get('ascending', default=1, type=int))
    
    order = ([ord for ord in orders_data if ord['ID'] == str(id)])[0]['Data']
    if order_by == 'ID': order_list = sorted(order, key=lambda x: (x['ID']), reverse=(not ascending))
    if order_by == 'Name': order_list = sorted(order, key=lambda x: (x['Name']), reverse=(not ascending))
    if order_by == 'Amount': order_list = sorted(order, key=lambda x: (x['Amount']), reverse=(not ascending))
    
    table = ""
    for prod in order_list:
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

