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
palette_dimensions = {'Szerokość': 800, 'Długość': 1200, 'Wysokość': 144}

# Inicjalizacja zmiennych
current_palette = {'Szerokość': 0, 'Długość': 0, 'Wysokość': 0}
number_of_packages = 0
palette_number = 1

# Funkcja do dodawania paczki na palecie
def add_package_to_palette(product_info):
    dimensions_str = product_info['Wymiary (mm)']
    dimensions = [int(dim) for dim in dimensions_str.split('x')]
    package_dimensions = dimensions

    # Sprawdzenie czy paczka zmieści się na aktualnej palecie
    if (current_palette['Szerokość'] + package_dimensions[0] <= palette_dimensions['Szerokość'] and
            current_palette['Długość'] + package_dimensions[1] <= palette_dimensions['Długość']):
        current_palette['Szerokość'] += package_dimensions[0]
        current_palette['Długość'] += package_dimensions[1]
        current_palette['Wysokość'] = max(current_palette['Wysokość'], package_dimensions[2])
        print(f"Dodano paczkę ID {product_info['ID Produktu']} na palecie {palette_number}. Wymiary paczki: {dimensions_str}.")
        return True
    elif (current_palette['Szerokość'] + package_dimensions[1] <= palette_dimensions['Szerokość'] and
          current_palette['Długość'] + package_dimensions[0] <= palette_dimensions['Długość']):
        # Spróbuj umieścić paczkę w innej orientacji
        current_palette['Szerokość'] += package_dimensions[1]
        current_palette['Długość'] += package_dimensions[0]
        current_palette['Wysokość'] = max(current_palette['Wysokość'], package_dimensions[2])
        print(f"Dodano paczkę ID {product_info['ID Produktu']} na palecie {palette_number}. Wymiary paczki (inna orientacja): {dimensions_str}.")
        return True
    else:
        return False

# Iteracja przez posegregowane paczki i dodawanie większych paczek na palety
for product_info in products_data:
    # Spróbuj dodać paczkę do aktualnej palety
    if not add_package_to_palette(product_info):
        # Jeżeli paczka nie zmieści się na aktualnej palecie, rozpocznij nową paletę
        print(f"\nZaczynam nową paletę {palette_number}. Ilość paczek na poprzedniej palecie: {number_of_packages}")
        current_palette = {'Szerokość': 0, 'Długość': 0, 'Wysokość': 0}
        number_of_packages = 1
        palette_number += 1

# Wyszukaj paczki mniejsze i dodaj je do istniejących palet
print("\nSzukam paczek mniejszych, aby uzupełnić istniejące palety...")
for product_info in products_data:
    if product_info not in added_packages:
        # Spróbuj dodać paczkę o mniejszych wymiarach do istniejącej palety
        added_to_palette = False
        for i in range(1, palette_number + 1):
            if add_package_to_palette(product_info):
                added_to_palette = True
                break

        if not added_to_palette:
            print(f"Nie udało się umieścić paczki ID {product_info['ID Produktu']} na żadnej z istniejących palet.")

# Wyświetlanie informacji o ostatniej palecie
print(f"\nOstatnia paleta {palette_number}. Ilość paczek na palecie: {number_of_packages}")
