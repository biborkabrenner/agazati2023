#1.feladat szorzás
while True:
    y=int(input("Kérem az első számot: "))
    if y==-1:
        break
    x=int(input("Kérem a második számot: "))
    if x==-1:
        break
    z=1
    for i in range(y,x+1):
        z*=i
    print(f"Az intervallumban található számok szorzata: {z}")

#1.feladat összeadás
while True:
    y=int(input("Kérem az első számot: "))
    if y==-1:
        break
    x=int(input("Kérem a második számot: "))
    if x==-1:
        break
    z=0
    for i in range(y,x+1):
        z+=i
    print(f"Az intervallumban található számok összege: {z}")

#2.feladat
def terület(x,y):
    z=x*y
    if z<100:
        raise ValueError("Hiba! Túl kicsi a terület!")
    return z

while True:
    x=int(input("Kérem az első számot(m): "))
    if x==0:
        break
    y=int(input("Kérem a második számot(m): "))
    if y==0:
        break
    try:
        print(f"Telek területe: {terület(x,y)} m2")
    except ValueError as hiba:
        print(hiba)
