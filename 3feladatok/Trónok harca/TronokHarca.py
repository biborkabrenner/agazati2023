class Epizodok:
    def __init__(self,sor:str):
        adatok=sor.strip().split(";")
        self.name=adatok[0]
        self.season=int(adatok[1])
        self.number=int(adatok[2])
        self.airdate=adatok[3]
        self.runtime=int(adatok[4])
        self.rating=float(adatok[5])
        self.summary=adatok[6]

epizodok:list[Epizodok]=[]

file=open("game_of_thrones.csv", "r")
file.readline()
for sor in file:
    epizodok.append(Epizodok(sor))
file.close

print(f"3. feladat: Összes epizód száma: {len(epizodok)}")

x=int(input("4. feladat: Évad sorszáma: "))
y=0
z=0
for i in epizodok:
    if i.season==x:
        y+=i.rating
        z+=1
print(f"\tAz évad átlagos értékelése: {y/z}")

a=""
b=""
for i in epizodok:
    if x==i.season and 1==i.number:
        a=i.airdate
    if x==i.season and z==i.number:
        b=i.airdate

v=a.split(" ")
c=v[0].split("-")
d=0
if int(c[0])%4!=0:
    if int(c[1])>=2:
        d+=31
    if int(c[1])>=3:
        d+=28
    if int(c[1])>=4:
        d+=31
    if int(c[1])>=5:
        d+=30
    if int(c[1])>=6:
        d+=31
    if int(c[1])>=7:
        d+=30
    if int(c[1])>=8:
        d+=31
    if int(c[1])>=9:
        d+=31
    if int(c[1])>=10:
        d+=30
    if int(c[1])>=11:
        d+=31
    if int(c[1])>=12:
        d+=30
else:
    if int(c[1])>=2:
        d+=31
    if int(c[1])>=3:
        d+=29
    if int(c[1])>=4:
        d+=31
    if int(c[1])>=5:
        d+=30
    if int(c[1])>=6:
        d+=31
    if int(c[1])>=7:
        d+=30
    if int(c[1])>=8:
        d+=31
    if int(c[1])>=9:
        d+=31
    if int(c[1])>=10:
        d+=30
    if int(c[1])>=11:
        d+=31
    if int(c[1])>=12:
        d+=30
d+=int(c[2])


g=b.split(" ")
e=g[0].split("-")
f=0
if int(e[0])%4!=0:
    if int(e[1])>=2:
        f+=31
    if int(e[1])>=3:
        f+=28
    if int(e[1])>=4:
        f+=31
    if int(e[1])>=5:
        f+=30
    if int(e[1])>=6:
        f+=31
    if int(e[1])>=7:
        f+=30
    if int(e[1])>=8:
        f+=31
    if int(e[1])>=9:
        f+=31
    if int(e[1])>=10:
        f+=30
    if int(e[1])>=11:
        f+=31
    if int(e[1])>=12:
        f+=30
else:
    if int(e[1])>=2:
        f+=31
    if int(e[1])>=3:
        f+=29
    if int(e[1])>=4:
        f+=31
    if int(e[1])>=5:
        f+=30
    if int(e[1])>=6:
        f+=31
    if int(e[1])>=7:
        f+=30
    if int(e[1])>=8:
        f+=31
    if int(e[1])>=9:
        f+=31
    if int(e[1])>=10:
        f+=30
    if int(e[1])>=11:
        f+=31
    if int(e[1])>=12:
        f+=30
f+=int(e[2])
print(f"5. feladat: Az első ({c[0]}.{c[1]}.{c[2]}.) és utolsó ({e[0]}.{e[1]}.{e[2]}.) epizódja között {f-d} nap teld el.")