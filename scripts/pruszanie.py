# polorzenie_pocznotkowe1="H106A00"
# polorzenie_koncowe1="H404A06"

def gdzie_idziesz(polorzenie_koncowe, polorzenie_pocznotkowe):
    polorzenie_pocznotkowe = list(polorzenie_pocznotkowe)
    polorzenie_koncowe = list(polorzenie_koncowe)
    prubna_list=[polorzenie_koncowe,polorzenie_pocznotkowe]
    if(polorzenie_pocznotkowe[5] !=0 and polorzenie_pocznotkowe[6] !=0):
        prubna_list=wychodzenie_z_alejek_bocznych(polorzenie_koncowe, polorzenie_pocznotkowe)
    if(prubna_list[1][1]==prubna_list[0][1]):
        print( "".join(prubna_list[1]),6)
        zmienne_dane.append("".join(prubna_list[1]))
        polorzenie_koncowe=prubna_list[0]
        polorzenie_pocznotkowe=prubna_list[1]

        if(polorzenie_pocznotkowe[3]!=polorzenie_koncowe[3]):
            if(int(polorzenie_koncowe[5])*10+int(polorzenie_koncowe[6])>8):
                polorzenie_pocznotkowe[3]=polorzenie_koncowe[3]
                print( "".join(polorzenie_pocznotkowe),12)
                zmienne_dane.append("".join(polorzenie_pocznotkowe))
                polorzenie_pocznotkowe[6]=polorzenie_koncowe[6]
                polorzenie_pocznotkowe[5]=polorzenie_koncowe[5]
            elif(polorzenie_pocznotkowe[3]>=polorzenie_koncowe[3]):
                if(int(polorzenie_koncowe[3])==1):
                    polorzenie_pocznotkowe[3]=str(int(polorzenie_koncowe[3])+1)
                else:
                    polorzenie_pocznotkowe[3]=str(int(polorzenie_koncowe[3])-1)
                print( "".join(polorzenie_pocznotkowe),18)
                zmienne_dane.append("".join(polorzenie_pocznotkowe))
                if(int(polorzenie_koncowe[3])%2==0):
                    polorzenie_pocznotkowe[5]=str(4)
                    polorzenie_pocznotkowe[6]=str(0)
                    print( "".join(polorzenie_pocznotkowe),19)
                    zmienne_dane.append("".join(polorzenie_pocznotkowe))
                else:
                    polorzenie_pocznotkowe[5]=str(2)
                    polorzenie_pocznotkowe[6]=str(0)
                    print( "".join(polorzenie_pocznotkowe),13)
                    zmienne_dane.append("".join(polorzenie_pocznotkowe))
            elif(polorzenie_pocznotkowe[3]<=polorzenie_koncowe[3]):
                if(int(polorzenie_koncowe[3])==7):
                    polorzenie_pocznotkowe[3]=str(int(polorzenie_koncowe[3])-1)
                else:
                    polorzenie_pocznotkowe[3]=str(int(polorzenie_koncowe[3])+1)
                print( "".join(polorzenie_pocznotkowe),18)
                zmienne_dane.append("".join(polorzenie_pocznotkowe))
                if(int(polorzenie_koncowe[3])%2==0):
                    polorzenie_pocznotkowe[5]=str(4)
                    polorzenie_pocznotkowe[6]=str(0)
                    print( "".join(polorzenie_pocznotkowe),19)
                    zmienne_dane.append("".join(polorzenie_pocznotkowe))
                else:
                    polorzenie_pocznotkowe[5]=str(2)
                    polorzenie_pocznotkowe[6]=str(0)
                    print( "".join(polorzenie_pocznotkowe),13)
                    zmienne_dane.append("".join(polorzenie_pocznotkowe))
            polorzenie_pocznotkowe[3]=str(int(polorzenie_koncowe[3]))
            print( "".join(polorzenie_pocznotkowe),14)
            zmienne_dane.append("".join(polorzenie_pocznotkowe))
            polorzenie_pocznotkowe[6]=polorzenie_koncowe[6]
            polorzenie_pocznotkowe[5]=polorzenie_koncowe[5]
        prubna_list=[polorzenie_koncowe,polorzenie_pocznotkowe]
        zmienne_dane.append("".join(prubna_list[1]))
        print( "".join(prubna_list[1]),11)
        prubna_list[0]="".join(prubna_list[0])
        prubna_list[1]="".join(prubna_list[1])
        return(prubna_list)
        
        
    else:
        zmienne_dane.append("".join(prubna_list[1]))
        print("".join(prubna_list[1]),7)
        prubna_list=poruszanie_po_halah(polorzenie_koncowe, polorzenie_pocznotkowe)
        
        return(prubna_list)
        

