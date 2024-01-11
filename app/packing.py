from helpers import load_database, load_orders
from attic import database_data, orders_data
from py3dbp import Packer, Bin, Item, Painter
from matplotlib import pyplot as plt
import os

def pack_to_palette(id: str):
    order = ([ord for ord in orders_data if ord['ID'] == id])[0]['Data']
    data = []
    for db_data in database_data:
        for ord_data in order:
            if db_data['ID'] == ord_data['ID']:
                for _ in range(0, ord_data['Amount']):
                    data.append(db_data)
    
    # sort data
    products_data = sorted(data, key=lambda x: x['Weight'], reverse=False)
    palette_dimensions = {'w': 800, 'l': 1200, 'h': 1856}
    
    packer = Packer()
    packer.addBin(Bin('paleta0', (800, 1856, 1200), 1000000, 0, 0))
    for d, i in zip(data, range(0, len(data))):
        w = d['Dimensions'][0]
        h = d['Dimensions'][1]
        l = d['Dimensions'][2]
        item = Item(i, d['Name'], 'cube', (w, h, l), d['Weight'], 1, 1000, True,'white')
        packer.addItem(item)
    
    
    # packer.addBin(Bin('paleta2', (800, 1856, 1200), 1000000, 0, 0))
    packer.pack(
        bigger_first=True,
        fix_point=True,
        distribute_items=True,
        check_stable=False,
        support_surface_ratio=0.75,
        number_of_decimals=0
    )
    
    i = 1
    while len(packer.unfit_items) > 0:
        packer.items = packer.unfit_items
        packer.addBin(Bin(f"paleta{i}", (800, 1856, 1200), 1000000, 0, 0))
        i += 1
        packer.pack(
            bigger_first=True,
            fix_point=True,
            distribute_items=True,
            check_stable=False,
            support_surface_ratio=0.75,
            number_of_decimals=0
        )
    
    figures = []
    for b in packer.bins:
        painter = Painter(b)
        fig = painter.plotBoxAndItems(
            title=b.partno,
            alpha=0.2,         
            write_num=True,   
            fontsize=10        
        )
        figures.append(f"{id}-{b.partno}.png")
        fig.savefig(os.path.join('data', 'plots', f"{id}-{b.partno}.png"))

    return figures

pack_to_palette('1')