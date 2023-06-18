import math
print('1.feladat: Számok szorzata')
print('Kérem az alsó és a felső határt:')
a=int(input('a= '))
b=int(input('b= '))
while a>b:
    print('Az alsó határ kisebb legyen!')
    a=int(input('a= '))
    b=int(input('b= '))

o=a
a=a+1
while a!=b+1:
   
   o=o*(a)
   a+=1 

print(o)


print('2.feladat:Derékszögű háromszög átfogójának kiszámítása!')

def atfogo(a,b):
    v=a*a+b*b
    o=math.sqrt(v)
    if o<5:
        raise ValueError('Hiba! Túl kicsi a derékszögű háromszög!')
    else:
        return o


print('Kérem a két befogó méretét!')
 
while True:
    a=float(input('Egyik befogó mérete: '))
    if a==0:
        break
    b=float(input('Másik befogó mérete: '))
    if b==0:
        break
    try:        
        print(f'Az átfogó mérete:{atfogo(a,b):.2f}')
    except ValueError as hiba:
        print(hiba)



print('3.feladat:Repülők')

class Utassz:
    def __init__(self,sor:str):
        adatok=sor.strip().split(';')
        self.tip=adatok[0]
        self.ev=int(adatok[1])
        self.utas=adatok[2]
        if '-' in adatok[2]:
            utas=adatok[2].split('-')
            self.maxutas=int(utas[1])
        else:
            self.maxutas=int(adatok[2])
        self.szemelyz=adatok[3]
        if '-' in adatok[3]:
            szem=adatok[3].split('-')
            self.maxszem=int(szem[1])
        else:
            self.maxszem=int(adatok[3])
        self.utazoseb=adatok[4]
        if int(adatok[4])>500:
            self.kategória='Alacsony sebességű'
        elif int(adatok[4])>1000:
            self.kategória='Szubszonikus'
        elif int(adatok[4])>1200:
            self.kategória='Transzszonikus'
        else: 
            self.kategória='Szuperszonikus'
        self.felsztomeg=adatok[5]
        self.fesztav=float(adatok[6].replace(',', '.'))

utasszallitok:list[Utassz]=[]

file=open('utasszallitok.txt', 'r')
fejlec=file.readline()
for sor in file:
    utasszallitok.append(Utassz(sor))

file.close()

print(f'3.2feladat: Adatsorok száma: {len(utasszallitok)}')
lg=0.0
for i in utasszallitok:
    if i.fesztav>lg:
        lg=i.fesztav
for h in utasszallitok:
    if h.fesztav==lg:
        print(f'3.3feladat: Legnagyobb fesztávú utasszallátó típus: {i.tip}')
    


o=0
for i in utasszallitok:
    if 'Boeing' in i.tip:
        o+=1
print(f'3.4feladat= Boeing típusok száma:{o} ')

file=open('utasstallitok_new.txt','w', encoding='utf-8')
file.write(f'{fejlec}n')
#for i in utasszallitok:
#    file.write(f'{i.tip};{i.ev};{i.maxutas};{i.maxszem};{i.utazoseb};{i.felsztomeg//1000};{i.fesztav*3-2808:.0f}\n;')
file.close()


stat={}
for i in utasszallitok:
    et=str(i.ev//10)+'0s'
    if et in stat:
        stat[et]+=1
    else:
        stat[et]=1
for j in stat:
    print(f'{j}->{stat[j]} db')