def wychodzenie_z_alejek_bocznych(polorzenie_koncowe, polorzenie_pocznotkowe):
    if((int(polorzenie_pocznotkowe[5])*10)+int(polorzenie_pocznotkowe[6])<20):
        if((int(polorzenie_pocznotkowe[5])*10)+int(polorzenie_pocznotkowe[6])<=8):
            polorzenie_pocznotkowe[6]=str(0)
        elif(int(polorzenie_pocznotkowe[3])%2==0):
            polorzenie_pocznotkowe[6]=str(0)
            polorzenie_pocznotkowe[5]=str(2)
        else:
            polorzenie_pocznotkowe[6]=str(0)
            polorzenie_pocznotkowe[5]=str(4)
        zmienne_dane.append("".join(polorzenie_pocznotkowe))
        print("".join(polorzenie_pocznotkowe),1)
        if(int(polorzenie_pocznotkowe[5])>=2 and int(polorzenie_pocznotkowe[5])<4 ):
            if(int(polorzenie_pocznotkowe[3])%2==0):
                polorzenie_pocznotkowe[3]=str(int(polorzenie_pocznotkowe[3])-1)
                zmienne_dane.append("".join(polorzenie_pocznotkowe))
                print("".join(polorzenie_pocznotkowe),2)
            
            polorzenie_pocznotkowe[5]=str(0)
            polorzenie_pocznotkowe[6]=str(0)
            zmienne_dane.append("".join(polorzenie_pocznotkowe))
            print("".join(polorzenie_pocznotkowe),3)
        elif(int(polorzenie_pocznotkowe[5])>=4):
            if(int(polorzenie_pocznotkowe[3])%2!=0):
                polorzenie_pocznotkowe[3]=str(int(polorzenie_pocznotkowe[3])+1)
                zmienne_dane.append("".join(polorzenie_pocznotkowe))
                print("".join(polorzenie_pocznotkowe),4)
            polorzenie_pocznotkowe[5]=str(0)
            polorzenie_pocznotkowe[6]=str(0)
            zmienne_dane.append("".join(polorzenie_pocznotkowe))
            print("".join(polorzenie_pocznotkowe),5)
    prubna_list=[polorzenie_koncowe,polorzenie_pocznotkowe]
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
        zmienne_dane.append("".join(polorzenie_pocznotkowe))
        print( "".join(polorzenie_pocznotkowe),8)
        polorzenie_pocznotkowe[1] = str(hala_początkowy + 1)
    elif(hala_początkowy % 2 != 0):#porószanie dla magaznów prawo lewo z docelowym parzystym
        polorzenie_pocznotkowe[3] = str(2)
        zmienne_dane.append("".join(polorzenie_pocznotkowe))
        print( "".join(polorzenie_pocznotkowe),9)
        polorzenie_pocznotkowe[1] = str(hala_początkowy - 1)

    return(gdzie_idziesz(polorzenie_koncowe, polorzenie_pocznotkowe))

zmienne_dane=[]
polorzenie_pocznotkowe1="H106A00"
zmienne_dane.append(polorzenie_pocznotkowe1)
print(polorzenie_pocznotkowe1)
polorzenie_koncowe1="H204A10"
prubna_list=[polorzenie_pocznotkowe1,polorzenie_koncowe1]
prubna_list= gdzie_idziesz(polorzenie_koncowe1, polorzenie_pocznotkowe1)


with open('scripts/zapis_róchów.txt','w') as plik:
    for i in zmienne_dane:
        plik.write(str(i+"\n"))