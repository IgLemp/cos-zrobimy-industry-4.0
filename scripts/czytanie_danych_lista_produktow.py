import csv
import os

# Inicjalizacja listy produktów
products_data = []

# Nazwa pliku CSV
csv_file = 'dane_produktow.csv'

# Wczytywanie danych z pliku CSV
with open(os.path.join('ListaProduktow.csv'), 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Zapisywanie danych do listy
        product_info = {
            'ID Produktu': row['ID Produktu'],
            'Nazwa Produktu': row['Nazwa Produktu'],
            'Waga (kg)': float(row['Waga (kg)']),  # Konwersja wagi na float dla poprawnego sortowania
            'Wymiary (mm)': row['Wymiary (mm)'],
        }
        products_data.append(product_info)

# Sortowanie listy produktów według wagi (malejąco)
products_data = sorted(products_data, key=lambda x: x['Waga (kg)'], reverse=True)

# Wyświetlanie wczytanych i posegregowanych danych
for product_info in products_data:
    print(f"ID: {product_info['ID Produktu']}, Dane: {product_info}")

