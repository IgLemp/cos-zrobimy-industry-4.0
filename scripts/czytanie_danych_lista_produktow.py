import csv
import os

# Nazwa pliku CSV
csv_file = os.path.join('ListaProduktow.csv')

def load_data() -> list:
    products_data = []
    # Wczytywanie danych z pliku CSV
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Zapisywanie danych do listy
            product_info = {
                'ID Produktu':     row['ID Produktu'],
                'Nazwa Produktu':  row['Nazwa Produktu'],
                'Waga (kg)': float(row['Waga (kg)']),
                'Wymiary (mm)':    row['Wymiary (mm)'],
            }
            products_data.append(product_info)

    # Sortowanie listy produktów według wagi (malejąco)
    products_data = sorted(products_data, key=lambda x: x['Waga (kg)'], reverse=True)
    
    parsed_data = {}
    for rec in products_data:
        dim: str = rec['Wymiary (mm)'].split('x')
        
        parsed_data[str(int(rec['ID Produktu']))] = {
            'name':       rec['Nazwa Produktu'],
            'weight':     rec['Waga (kg)'],
            'dimensions': {
                'x': dim[0],
                'y': dim[1],
                'z': dim[2]
            }
        }

    return parsed_data