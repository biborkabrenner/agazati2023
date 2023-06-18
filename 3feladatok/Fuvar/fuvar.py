class Fuvar:
    def __init__(self,sor:str):
        adatok=sor.strip().split(';')
        self.taxiID=int(adatok[0])
        self.indul=adatok[1]
        self.idő=int(adatok[2])
        self.táv=float(adatok[3].replace(",","."))
        self.díj=float(adatok[4].replace(",","."))
        self.borravaló=float(adatok[5].replace(",","."))
        self.fizetésmod=adatok[6]
fuvar:list[Fuvar]=[]

file=open("fuvar.csv","r", encoding="UTF-8")
read=file.readline()
for sor in file:
    fuvar.append(Fuvar(sor))
file.close

print(f"3. feladat: {len(fuvar)} fuvar")

id=6185
utak=0
money=0
for i in fuvar:
    if i.taxiID==id:
        utak+=1
        money+=i.díj
        money+=i.borravaló
print(f"4. feladat {utak} fuvar alatt: {money}$")

bk=0
kp=0
vita=0
ingyé=0
anonim=0
for i in fuvar:
    if i.fizetésmod=="bankkártya":
        bk+=1
    elif i.fizetésmod=="készpénz":
        kp+=1
    elif i.fizetésmod=="vitatott":
        vita+=1
    elif i.fizetésmod=="ingyenes":
        ingyé+=1
    elif i.fizetésmod=="ismeretlen":
        anonim+=1
print(f"5.feladat:\n\tbankkártya: {bk} fuvar\n\tkészpénz: {kp} fuvar\n\tvitatott: {vita} fuvar\n\tingyenes: {ingyé} fuvar\n\tismeretlen: {anonim} fuvar")

mf=0
for i in fuvar:
    mf+=i.táv
km=round(mf*1.6,2)
print(f"6. feladat: {km}km")


time=0
index=0
for i in fuvar:
    if i.idő>time:
        time=i.idő
for i in range(len(fuvar)):
    if time==fuvar[i].idő:
        index=i
print(f"7.feladat: Leghosszabb fuvar:\n\tFuvar hossza: {fuvar[index].idő} másodperc\n\tTaxi azonosító: {fuvar[index].taxiID}\n\tMegtett távolság: {round(fuvar[index].táv*1.6,1)} km\n\tViteldíj: {fuvar[index].díj}$")

file=open("hibak.txt", "w", encoding="UTF-8")
file.write(read)
for i in fuvar:
    if i.táv==0 and i.díj>0 and i.idő>0:
        file.write(f"{i.taxiID};{i.indul};{i.idő};{i.táv};{i.díj};{i.borravaló};{i.fizetésmod}\n")
file.close()
print("8. feladat: hibak.txt")