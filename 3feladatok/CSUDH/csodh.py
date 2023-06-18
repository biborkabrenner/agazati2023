class Adatok:
    def __init__(self, sor:str):
        adatok=sor.strip().split(";")
        self.domain=adatok[0]
        self.IP=adatok[1]
        
csudh:list[Adatok]=[]

file=open("csudh.txt", "r")
file.readline()
for sor in file:
    csudh.append(Adatok(sor))
file.close()

def Domain(szint, ip):
    egy="nincs"
    ket="nincs"
    ha="nincs"
    negy="nincs"
    öt="nincs"
    for i in csudh:
        if ip==i.IP:
            y=i.domain.split('.')
    if len(y)==1:
        egy=y[0]
    elif len(y)==2:
        egy=y[1]
        ket=y[0]
    elif len(y)==3:
        egy=y[2]
        ket=y[1]
        ha=y[0]
    elif len(y)==4:
        egy=y[3]
        ket=y[2]
        ha=y[1]
        negy=[0]
    elif len(y)==5:
        egy=y[4]
        ket=y[3]
        ha=y[2]
        negy=y[1]
        öt=y[0]
    if szint==1:
        return egy
    elif szint==2:
        return ket
    elif szint==3:
        return ha
    elif szint==4:
        return negy
    elif szint==5:
        return öt
    



print(f"3. feladat: Domainek száma: {len(csudh)}")

ip=csudh[0].IP
print(f"5.feladat: Az első domain felépítése:\n\t1. szint: {Domain(1,ip)}\n\t2. szint: {Domain(2,ip)}\n\t3. szint: {Domain(3,ip)}\n\t4. szint: {Domain(4,ip)}\n\t5. szint: {Domain(5,ip)}")

file=open("table.html", "w")
file.write(f"Ssz\tHostname\tHost IP címe\t1.szint\t2.szint\t3.szint\t4.szint\t5.szint")
for i in range(len(csudh)):
    file.write(f"{i+1}.\t{csudh[i].domain}\t{csudh[i].IP}\t{Domain(1,csudh[i].IP)}\t{Domain(2,csudh[i].IP)}\t{Domain(3,csudh[i].IP)}\t{Domain(4,csudh[i].IP)}\t{Domain(5,csudh[i].IP)}")
file.close()