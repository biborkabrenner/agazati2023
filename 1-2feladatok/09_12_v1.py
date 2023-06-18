x=int(input("Írj be egy pozitív egész számot: "))
oszt="1; "
y=2
while y<= x/2:
    if x%y == 0:
        oszt=oszt+"; "+str(y)
    y+=1
print(oszt,x)
