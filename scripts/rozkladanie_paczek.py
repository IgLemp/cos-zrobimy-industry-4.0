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
remaining_height = palette_dimensions['Wysokość']  # Dodana zmienna do śledzenia brakującej wysokości
stack_number = 1  # Numer stosu paczek na palecie

# Funkcja do dodawania paczki na palecie
def add_package_to_palette(product_info):
    global remaining_height, stack_number
    dimensions_str = product_info['Wymiary (mm)']
    dimensions = [int(dim) for dim in dimensions_str.split('x')]
    package_dimensions = dimensions

    # Sprawdzenie czy paczka zmieści się na aktualnej palecie
    if current_palette['Wysokość'] + package_dimensions[2] <= palette_dimensions['Wysokość']:
        current_palette['Wysokość'] += package_dimensions[2]
        remaining_height = palette_dimensions['Wysokość'] - current_palette['Wysokość']
        print(f"Paczka ID {product_info['ID Produktu']} na palecie {palette_number}, stos {stack_number}. Wymiary paczki: {dimensions_str}. Wolna przestrzeń: {remaining_height} mm.")
        return True
    else:
        # Paczka nie zmieści się na aktualnej palecie, sprawdź czy można umieścić jedna na drugiej
        if package_dimensions[2] <= remaining_height:
            remaining_height -= package_dimensions[2]
            stack_number += 1
            current_palette['Wysokość'] = package_dimensions[2]
            print(f"Paczka ID {product_info['ID Produktu']} na palecie {palette_number}, stos {stack_number}. Wymiary paczki: {dimensions_str}. Wolna przestrzeń (po umieszczeniu jedna na drugiej): {remaining_height} mm.")
            return True
        else:
            # Paczka nie zmieściła się ani na palecie, ani jedna na drugiej, rozpocznij nową paletę
            print(f"Paczce ID {product_info['ID Produktu']} brakuje miejsca na palecie. Wolna przestrzeń: {remaining_height} mm.")
            return False

# Iteracja przez posegregowane paczki i dodawanie paczek na palety
for product_info in products_data:
    number_of_packages += 1  # Inkrementacja licznika paczek

    # Spróbuj dodać paczkę do aktualnej palety
    if not add_package_to_palette(product_info):
        # Jeżeli paczka nie zmieści się na aktualnej palecie, rozpocznij nową paletę
        print(f"\nZaczynam nową paletę {palette_number}. Ilość paczek na poprzedniej palecie: {number_of_packages}")
        current_palette = {'Szerokość': 0, 'Długość': 0, 'Wysokość': 0}
        remaining_height = palette_dimensions['Wysokość']
        number_of_packages = 1
        palette_number += 1
        stack_number = 1  # Reset numeru stosu

# Wyświetlanie informacji o ostatniej palecie
print(f"\nOstatnia paleta {palette_number}. Ilość paczek na palecie: {number_of_packages}. Wolna przestrzeń: {remaining_height} mm.")
