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
    map_image = Image.open("mapa.jpg")
    draw = ImageDraw.Draw(map_image)
    for x, y in lista_punktow:
        draw.rectangle([x - 12.5, y-12.5, x + 12.5, y+12.5], fill=(255, 0, 0))
    map_image.save("pomoc.jpg")
def rysuj_prosta(lista_punktow):
    map_image = Image.open("pomoc.jpg")
    draw = ImageDraw.Draw(map_image)
    for i in range(len(lista_punktow) - 1):
        (x1, y1) = lista_punktow[i]
        (x2, y2) = lista_punktow[i + 1]
        draw.line([(x1, y1), (x2, y2)], fill=(255, 0, 0), width=5)

    map_image.save("koniec.jpg")
# Otwieramy plik magazyn.txt do odczytu
with open('magazyn.txt', 'r') as file:
    # Inicjalizujemy pusty słownik
    magazyn_dict = {}

    # Iterujemy po każdej linii w pliku
    for line in file:
        # Dzielimy linię na kolumny (współrzędne X, Y, klucz)
        columns = line.strip().split('\t')

        # Tworzymy wpis w słowniku
        x, y, key = int(columns[0]), int(columns[1]), columns[2]
        magazyn_dict[key] = {'X': x, 'Y': y}

kroki=["H103A10","H103A40","H104A40","H104A00","H104A00","H301A00","H301A00","H302A00","H202A00","H202A00","H401A00","H401A00","H401A00","H401A09"]
kwadraty=[]
linie=[]
pocz=0
koniec=len(kroki)
if kroki[0][5::] not in ["20","00","40"]:
    pocz+=1
    liczba=przyporzadkuj(int(kroki[0][5::]))
    if int(kroki[1][2:4])%2==0:
        kwadraty.append((magazyn_dict[kroki[1]]['X']+95*(8-liczba), magazyn_dict[kroki[1]]['Y']))
        if int(kroki[1][5::])%2==0:
            linie.append((magazyn_dict[kroki[1]]['X']+95*(8-liczba), magazyn_dict[kroki[1]]['Y']-50))
        else:
            linie.append((magazyn_dict[kroki[len(kroki)-2]]['X']+95*(8-liczba), magazyn_dict[kroki[1]]['Y']+50))
        linie.append((magazyn_dict[kroki[1]]['X']+95*(8-liczba), magazyn_dict[kroki[1]]['Y']))
    else:
        kwadraty.append((magazyn_dict[kroki[1]]['X']-95*(liczba), magazyn_dict[kroki[1]]['Y']))
        if int(kroki[0][5::])%2==0:
            linie.append((magazyn_dict[kroki[1]]['X']-95*(liczba), magazyn_dict[kroki[1]]['Y']+50))
        else:
            linie.append((magazyn_dict[kroki[1]]['X']-95*(liczba), magazyn_dict[kroki[1]]['Y']-50))
        linie.append((magazyn_dict[kroki[1]]['X']-95*(liczba), magazyn_dict[kroki[1]]['Y']))
if kroki[len(kroki)-1][5::] not in ["20","00","40"]:
    koniec-=1
for i in range(pocz,koniec):
    kwadraty.append((magazyn_dict[kroki[i]]['X'], magazyn_dict[kroki[i]]['Y']))
    linie.append((magazyn_dict[kroki[i]]['X'], magazyn_dict[kroki[i]]['Y']))
    
if kroki[len(kroki)-1][5::] not in ["20","00","40"]:
    liczba=przyporzadkuj(int(kroki[len(kroki)-1][5::]))
    if int(kroki[len(kroki)-1][2:4])%2==0:
        kwadraty.append((magazyn_dict[kroki[len(kroki)-2]]['X']-95*(5-liczba), magazyn_dict[kroki[len(kroki)-2]]['Y']))
        linie.append((magazyn_dict[kroki[len(kroki)-2]]['X']-95*(5-liczba), magazyn_dict[kroki[len(kroki)-2]]['Y']))
        if int(kroki[len(kroki)-1][5::])%2==0:
            linie.append((magazyn_dict[kroki[len(kroki)-2]]['X']-95*(5-liczba), magazyn_dict[kroki[len(kroki)-2]]['Y']-50))
        else:
            linie.append((magazyn_dict[kroki[len(kroki)-2]]['X']-95*(5-liczba), magazyn_dict[kroki[len(kroki)-2]]['Y']+50))
    else:
        kwadraty.append((magazyn_dict[kroki[len(kroki)-2]]['X']+95*(5-liczba), magazyn_dict[kroki[len(kroki)-2]]['Y']))
        linie.append((magazyn_dict[kroki[len(kroki)-2]]['X']+95*(5-liczba), magazyn_dict[kroki[len(kroki)-2]]['Y']))
        if int(kroki[len(kroki)-1][5::])%2==0:
            linie.append((magazyn_dict[kroki[len(kroki)-2]]['X']+95*(5-liczba), magazyn_dict[kroki[len(kroki)-2]]['Y']+50))
        else:
            linie.append((magazyn_dict[kroki[len(kroki)-2]]['X']+95*(5-liczba), magazyn_dict[kroki[len(kroki)-2]]['Y']-50))
rysuj_kwadrat(kwadraty)
rysuj_prosta(linie)
    
