import csv
import os


# usefull functions
def load_site(file: str) -> str:
    with open(file, "r") as file:
        return file.read()


# Inicjalizacja listy produktów
def load_database() -> list:
    products_data = []

    # Nazwa pliku CSV
    csv_file = os.path.join('data', 'ListaProduktow.csv')

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

