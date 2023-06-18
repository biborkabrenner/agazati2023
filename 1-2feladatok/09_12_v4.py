szam=int(input("Adjá számot:  "))
if szam==1:
    print('Definíció szerint nem Prím')
else:
    oszt_db=0
    x=1
    while x<=szam:
        if szam%x==0:
            oszt_db+=1
        x+=1
    if oszt_db==2:
        print('Prím a szám')
    else:
        print('Nem prím')