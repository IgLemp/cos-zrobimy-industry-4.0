from PIL import Image, ImageDraw
def przyporzadkuj(liczba):
    if liczba == 1 or liczba == 2 or liczba==15 or liczba==16:
        return 1
    elif 3==liczba or liczba== 4 or liczba==14 or liczba==13:
        return 2
    elif 5 == liczba or liczba == 6 or liczba==12 or liczba ==11:
        return 3
    elif 7 == liczba or liczba== 8 or liczba==10 or liczba==9:
        return 4
def rysuj_kwadrat(lista_punktow):
    map_image = Image.open("scripts/rys/mapa.jpg")
    draw = ImageDraw.Draw(map_image)
    for x, y in lista_punktow:
        draw.rectangle([x - 12.5, y-12.5, x + 12.5, y+12.5], fill=(255, 0, 0))
    map_image.save("scripts/rys/pomoc.jpg")
def rysuj_prosta(lista_punktow):
    map_image = Image.open("scripts/rys/pomoc.jpg")
    draw = ImageDraw.Draw(map_image)
    for i in range(len(lista_punktow) - 1):
        (x1, y1) = lista_punktow[i]
        (x2, y2) = lista_punktow[i + 1]
        draw.line([(x1, y1), (x2, y2)], fill=(255, 0, 0), width=5)

    map_image.save("scripts/rys/koniec.jpg")
# Otwieramy plik magazyn.txt do odczytu
with open('scripts/magazyn.txt', 'r') as file:
    # Inicjalizujemy pusty słownik
    magazyn_dict = {}

    # Iterujemy po każdej linii w pliku
    for line in file:
        # Dzielimy linię na kolumny (współrzędne X, Y, klucz)
        columns = line.strip().split('\t')

        # Tworzymy wpis w słowniku
        x, y, key = int(columns[0]), int(columns[1]), columns[2]
        magazyn_dict[key] = {'X': x, 'Y': y}
kroki = []
with open('scripts/zapis_róchów.txt', 'r') as file:
    for line in file:
        kroki.append(line.strip())
kwadraty=[]
linie=[]
pocz=0
koniec=len(kroki)
if int(kroki[1][2:4])%2==0 and kroki[1][5::] not in ['20','00','40']:
    linie.append((magazyn_dict[kroki[1]]['X'], magazyn_dict[kroki[1]]['Y']-50))
else:
    linie.append((magazyn_dict[kroki[1]]['X'], magazyn_dict[kroki[1]]['Y']+50))
for i in range(pocz,koniec):
    kwadraty.append((magazyn_dict[kroki[i]]['X'], magazyn_dict[kroki[i]]['Y']))
    linie.append((magazyn_dict[kroki[i]]['X'], magazyn_dict[kroki[i]]['Y']))
if int(kroki[koniec-1][2:4])%2==0 and kroki[koniec-1][5::] not in ['20','00','40']:
    linie.append((magazyn_dict[kroki[koniec-1]]['X'], magazyn_dict[kroki[koniec-1]]['Y']+50))
else:
    linie.append((magazyn_dict[kroki[koniec-1]]['X'], magazyn_dict[kroki[koniec-1]]['Y']-50))
rysuj_kwadrat(kwadraty)
rysuj_prosta(linie)
    
