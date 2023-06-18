x=int(input("Írj be egy pozitív egész számot: "))
oszt_ö=0
y=1
while y>=x/2:
    if x%y == 0:
        oszt_ö+=y
    y+=1
if oszt_ö == x:
    print('Tökéletes szám!')
else:
    print('Nem tökéletes szám!')
