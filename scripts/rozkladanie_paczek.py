import csv
import os

# Inicjalizacja list 2-wymiarowych dla ID, nazw produktów i wymiarów paczek
id_list = [[]]
names_list = [[]]
dimensions_list = [[]]

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
    global remaining_height, stack_number, number_of_packages
    dimensions_str = product_info['Wymiary (mm)']
    dimensions = [int(dim) for dim in dimensions_str.split('x')]
    package_dimensions = dimensions

    # Sprawdzenie czy paczka zmieści się na aktualnej palecie
    if current_palette['Wysokość'] + package_dimensions[2] <= palette_dimensions['Wysokość']:
        current_palette['Wysokość'] += package_dimensions[2]
        remaining_height = palette_dimensions['Wysokość'] - current_palette['Wysokość']
        id_list[-1].append(product_info['ID Produktu'])
        names_list[-1].append(product_info['Nazwa Produktu'])
        dimensions_list[-1].append(dimensions_str)
        return True
    else:
        # Paczka nie zmieści się na aktualnej palecie, sprawdź czy można umieścić jedna na drugiej
        if package_dimensions[2] <= remaining_height:
            remaining_height -= package_dimensions[2]
            stack_number += 1
            current_palette['Wysokość'] = package_dimensions[2]
            id_list[-1].append(product_info['ID Produktu'])
            names_list[-1].append(product_info['Nazwa Produktu'])
            dimensions_list[-1].append(dimensions_str)
            return True
        else:
            # Paczka nie zmieściła się ani na palecie, ani jedna na drugiej, rozpocznij nową paletę
            return False

# Iteracja przez posegregowane paczki i dodawanie paczek na palety
for product_info in products_data:
    # Spróbuj dodać paczkę do aktualnej palety
    if add_package_to_palette(product_info):
        # Jeżeli paczka została pomyślnie dodana, inkrementuj licznik paczek
        number_of_packages += 1
    else:
        # Jeżeli paczka nie zmieści się na aktualnej palecie, rozpocznij nową paletę
        current_palette = {'Szerokość': 0, 'Długość': 0, 'Wysokość': 0}
        remaining_height = palette_dimensions['Wysokość']
        stack_number = 1  # Reset numeru stosu
        # Zapisz ID, nazwy produktów i wymiary paczek na aktualnej palecie jako osobne listy dla każdej palety
        id_list.append([])
        names_list.append([])
        dimensions_list.append([])

        # Dodaj ID, nazwę produktu i wymiary pierwszej paczki do nowej palety
        id_list[-1].append(product_info['ID Produktu'])
        names_list[-1].append(product_info['Nazwa Produktu'])
        dimensions_list[-1].append(product_info['Wymiary (mm)'])

        # Liczba paczek na palecie powinna zostać zresetowana do 1
        number_of_packages = 1
        palette_number += 1

# Zapisz listy ID, nazw produktów i wymiarów paczek do plików tekstowych
with open('ID.txt', 'w') as id_file:
    for id_sublist in id_list:
        id_file.write(str(id_sublist) + '\n')

with open('NazwyProduktow.txt', 'w') as names_file:
    for names_sublist in names_list:
        names_file.write(str(names_sublist) + '\n')

with open('WymiaryProduktow.txt', 'w') as dimensions_file:
    for dimensions_sublist in dimensions_list:
        dimensions_file.write(str(dimensions_sublist) + '\n')

# Wyświetlanie informacji o ostatniej palecie
print(f"\nOstatnia paleta {palette_number}. Ilość paczek na palecie: {number_of_packages}. Wolna przestrzeń: {remaining_height} mm.")
