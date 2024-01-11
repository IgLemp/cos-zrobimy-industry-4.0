# OK ##########################################################################

from czytanie_danych_lista_produktow import load_data

data = load_data()
parsed_data = {}

for rec in data:
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

print(parsed_data['1'])
