import csv
import os

# Inicjalizacja listy produktów
products_data = []

# Nazwa pliku CSV
csv_file = os.path.join('ListaProduktow.csv')

# Wczytywanie danych z pliku CSV
with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Zapisywanie danych do listy
        product_info = {
            'ID Produktu': row['ID Produktu'],
            'Nazwa Produktu': row['Nazwa Produktu'],
            'Waga (kg)': float(row['Waga (kg)']),
            'Wymiary (mm)': row['Wymiary (mm)'],
        }
        products_data.append(product_info)

# Sortowanie listy produktów według wagi malejąco
products_data = sorted(products_data, key=lambda x: x['Waga (kg)'], reverse=True)

# Wymiary palety
palette_dimensions = {'Szerokość': 800, 'Długość': 1200, 'Wysokość': 1856}

# Inicjalizacja zmiennych
current_palette = {'Szerokość': 0, 'Długość': 0, 'Wysokość': 0}
number_of_packages = 0
palette_number = 1
current_layer_height = 0

# Funkcja do dodawania paczki na palecie
def add_package_to_palette(product_info):
    global current_layer_height  # Dodano deklarację jako zmiennej globalnej
    dimensions_str = product_info['Wymiary (mm)']
    dimensions = [int(dim) for dim in dimensions_str.split('x')]
    package_dimensions = dimensions

    # Sprawdzenie czy paczka zmieści się na aktualnej palecie i warstwie
    if (current_palette['Szerokość'] + package_dimensions[0] <= palette_dimensions['Szerokość'] and
            current_palette['Długość'] + package_dimensions[1] <= palette_dimensions['Długość'] and
            current_layer_height + package_dimensions[2] <= palette_dimensions['Wysokość']):
        current_palette['Szerokość'] += package_dimensions[0]
        current_palette['Długość'] += package_dimensions[1]
        current_layer_height += package_dimensions[2]
        print(f"Dodano paczkę ID {product_info['ID Produktu']} na palecie {palette_number}. Wymiary paczki: {dimensions_str}. Wysokość warstwy: {current_layer_height}.")
        return True
    elif (current_palette['Szerokość'] + package_dimensions[1] <= palette_dimensions['Szerokość'] and
          current_palette['Długość'] + package_dimensions[0] <= palette_dimensions['Długość'] and
          current_layer_height + package_dimensions[2] <= palette_dimensions['Wysokość']):
        # Spróbuj umieścić paczkę w innej orientacji
        current_palette['Szerokość'] += package_dimensions[1]
        current_palette['Długość'] += package_dimensions[0]
        current_layer_height += package_dimensions[2]
        print(f"Dodano paczkę ID {product_info['ID Produktu']} na palecie {palette_number}. Wymiary paczki (inna orientacja): {dimensions_str}. Wysokość warstwy: {current_layer_height}.")
        return True
    else:
        # Paczka nie zmieściła się na aktualnej palecie, rozpocznij nową
        return False

# Iteracja przez posegregowane paczki i dodawanie paczek na palety
for product_info in products_data:
    number_of_packages += 1  # Inkrementacja licznika paczek

    # Spróbuj dodać paczkę do aktualnej palety
    if not add_package_to_palette(product_info):
        # Jeżeli paczka nie zmieści się na aktualnej palecie, rozpocznij nową paletę
        print(f"\nZaczynam nową paletę {palette_number}. Ilość paczek na poprzedniej palecie: {number_of_packages}.")
        current_palette = {'Szerokość': 0, 'Długość': 0, 'Wysokość': 0}
        current_layer_height = 0
        number_of_packages = 1
        palette_number += 1
        # Spróbuj dodać paczkę do nowej palety
        if not add_package_to_palette(product_info):
            print(f"Nie udało się umieścić paczki ID {product_info['ID Produktu']} na nowej palecie.")

# Wyświetlanie informacji o ostatniej palecie
print(f"\nOstatnia paleta {palette_number}. Ilość paczek na palecie: {number_of_packages}. Wysokość warstwy: {current_layer_height}.")
