class Repülők:
    def __init__(self, sor:str):
        adatok=sor.strip().split(';')
        self.tipus=adatok[0]
        self.év=int(adatok[1])
        self.utas=adatok[2]
        self.szemelyzet=adatok[3]
        self.utazósebesség=int(adatok[4])
        self.felszallotomeg=int(adatok[5])
        self.fesztav=float(adatok[6].replace(",","."))

repülők:list[Repülők]=[]

file=open("utasszallitok.txt", "r")
file.readline()
for sor in file:
    repülők.append(Repülők(sor))
file.close()

print(f"3.3 feladat: Repülők száma: {len(repülők)}")

x=0
for i in repülők:
    x+=i.utazósebesség
print(f"3.4 feladat: Az átlag sebesség: {float(x/len(repülők)) :.2f} km/h")

y=0.0
index=0
for i in range(len(repülők)):
    if y<repülők[i].fesztav:
        y=repülők[i].fesztav
        index=i
print(f"3.5 feladat: a Legnagyobb fesztávú repülő adatai\n\tTípus: {repülők[index].tipus}\n\tÉv: {repülők[index].év}\n\tUtazó sebesség: {repülők[index].utazósebesség}\n\tFelszállótömeg: {repülők[index].felszallotomeg}\n\tFesztáv: {repülők[index].fesztav}")

stat={}
print("3.6 feladat: Statisztika")
for i in repülők:
    d=str(i.év//10)+"0s"
    if d in stat:
        stat[d]+=1
    else:
        stat[d]=1
for i in stat:
    print(f"\t{i} -> {stat[i]} db")