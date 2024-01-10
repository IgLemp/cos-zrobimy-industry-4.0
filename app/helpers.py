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
                'ID Produktu': row['ID Produktu'],
                'Nazwa Produktu': row['Nazwa Produktu'],
                'Waga (kg)': float(row['Waga (kg)']),  # Konwersja wagi na float dla poprawnego sortowania
                'Wymiary (mm)': row['Wymiary (mm)'],
            }
            products_data.append(product_info)

    # Sortowanie listy produktów według wagi (malejąco)
    products_data = sorted(products_data, key=lambda x: x['Waga (kg)'], reverse=True)
    return products_data