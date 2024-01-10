
def gdzie_idziesz(polorzenie_koncowe, polorzenie_pocznotkowe):
    polorzenie_pocznotkowe = list(polorzenie_pocznotkowe)
    polorzenie_koncowe = list(polorzenie_koncowe)
    prubna_list=[polorzenie_koncowe,polorzenie_pocznotkowe]
    if(polorzenie_pocznotkowe[1] == polorzenie_koncowe[1]):
        print( "".join(polorzenie_pocznotkowe))
        polorzenie_koncowe="".join(polorzenie_koncowe)
        polorzenie_pocznotkowe="".join(polorzenie_pocznotkowe)
        return(polorzenie_koncowe, polorzenie_pocznotkowe)
        
        
    else:
        print("".join(prubna_list[1]))
        prubna_list=poruszanie_po_halah(polorzenie_koncowe, polorzenie_pocznotkowe)
        
        return(prubna_list)
        


   

def poruszanie_po_halah(polorzenie_koncowe, polorzenie_pocznotkowe):
    hala_docelowa = int(polorzenie_koncowe[1])
    hala_początkowy = int(polorzenie_pocznotkowe[1])
    if(hala_początkowy == 1):
            polorzenie_pocznotkowe[1] = str(hala_początkowy + 2)
            polorzenie_pocznotkowe[3] = str(1)
    elif(hala_docelowa % 2 == hala_początkowy % 2):
        if (hala_docelowa>hala_początkowy): #porószanie dla magazynów góra dół 
            polorzenie_pocznotkowe[1] = str(hala_początkowy + 2)
            polorzenie_pocznotkowe[3] = str(1)
        elif (hala_docelowa < hala_początkowy):
            polorzenie_pocznotkowe[1] = str(hala_początkowy - 2)
            polorzenie_pocznotkowe[3] = str(7)
    elif(hala_docelowa % 2 != 0):#porószanie dla magaznów prawo lewo z początkowym nie parzystym
        polorzenie_pocznotkowe[3] = str(5)
        print( "".join(polorzenie_pocznotkowe))
        polorzenie_pocznotkowe[1] = str(hala_początkowy + 1)
    elif(hala_początkowy % 2 != 0):#porószanie dla magaznów prawo lewo z docelowym parzystym
        polorzenie_pocznotkowe[3] = str(2)
        print( "".join(polorzenie_pocznotkowe))
        polorzenie_pocznotkowe[1] = str(hala_początkowy - 1)

    
    
    
    return(gdzie_idziesz(polorzenie_koncowe, polorzenie_pocznotkowe))


polorzenie_pocznotkowe1="H106A00"
polorzenie_koncowe1="H404A06"
prubna_list=[polorzenie_pocznotkowe1,polorzenie_koncowe1]
prubna_list= gdzie_idziesz(polorzenie_koncowe1, polorzenie_pocznotkowe1)

print(prubna_list[1])
