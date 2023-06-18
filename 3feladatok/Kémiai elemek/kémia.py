class Kemia:
    def __init__(self,sor:str):
        adatok=sor.strip().split(";")
        self.ev=adatok[0]
        self.nev=adatok[1]
        self.vegyjel=adatok[2]
        self.rendszam=int(adatok[3])
        self.felfedezo=adatok[4]
kemia:list[Kemia]=[]

file=open("felfedezesek.csv", "r")
file.readline()
for sor in file:
    kemia.append(Kemia(sor))
file.close

print(f"3.feladat: Elemek száma: {len(kemia)}")


x=0
for i in kemia:
    if i.ev=="Ókor":
        x+=1
print(f"4.feladat: Felfedezések száma az ókorban: {x}")


betu=""
for i in range(65,91):
    betu+=chr(i)
for i in range(97,123):
    betu+=chr(i)
y=input("5. feladat: Kérek egy vegyjelet: ")
s=""
for i in y:
    if i in betu:
        s+=i
while len(y)>int(2) or len(y)<int(1) or s!=y:
    y=input("5. feladat: Kérek egy vegyjelet: ")
    s=""
    for i in y:
        if i in betu:
            s+=i
é=0
c=""
if len(y)==2:
    for i in y:
        if é==0:
            c+=i.upper()
            é+=1
        else:
            c+=i.lower()
else:
    c=y.upper()


print("6.feladat: Keresés")
l=0
for i in kemia:
    if c==i.vegyjel:
        print(f"\tAz elem vegyjele: {c}\n\tAz elem neve: {i.nev}\n\tRendszáma: {i.rendszam}\n\tFelfedezés éve: {i.ev}\n\tFelfedező: {i.felfedezo}")
        l=1
        break
if l==0:
    print("Nincs ilyen elem az adatforrásban!")

x=0
for i in range(len(kemia)):
    try:
        y=int(kemia[i+1].ev)-int(kemia[i].ev)
        if y>x:
            x=y
    except:
        x+=0
print(f"7.feladat: {x} év volt a leghosszabb időszak két elem felfedezése között.")


print("8.fealdat: Statisztika")
stat={}
for i in kemia:
    if i.ev not in stat:
        stat[i.ev]=1
    else:
        stat[i.ev]+=1
for i in stat:
    if stat[i]>3 and i!="Ókor":
        print(f"\t{i}: {stat[i]} db")