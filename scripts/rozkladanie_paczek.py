import csv
import os

def load_dimensions(filename):
    dimensions = {}
    with open(filename, newline='', encoding='utf-8') as dimensions_file:
        dimensions_reader = csv.DictReader(dimensions_file)
        for row in dimensions_reader:
            dimensions[row['ID Produktu']] = {
                'Waga (kg)': row['Waga (kg)'],
                'Wymiary (mm)': row['Wymiary (mm)']
            }
    return dimensions

def create_package_list():
    # Inicjalizacja list 2-wymiarowych dla ID, nazw produktów i wymiarów paczek
    id_list = [[]]
    names_list = [[]]
    dimensions_list = [[]]

    # Inicjalizacja listy produktów
    products_data = []

    # Wczytaj wymiary paczek
    dimensions = load_dimensions('ListaProduktow.csv')

    # Pobierz dane z pliku Zamowienie13.csv
    with open('Zamowienie13.csv', newline='', encoding='utf-8') as zamowienie_file:
        zamowienie_reader = csv.DictReader(zamowienie_file)
        for row in zamowienie_reader:
            id_produktu = row['ID Produktu']
            ilosc = int(row['Ilość'])

            # Pobierz dane dotyczące produktu z ListaProduktow.csv
            produkt_info = dimensions.get(id_produktu)

            if produkt_info:
                waga = produkt_info['Waga (kg)']
                wymiary = produkt_info['Wymiary (mm)']

                # Dodaj ilość produktów do listy do realizacji
                for _ in range(ilosc):
                    products_data.append({
                        'ID Produktu': id_produktu,
                        'Nazwa Produktu': row['Nazwa Produktu'],
                        'Waga (kg)': waga,
                        'Wymiary (mm)': wymiary
                    })

    # Sortowanie listy produktów według wagi malejąco, a następnie wymiarów malejąco
    products_data = sorted(products_data, key=lambda x: (x['Waga (kg)'], x['Wymiary (mm)']), reverse=True)

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
        nonlocal remaining_height, stack_number, number_of_packages
        dimensions_str = product_info['Wymiary (mm)']
        dimensions = [int(dim) for dim in dimensions_str.split('x')]
        package_dimensions = dimensions

        # Sprawdzenie czy paczka ma takie same wymiary jak poprzednie paczki na palecie
        if dimensions_list[-1] and dimensions_list[-1][0] != dimensions_str:
            return False

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

    # Wyświetl informacje o ostatniej palecie
    print(f"\nOstatnia paleta {palette_number}. Ilość paczek na palecie: {number_of_packages}. Wolna przestrzeń: {remaining_height} mm.")

    # Zwróć potrzebne dane
    return id_list, names_list, dimensions_list

if __name__ == "__main__":
    create_package_list()
