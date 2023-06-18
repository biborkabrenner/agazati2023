import random

x = random.randint(1, 100)
y = int(input('Kérem a számot 1-100: '))
z = 1
while y != x:
    if y > x:
        y = int(input('Kisebbet kérek: '))
        z = z + 1
    if x > y:
        y = int(input('Nagyobbbat kérek: '))
        z = z + 1
print('Gratulálok eltaláltad ', z, ' lépésből!')
