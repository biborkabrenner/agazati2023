class Balaton:
    def __init__(self, sor:str):
        adatok=sor.strip().split(";")
        self.versenyzo=adatok[0]
        self.rajtszam=int(adatok[1])
        self.kategoria=adatok[2]
        ido=adatok[3].strip().split(":")
        self.ora=int(ido[0])
        self.perc=int(ido[1])
        self.mperc=int(ido[2])
        self.tavszazalek=int(adatok[4])

balaton:list[Balaton]=[]

file=open("ub2017egyeni.txt", "r")
file.readline()
for sor in file:
    balaton.append(Balaton(sor))
file.close

print(f"3. feladat: Egyéni indulók: {len(balaton)} fő")


x=0
for i in balaton:
    if i.kategoria=="Noi":
        x+=1
print(f"4. feladat: Célba érkező női sportolók: {x} fő")

x=input("5. feladat: Kérem a sportoló nevét: ")
y=False
print(f"\tIndult egyéniben a sportoló? ", end="")
for i in balaton:
    if i.versenyzo==x:
        y=True
        print("Igen\n\tTeljesítette a teljes távot? ", end="")
        if i.tavszazalek==100:
            print("Igen")
        else:
            print("Nem")
        break
if y==False:
    print("Nem")


def IdőÓra(i):
    z=float(balaton[i].ora)+float(balaton[i].perc/60)+float(balaton[i].mperc/3600)
    return float(z)

w=0.0
q=0
for i in range(len(balaton)):
    if balaton[i].kategoria=="Ferfi":
        w+=IdőÓra(i)
        q+=1
print(f"7. feladat: Átlagos idő: {w/q} óra")


print("8. feladat: Veseny győztesei")

j=0.0
index=0
ú=0
for i in range(len(balaton)):
    if balaton[i].kategoria=="Noi" and ú==0 and balaton[i].tavszazalek==100:
        j=IdőÓra(i)
        ú+=1
        index=i
    if balaton[i].kategoria=="Noi" and ú==1 and IdőÓra(i)<j and balaton[i].tavszazalek==100:
        j=IdőÓra(i)
        index=i
print(f"\tNők: {balaton[index].versenyzo} ({balaton[index].rajtszam}.) - {balaton[index].ora}:{balaton[index].perc}:{balaton[index].mperc}")

j=0.0
index=0
ú=0
for i in range(len(balaton)):
    if balaton[i].kategoria=="Ferfi" and ú==0 and balaton[i].tavszazalek==100:
        j=IdőÓra(i)
        ú+=1
        index=i
    if balaton[i].kategoria=="Ferfi" and ú==1 and IdőÓra(i)<j and balaton[i].tavszazalek==100:
        j=IdőÓra(i)
        index=i
print(f"\tFérfiak: {balaton[index].versenyzo} ({balaton[index].rajtszam}.) - {balaton[index].ora}:{balaton[index].perc}:{balaton[index].mperc}")