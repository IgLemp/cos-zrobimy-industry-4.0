import csv
import os
import re


# usefull functions
def load_site(file: str) -> str:
    with open(file, "r") as file:
        return file.read()


# Inicjalizacja listy produktów
def load_database() -> list:
    products_data = []

    # Nazwa pliku CSV
    csv_file = os.path.join('data', 'product_list.csv')

    # Wczytywanie danych z pliku CSV
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Zapisywanie danych do listy
            product_info = {
                'ID':     int(row['ID Produktu']),
                'Name':   row['Nazwa Produktu'],
                'Weight': float(row['Waga (kg)']),  # Konwersja wagi na float dla poprawnego sortowania
                'Dimensions': row['Wymiary (mm)'].split('x'),
            }
            products_data.append(product_info)

    # Sortowanie listy produktów według wagi (malejąco)
    products_data = sorted(products_data, key=lambda x: x['Weight'], reverse=True)
    return products_data


def load_orders():
    data = []
    files = [f for f in os.listdir(os.path.join('data', 'orders'))]
    for fname in files:
        with open(os.path.join('data', 'orders', fname), 'r') as file:
            fid = re.sub('\D', '', fname)
            file_data = []
            
            reader = csv.DictReader(file)
            for row in reader:
                order_data = {
                    'ID':       row['ID Produktu'],
                    'Name':     row['Nazwa Produktu'],
                    'Location': row['Lokacja'],
                    'Amount':   row['Ilość']
                }
                file_data.append(order_data)
            
            data.append({'ID': fid ,'Data': file_data})
    
    return data

if __name__ == '__main__':
    print(load_orders()[0])