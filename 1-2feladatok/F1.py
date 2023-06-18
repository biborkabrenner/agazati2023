import random

#1. feladat
def lánchossz(lánc,karakter):
    z=0
    for i in lánc:
        if i==karakter:
            z+=1
    return z

x=input("Kérem a karakter láncot: ")
y=input("Kérem a keresendő karakter: ")
print(f"{y} karakter {lánchossz(x,y)} alkalommal található meg a {x} szóláncban.")


#2.feladat
def terület(a,b):
    T=round(a*b,2)
    return T

a=float(input("Kérem a téglalap egyik oldalát(cm): "))
b=float(input("Kérem a téglalap másik oldalát(cm): "))
print(f"A téglalap területe: {terület(a,b)} cm2")



#3. feladat
def lnko(a,b):
    x=max(a,b)
    y=min(a,b)
    for i in reversed(range(x)):
        if x%i==0 and y%i==0:
            return i

a=int(input("Kérem az egyik számot: "))
b=int(input("Kérem a másik számot: "))
while a==b:
    a=int(input("Kérem az egyik számot: "))
    b=int(input("Kérem a másik számot: "))
print(f"{a} és {b} legnagyobb közös osztólya: {lnko(a,b)}")



#4.feladat
def osztoszam(a):
    x=0
    for i in range(1,a+1):
        if a%i==0:
            x+=1
    return x


a=int(input("Kérek egy számot: ")  )
print(f"{a} számnak {osztoszam(a)} osztólya van.")


#5.feladat
def primszam(a):
    x=0
    for i in range(1,a+1):
        if a%i==0:
            x+=1
    if x==2:
        return "prímszám"
    else:
        return "nem prímszám"


a=int(input("Kérek egy számot: "))
print(f"A {a} {primszam(a)}.")

#6.feladat
def rendprint(x):
    x=sorted(x)
    print(x)

def rend(x):
    x=sorted(x)
    return x

def rendvizs(x):
    if x[0]<x[1] and x[0]<x[2] and x[1]<x[2]:
        return True
    else:
        return False

a=int(input("Kérem az első számot: "))
b=int(input("Kérem a második számot: "))
c=int(input("Kérem a harmadik számot: "))
x=(a,b,c)
print(f"{a} {b} {c} számsor rendezve: {rend(x)[0]} {rend(x)[1]} {rend(x)[2]}")
if rendvizs(x)==True:
    print(f"{a} {b} {c} számsor rendezve van.")
else:
    print(f"{a} {b} {c} számsor nincs rendezve.")

#7. feladat
def rendomlánc(x):
    a=random.randint(1,x+1)
    b=""
    for i in range(a):
        c=random.randint(1,2)
        if c==1:
            b+=chr(random.randint(65,90))
        elif c==2:
            b+=chr(random.randint(97,122))
    return b

x=int(input("Kérem a lánc maximum hosszát: "))
print(rendomlánc(x))

#8.feladat
def utskar(x):
    z=""
    for i in range(-5,0):
        z+=x[i]

    return z

x=input("Kérek egy szóláncot: ")
print(utskar(x))

#9.feladat
def camel(x):
    y=x.split(" ")
    z=[]
    for i in y:
        a=[]
        g=0
        for k in i:
            if g==0:
                a.append(k.upper())
                g+=1
            else:
                a.append(k.lower())
        b=""
        for j in a:
            if j in "öüóqwretzuiopőúasdfghjkléáűíyxcvbnmÖÜÓQWERTZUIOPŐÚASDFGHJKLÉÁŰÍYXCVBNM":
                b+=j
        z.append(b)
    s=""
    for i in z:
        s+=i
    return s

x=input("Szöveg:")
print(camel(x))
    
#10.feladat
a=int(input("Kérek egy számot: "))
b=int(input("Kérek egy kisebb számot: "))
while b>=a:
    a=int(input("Kérek egy számot: "))
    b=int(input("Mondom kérek egy kisebb számot: "))
z=0
for i in range(b,a+1):
    z+=i
print(f"A két szám közötti intervallumba található számok öszzege: {z}")



#11. feladat
def terület(x,y):
    z=x*y
    return z


x=int(input("Kérem az első számot(m): "))
y=int(input("Kérem a második számot(m): "))
try:
    print(f"Telek területe: {terület(x,y)} m2")
except terület(x,y)<100:
    print("Hiba! Túl kicsi a terület!")
except x==-1 or y==-1:
    print("")
while x!=-1 or y!=-1:
    x=int(input("Kérem az első számot(m): "))
    y=int(input("Kérem a második számot(m): "))
    try:
        print(f"Telek területe: {terület(x,y)} m2")
    except terület(x,y)<100:
        print("Hiba! Túl kicsi a terület!")
    except x==-1 or y==-1:
        print("")




